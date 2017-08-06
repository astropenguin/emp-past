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
def command(empfiles, mode, minimum=False, force=False):
    for path in glob.glob(emp.join_path(empfiles, '*')):
        dirname = os.path.basename(path)
        filename = emp.join_path(path, emp.CONFIGFILE)

        if not os.path.exists(filename):
            continue

        with open(filename) as f:
            configs = yaml.load(f)

        logger = getLogger('emp.{0}'.format(dirname))
        question = '{0}: {1}?'.format(dirname, mode)
        answer = force or emp.prompt(question, logger=logger)

        if (mode in configs) and answer:
            config = configs[mode]
            emp.check_dependencies(config['dependencies'], logger=logger)
            if minimum:
                emp.run_script(config['minimum'], cwd=path, logger=logger)
            else:
                emp.run_script(config['default'], cwd=path, logger=logger)


install = partial(command, mode='install')
backup = partial(command, mode='backup')
uninstall = partial(command, mode='uninstall')
