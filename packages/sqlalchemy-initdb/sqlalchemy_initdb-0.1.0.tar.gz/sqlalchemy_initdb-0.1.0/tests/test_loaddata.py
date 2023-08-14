from collections.abc import Iterator
from pathlib import Path

from sqlalchemy_initdb.loaddata import collect_fixtures


def test_collect_fixtures():
    """Test collect_fixtures."""

    fixtures = collect_fixtures()
    assert isinstance(fixtures, Iterator)
    assert len(list(fixtures)) > 0
    assert all(isinstance(fixture, Path) for fixture in fixtures)
