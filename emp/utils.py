# coding: utf-8

from __future__ import absolute_import as _absolute_import
from __future__ import print_function as _print_function
from __future__ import unicode_literals as _unicode_literals

# public items
__all__ = [
    'check_dependencies',
    'clone_github',
    'clone_gitlab',
    'clone_url',
    'join_path',
    'parse_user_repo',
    'prompt',
    'run_script',
]

# standard library
import os
import re
import sys
from logging import getLogger
from subprocess import Popen, PIPE, STDOUT

if sys.version_info[0] == 2:
    input = raw_input

# dependent packages
import emp
import yaml

# local constants
URL_GITHUB = 'https://github.com/{0}/{1}.git'
URL_GITLAB = 'https://gitlab.com/{0}/{1}.git'


# functions
def check_dependencies(dependencies, cwd=None, logger=None):
    logger = logger or getLogger('emp.check_dependencies')

    for dependency in dependencies:
        if run_script(dependency['try'], False, cwd=cwd, logger=logger):
            if run_script(dependency['except'], True, cwd=cwd, logger=logger):
                return 1

    return 0


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


def join_path(*paths):
    from os.path import expanduser, join, realpath
    return realpath(expanduser(join(*paths)))


def parse_user_repo(args):
    if args['--github']:
        try:
            user, repo = args['--github'].split('/')
        except ValueError:
            user, repo = args['--github'], emp.EMPREPO
    elif args['--gitlab']:
        try:
            user, repo = args['--gitlab'].split('/')
        except ValueError:
            user, repo = args['--gitlab'], emp.EMPREPO
    elif args['--url']:
        user, repo = None, args['--url'].split('/')[-1].rsplit('.git')
    else:
        user, repo = None, ''

    return user, repo

def prompt(question, returntrue='^[Y|y]', logger=None):
    logger = logger or getLogger('emp.prompt')
    answer = input('{0} '.format(question))
    logger.info('{0} --> {1}'.format(question, answer))
    return bool(re.search(returntrue, answer))


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
