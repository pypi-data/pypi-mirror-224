"""Run `python -m sqlalchemy_initdb`.

Allow running SQLAlchemy InitDB, also by invoking
the python module:

`python -m sqlalchemy_initdb`

This is an alternative to directly invoking the cli that uses python as the
"entrypoint".
"""
from __future__ import absolute_import

from sqlalchemy_initdb.cli import main

if __name__ == "__main__":  # pragma: no cover
    main(prog_name="sqlalchemy-initdb")
