# coding: utf-8

from __future__ import absolute_import as _absolute_import
from __future__ import print_function as _print_function
from __future__ import unicode_literals as _unicode_literals

# public items
__all__ = [
    'setlogfile',
    'setloglevel',
]

# standard library
import logging
import os
import sys

# dependent packages
import emp

# local constants
DATEFORMAT = '%Y-%m-%d %H:%M:%S'
FORMAT = '%(asctime)s %(name)s [%(levelname)s] %(message)s'


# functions
def setlogfile(filename=None, overwrite=False, logger=None):
    logger = logger or emp.logger

    for handler in logger.handlers:
        handler.close()
        logger.removeHandler(handler)

    if filename is None:
        handler = logging.StreamHandler(sys.stdout)
    else:
        filename = os.path.expanduser(filename)
        if overwrite:
            handler = logging.FileHandler(filename, 'w', encoding='utf-8')
        else:
            handler = logging.FileHandler(filename, 'a', encoding='utf-8')

    formatter = logging.Formatter(FORMAT, DATEFORMAT)
    handler.setFormatter(formatter)
    handler.setLevel(logger.level)
    logger.addHandler(handler)


def setloglevel(level='INFO', logger=None):
    logger = logger or emp.logger

    logger.setLevel(level.upper())
    for handler in logger.handlers:
        handler.setLevel(level.upper())
