# coding: utf-8

"""Empower your Mac with simple config files"""

from __future__ import absolute_import as _absolute_import
from __future__ import print_function as _print_function
from __future__ import unicode_literals as _unicode_literals

# standard library
from setuptools import setup, find_packages


# main
setup(
    name = 'emp',
    description = __doc__,
    version = '0.1.5',
    author = 'snoopython',
    author_email = 'taniguchi@ioa.s.u-tokyo.ac.jp',
    url = 'https://github.com/snoopython/emp',
    entry_points = {'console_scripts': ['emp=emp.cli:main']},
    install_requires = ['docopt', 'pyyaml'],
    packages = find_packages(),
)
