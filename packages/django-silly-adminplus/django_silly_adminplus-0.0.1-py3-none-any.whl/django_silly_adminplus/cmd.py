#! /usr/bin/env python3

from flamewok.cli import cli
from django_silly_adminplus import __version__, __home_page__

import os
import shutil

BASE_DIR = os.path.abspath(os.path.dirname(__file__))


def plop():
    "plop's the installer in your cwd"
    file = os.path.join(BASE_DIR, "plop/adminplus.html")
    cwd = os.getcwd()
    shutil.copy(file, cwd)
    print(f"template plopped in {cwd}")


def cmd():
    cli.route(
        "HELP",
        (["", "-h", "--help"], cli.help, "display this help"),
        "ACTIONS",
        ("plop", plop, "provides a 'adminplus.html' template in the current directory"),
        "ABOUT",
        "package: Django Silly Adminplus",
        f"version: {__version__}",
        f"home page : {__home_page__}",
    )


if __name__ == '__main__':
    cmd()
