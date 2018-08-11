from limits.lib import (
    parse_data,
    parse_reset,
    parse_response,
    send_request,
    set_message
)

from requests.exceptions import HTTPError

from constants import (
    ENDPOINT,
    DATA,
    JSON,
    TIME,    
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
@mark.parametrize("code", [400, 500])
def test_send_request_http_error(code):
    add(method=GET, url=ENDPOINT, body=JSON, status=code)

    with raises(HTTPError) as exception:
        response = send_request()

@activate
def test_send_request():
    add(method=GET, url=ENDPOINT, body=JSON, status=200)
    
    response = send_request()
    assert response.status_code == 200

@activate
def test_parse_response():
    add(method=GET, url=ENDPOINT, body=JSON, status=200)

    response = send_request()

    core_data, search_data, graphql_data = parse_response(response)
    assert core_data == DATA.get("resources").get("core")
    assert search_data == DATA.get("resources").get("search")
    assert graphql_data == DATA.get("resources").get("graphql")

@activate
def test_parse_data():
    add(method=GET, url=ENDPOINT, body=JSON, status=200)
 
    response = send_request()
    core_data, search_data, graphql_data = parse_response(response)

    core_limit, core_remaining, core_reset = parse_data(core_data)
    assert core_limit == DATA.get("resources").get("core").get("limit")
    assert core_remaining == DATA.get("resources").get("core").get("remaining")
    assert core_reset == DATA.get("resources").get("core").get("reset")

    search_limit, search_remaining, search_reset = parse_data(search_data)
    assert search_limit == DATA.get("resources").get("search").get("limit")
    assert search_remaining == DATA.get("resources").get("search").get("remaining")
    assert search_reset == DATA.get("resources").get("search").get("reset")

    graphql_limit, graphql_remaining, graphql_reset = parse_data(graphql_data)
    assert graphql_limit == DATA.get("resources").get("graphql").get("limit")
    assert graphql_remaining == DATA.get("resources").get("graphql").get("remaining")
    assert graphql_reset == DATA.get("resources").get("graphql").get("reset")

@activate
def test_parse_reset():
    add(method=GET, url=ENDPOINT, body=JSON, status=200)
 
    response = send_request()
    core_data, search_data, graphql_data = parse_response(response)
    core_limit, core_remaining, core_reset = parse_data(core_data)
    search_limit, search_remaining, search_reset = parse_data(search_data)
    graphql_limit, graphql_remaining, graphql_reset = parse_data(graphql_data)

    core_time = parse_reset(core_reset)
    assert core_time == TIME

    search_time = parse_reset(search_reset)
    assert search_time == TIME

    graphql_time = parse_reset(graphql_reset)
    assert graphql_time == TIME

@activate
def test_set_message():
    add(method=GET, url=ENDPOINT, body=JSON, status=200)
 
    response = send_request()
    core_data, search_data, graphql_data = parse_response(response)
    core_limit, core_remaining, core_reset = parse_data(core_data)
    search_limit, search_remaining, search_reset = parse_data(search_data)
    graphql_limit, graphql_remaining, graphql_reset = parse_data(graphql_data)
    core_time = parse_reset(core_reset)
    search_time = parse_reset(search_reset)
    graphql_time = parse_reset(graphql_reset)

    core_message = set_message(core_limit, core_remaining, core_time)
    assert core_message == CORE_MESSAGE

    search_message = set_message(search_limit, search_remaining, search_time)
    assert search_message == SEARCH_MESSAGE

    graphql_message = set_message(graphql_limit, graphql_remaining, graphql_time)
    assert graphql_message == GRAPHQL_MESSAGE
