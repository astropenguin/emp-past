# coding: utf-8

"""Empower your Mac with simple dotfiles.

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
  -m --minimum          Run subcommand with a minimum script.
  --github <user/repo>  Clone a dotfiles' repository from GitHub.
  --gitlab <user/repo>  Clone a dotfiles' repository from GitLab.
  --url <url>           Clone a dotfiles' repository from a URL.

"""

from __future__ import absolute_import as _absolute_import
from __future__ import print_function as _print_function
from __future__ import unicode_literals as _unicode_literals

# dependent packages
import emp
from docopt import docopt


# functions
def main():
    args = docopt(__doc__)

    # clone repository (optional)
    user, repo = emp.parse_user_repo(args)
    empfiles = emp.join_path(args['path'], repo)

    if args['--github']:
        emp.clone_github(user, repo)
    elif args['--gitlab']:
        emp.clone_gitlab(user, repo)
    elif args['--url']:
        emp.clone_url(args['--url'])

    # main command
    minimum = args['--minimum']
    force = args['--force']

    if args['--install']:
        emp.install(empfiles, minimum, force)
    elif args['--backup']:
        emp.backup(empfiles, minimum, force)
    elif args['--uninstall']:
        emp.uninstall(empfiles, minimum, force)


# main
if __name__ == '__main__':
    main()
