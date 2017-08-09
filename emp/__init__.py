# coding: utf-8

from __future__ import absolute_import as _absolute_import
from __future__ import print_function as _print_function
from __future__ import unicode_literals as _unicode_literals

# information
__version__ = '0.1.5'
__author__  = 'snoopython'

# submodules
from .constants import *
from .commands import *
from .logging import *
from .utils import *
del constants
del commands
del logging
del utils

# default logger
import logging
logger = logging.getLogger('emp')
setlogfile(logger=logger)
setloglevel(logger=logger)
del logging
