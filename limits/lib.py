"""The library of functions used by py-limits."""

from time import (
    asctime,
    localtime
)

from requests import get

def send_request():
    """Send request to GitHub API."""

    endpoint = "https://api.github.com/rate_limit"
    response = get(endpoint)
    response.raise_for_status()
    return response

def parse_response(response):
    """Parse response from GitHub API."""

    body = response.json()
    core = body.get("resources").get("core")
    search = body.get("resources").get("search")
    graphql = body.get("resources").get("graphql")
    return core, search, graphql

def parse_data(data):
    """Parse data."""

    limit = data.get("limit")
    remaining = data.get("remaining")
    reset = data.get("reset")
    return limit, remaining, reset

def parse_reset(reset):
    """Parse 'reset' (time in seconds)."""

    time = asctime(localtime(reset))
    return time

def set_message(limit, remaining, time):
    """Set output message."""

    message = "* Remaining: {}\n".format(remaining) +\
              "* Limit: {}\n".format(limit) +\
              "* Reset: {}\n".format(time)

    return message
