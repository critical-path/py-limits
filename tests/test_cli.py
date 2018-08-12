from limits.cli import limits

from click.testing import CliRunner

from constants import (
    ENDPOINT,
    JSON,
    CORE_MESSAGE,
    SEARCH_MESSAGE,
    GRAPHQL_MESSAGE
)

from pytest import (
    mark,
    raises
)

from responses import (
    activate,
    add,
    GET
)

@activate
@mark.parametrize("status_code", [400, 500])
def test_cli_http_error(status_code):
    add(method=GET, url=ENDPOINT, body=JSON, status=status_code)

    runner = CliRunner()
    result = runner.invoke(limits)
    assert result.exit_code != 0

@activate
def test_cli_non_200_status_code():
    add(method=GET, url=ENDPOINT, body=JSON, status=201)

    runner = CliRunner()
    result = runner.invoke(limits)
    assert result.exit_code == 0
    
@activate
def test_cli():
    add(method=GET, url=ENDPOINT, body=JSON, status=200)

    runner = CliRunner()
    result = runner.invoke(limits)
    assert result.exit_code == 0
    assert result.output == "Core\n----\n{}".format(CORE_MESSAGE) + "\n"

@activate
def test_cli_with_core():
    add(method=GET, url=ENDPOINT, body=JSON, status=200)

    runner = CliRunner()
    result = runner.invoke(limits, ["--core"])
    assert result.exit_code == 0
    assert result.output == "Core\n----\n{}".format(CORE_MESSAGE) + "\n"

@activate
def test_cli_with_search():
    add(method=GET, url=ENDPOINT, body=JSON, status=200)

    runner = CliRunner()
    result = runner.invoke(limits, ["--no-core", "--search"])
    assert result.exit_code == 0
    assert result.output == "Search\n------\n{}".format(SEARCH_MESSAGE) + "\n"

@activate
def test_cli_with_graphql():
    add(method=GET, url=ENDPOINT, body=JSON, status=200)

    runner = CliRunner()
    result = runner.invoke(limits, ["--no-core", "--graphql"])
    assert result.exit_code == 0
    assert result.output == "GraphQL\n-------\n{}".format(GRAPHQL_MESSAGE) + "\n"

@activate
def test_cli_with_core_search_and_graphql():
    add(method=GET, url=ENDPOINT, body=JSON, status=200)

    runner = CliRunner()
    result = runner.invoke(limits, ["--core", "--search", "--graphql"])
    assert result.exit_code == 0
    assert result.output == "Core\n----\n{}".format(CORE_MESSAGE) + "\n" +\
                            "Search\n------\n{}".format(SEARCH_MESSAGE) + "\n" +\
                            "GraphQL\n-------\n{}".format(GRAPHQL_MESSAGE) + "\n"                     
