# coding: utf-8

from __future__ import absolute_import
from __future__ import print_function
from __future__ import unicode_literals

from .cmds import *
from .logging import *
from .utils import *
del cmds
del logging
del utils

# default logger
import logging
logger = logging.getLogger('emp')
setlogfile(logger=logger)
setloglevel(logger=logger)
del logging
