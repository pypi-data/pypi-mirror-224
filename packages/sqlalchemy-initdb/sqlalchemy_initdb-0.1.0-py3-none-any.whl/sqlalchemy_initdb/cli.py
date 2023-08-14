"""Main `sqlalchemy_initdb` CLI."""

import os
import sys

import click

from sqlalchemy_initdb import __version__

this_file_location = os.path.dirname(os.path.realpath(os.path.abspath(__file__)))


def version_msg():
    """sqlalchemy_initdb version, location and Python version.

    Get message about sqlalchemy_initdb version, location
    and Python version.
    """
    python_version = sys.version[:3]
    message = "SQLAlchemy InitDB %(version)s from {} (Python {})"
    location = os.path.dirname(this_file_location)
    return message.format(location, python_version)


@click.command(context_settings=dict(help_option_names=["-h", "--help"]))
@click.version_option(__version__, "-V", "--version", message=version_msg())
@click.option("-v", "--verbose", is_flag=True, help="Print debug information", default=False)
def main(
    verbose,
):
    """TODO Write this content that gets renders when invoking with --help flag!

    Eg:
    Create a Project from the project template.

    Cookiecutter Python Package is Free/Libre Open Source Software. If you would
    like to get in touch, please see
    https://github.com/boromir674/cookiecutter-python-package.
    """
    try:
        pass
    except Exception as error:
        click.echo(error)
        sys.exit(1)


if __name__ == "__main__":  # pragma: no cover
    main()
