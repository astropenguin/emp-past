# coding: utf-8

from __future__ import absolute_import
from __future__ import print_function
from __future__ import unicode_literals

# public items
__all__ = [
    'call',
    'clone_github',
    'clone_gitlab',
    'clone_url',
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
def call(cmds, shell=False, logger=None):
    logger = logger or emp.logger
    proc = Popen(cmds, shell=shell, stdout=PIPE, stderr=STDOUT)

    while True:
        line = proc.stdout.readline()
        if line:
            logger.info(line.decode('utf-8').rstrip())
        else:
            returncode = proc.poll()
            if returncode is not None:
                return returncode


def clone_github(args):
    try:
        user, repo = args['--github'].split('/')
    except ValueError:
        user, repo = args['--github'], REPO

    cmds = ['git', 'clone', URL_GITHUB.format(user, repo)]
    logger = getLogger('emp.clone_github')
    return call(cmds, logger=logger)


def clone_gitlab(args):
    try:
        user, repo = args['--gitlab'].split('/')
    except ValueError:
        user, repo = args['--gitlab'], REPO

    cmds = ['git', 'clone', URL_GITLAB.format(user, repo)]
    logger = getLogger('emp.clone_gitlab')
    return call(cmds, logger=logger)


def clone_url(args):
    cmds = ['git', 'clone', args['--url']]
    return call(cmds, logger=logger)
