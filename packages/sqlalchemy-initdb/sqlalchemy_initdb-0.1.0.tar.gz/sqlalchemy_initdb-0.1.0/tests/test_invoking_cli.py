import pytest
from click.testing import CliRunner

from sqlalchemy_initdb.cli import main


@pytest.fixture
def cli_runner():
    """Fixture for invoking command-line interfaces (CLIs)."""
    return CliRunner()


def test_invoking_cli_as_python_module(cli_runner):
    result = cli_runner.invoke(main, ["--help"])
    assert result.exit_code == 0
    assert result.output.split("\n")[0] == "Usage: main [OPTIONS]"
