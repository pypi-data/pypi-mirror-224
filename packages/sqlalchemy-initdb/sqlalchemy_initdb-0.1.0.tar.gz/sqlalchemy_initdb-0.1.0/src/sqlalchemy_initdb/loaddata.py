import importlib
import json
from collections.abc import Iterator, Sequence
from itertools import groupby
from pathlib import Path

from sqlalchemy import Engine, insert
from sqlalchemy.orm import Session


def collect_fixtures() -> Iterator[Path]:
    """Collect all fixtures from the fixtures directory."""
    return (e for e in Path.cwd().glob("*/*/fixtures/*.json"))


def _get_model_class(model: str) -> type:
    """Get model class from model string."""
    model_module_path, model_class_name = model.rsplit(".", 1)
    model_module = importlib.import_module(model_module_path)
    return getattr(model_module, model_class_name)


def initialize(engine: Engine, fixtures: Sequence[Path]) -> int:
    """Load data from fixtures into sqlalchemy db.

    Args:
        engine: SQLAlchemy engine.
        fixtures: Iterator of fixtures.
    Returns:
        Number of fixtures loaded.
    """

    with Session(engine) as session:
        num_rows = 0
        for fixture in fixtures:
            with fixture.open() as fixture_file:
                data = json.load(fixture_file)
                num_rows += len(data)

                # Group by model
                data = groupby(data, key=lambda x: x["model"])

                # Insert rows for each model
                for model_path, rows in data:
                    model = _get_model_class(model_path)
                    session.execute(
                        statement=insert(model), params=[e["fields"] for e in rows]
                    )

        session.commit()
        return num_rows
