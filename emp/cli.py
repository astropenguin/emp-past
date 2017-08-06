# coding: utf-8

"""Empower your Mac with simple config files.

Usage:
  emp install <path> [options]
  emp backup <path> [options]
  emp uninstall <path> [options]
  emp -h | --help
  emp -v | --version

Options:
  -h --help             Show this screen and exit.
  -v --version          Show the version and exit.
  -f --force            Force to answer every question with Yes.
  -m --minimal          Run a command with a minimal script.
  --github <user/repo>  Clone a dotfiles' repository from GitHub.
  --gitlab <user/repo>  Clone a dotfiles' repository from GitLab.
  --url <url>           Clone a dotfiles' repository from a URL.
  --log <filename>      Output log to a file instead of stdout.

"""

from __future__ import absolute_import as _absolute_import
from __future__ import print_function as _print_function
from __future__ import unicode_literals as _unicode_literals

# standard library
import sys

# dependent packages
import emp
from docopt import docopt


# functions
def main():
    args = docopt(__doc__, version=emp.__version__)
    logger = emp.logger

    # set logfile (optional)
    if args['--log']:
        emp.setlogfile(args['--log'], True)

    logger.info(' '.join(sys.argv[1:]))

    # clone repository (optional)
    user, repo = emp.parse_user_repo(args)
    empfiles = emp.join_path(args['<path>'], repo)

    code = 0
    if args['--github']:
        logger.info('clone a repository from {0}/{1}'.format(user, repo))
        code = emp.clone_github(user, repo, logger=logger)
    elif args['--gitlab']:
        logger.info('clone a repository from {0}/{1}'.format(user, repo))
        code = emp.clone_gitlab(user, repo, logger=logger)
    elif args['--url']:
        logger.info('clone a repository from {0}'.format(url))
        code = emp.clone_url(args['--url'], logger=logger)

    if code:
        logger.error('emp finished with an error')
        sys.exit()

    # main command
    minimal = args['--minimal']
    force = args['--force']

    if args['install']:
        emp.install(empfiles, minimal, force)
    elif args['backup']:
        emp.backup(empfiles, minimal, force)
    elif args['uninstall']:
        emp.uninstall(empfiles, minimal, force)

    # finally
    logger.info('emp finished')


# main
if __name__ == '__main__':
    main()
