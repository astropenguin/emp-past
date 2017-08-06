# coding: utf-8

from __future__ import absolute_import as _absolute_import
from __future__ import print_function as _print_function
from __future__ import unicode_literals as _unicode_literals

# public items
__all__ = [
    'clone_github',
    'clone_gitlab',
    'clone_url',
    'run_script',
]

# standard library
import os
from logging import getLogger
from subprocess import Popen, PIPE, STDOUT

# dependent packages
import emp
import yaml

# local constants
REPO = 'dotfiles'
URL_GITHUB = 'https://github.com/{0}/{1}.git'
URL_GITLAB = 'https://gitlab.com/{0}/{1}.git'


# functions
def clone_github(user, repo, cwd=None, logger=None):
    logger = logger or getLogger('emp.clone_github')
    cmds = 'git clone ' + URL_GITHUB.format(user, repo)
    return run_script(cmds, cwd=cwd, logger=logger)


def clone_gitlab(user, repo, cwd=None, logger=None):
    logger = logger or getLogger('emp.clone_gitlab')
    cmds = 'git clone ' + URL_GITLAB.format(user, repo)
    return run_script(cmds, cwd=cwd, logger=logger)


def clone_url(url, cwd=None, logger=None):
    logger = logger or getLogger('emp.clone_url')
    cmds = 'git clone ' + url
    return run_script(cmds, cwd=cwd, logger=logger)








def run_script(cmds, log=True, cwd=None, logger=None):
    logger = logger or getLogger('emp.run_script')
    proc = Popen(cmds, stdout=PIPE, stderr=STDOUT, shell=True, cwd=cwd)

    while True:
        line = proc.stdout.readline()
        if line and log:
            logger.info(line.decode('utf-8').rstrip())
        else:
            returncode = proc.poll()
            if returncode is not None:
                return returncode
