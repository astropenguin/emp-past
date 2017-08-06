# coding: utf-8

from __future__ import absolute_import as _absolute_import
from __future__ import print_function as _print_function
from __future__ import unicode_literals as _unicode_literals

# public items
__all__ = [
    'install',
    'backup',
    'uninstall',
]

# standard library
import os
import glob
from functools import partial
from logging import getLogger

# dependent packages
import emp
import yaml


# functions
def command(empfiles, minimal=False, force=False, mode='install'):
    for path in glob.glob(emp.join_path(empfiles, '*')):
        dirname = os.path.basename(path)
        filename = emp.join_path(path, emp.CONFIGFILE)
        logger = getLogger('emp.{0}'.format(dirname))

        if os.path.exists(filename):
            with open(filename) as f:
                configs = yaml.load(f)
        else:
            continue

        if mode in configs:
            config = configs[mode]
        else:
            continue

        question = '{0}: {1}? [y/n]'.format(dirname, mode)
        if force or emp.prompt(question, logger=logger):
            # check dependencies
            if 'dependencies' in config:
                cmds = config['dependencies']

                logger.info('start checking dependencies')
                if emp.check_dependencies(cmds, cwd=path, logger=logger):
                    logger.error('failed to install dependencies')
                    logger.error('skipped execution')
                    continue
                else:
                    logger.info('finish checking dependencies')

            # execute command
            if 'default' in config:
                cmds = config['default']
            else:
                logger.error('default script is not found')
                logger.error('skipped execution')
                continue

            if minimal:
                if 'minimal' in config:
                    cmds = config['minimal']
                else:
                    logger.warning('minimal script is not found')
                    logger.warning('using default script instead')

            logger.info('start execution')
            if emp.run_script(cmds, cwd=path, logger=logger):
                logger.error('failed to finish execution')
                continue
            else:
                logger.info('finish execution')
        else:
            logger.info('skipped execution')


install = partial(command, mode='install')
backup = partial(command, mode='backup')
uninstall = partial(command, mode='uninstall')
