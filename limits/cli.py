"""The command-line interface for py-limits."""


from limits.lib import (
    parse_data,
    parse_reset,
    parse_response,
    send_request,
    set_message
)


from click import (
    command,
    echo,
    option
)


@command()
@option("--core/--no-core", default=True, help="Core API")
@option("--search/--no-search", default=False, help="Search API")
@option("--graphql/--no-graphql", default=False, help="GraphQL API")
def limits(core, search, graphql):
    """Command-line util that retrieves rate limits from GitHub."""

    response = send_request()

    if response.status_code == 200:
        core_data, search_data, graphql_data = parse_response(response)

        # Core API

        if core:
            limit, remaining, reset = parse_data(core_data)
            time = parse_reset(reset)
            message = set_message(limit, remaining, time)
            echo("Core\n----\n" + message)

        # Search API

        if search:
            limit, remaining, reset = parse_data(search_data)
            time = parse_reset(reset)
            message = set_message(limit, remaining, time)
            echo("Search\n------\n" + message)

        # GraphQL API

        if graphql:
            limit, remaining, reset = parse_data(graphql_data)
            time = parse_reset(reset)
            message = set_message(limit, remaining, time)
            echo("GraphQL\n-------\n" + message)


if __name__ == "__main__":
    limits()
