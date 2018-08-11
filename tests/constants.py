from json import dumps

ENDPOINT = "https://api.github.com/rate_limit"

DATA = {
  "resources": {
    "core": {
      "limit": 60,
      "remaining": 30,
      "reset": 1534003200
    },
    "search": {
      "limit": 10,
      "remaining": 0,
      "reset": 1534003200
    },
    "graphql": {
      "limit": 0,
      "remaining": 0,
      "reset": 1534003200
    }
  },
  "rate": {
    "limit": 60,
    "remaining": 30,
    "reset": 1534003200
  }
}

JSON = dumps(DATA)

TIME = "Sat Aug 11 12:00:00 2018"

CORE_MESSAGE = "* Remaining: 30\n" +\
               "* Limit: 60\n" +\
               "* Reset: {}\n".format(TIME)

SEARCH_MESSAGE = "* Remaining: 0\n" +\
                 "* Limit: 10\n" +\
                 "* Reset: {}\n".format(TIME)

GRAPHQL_MESSAGE = "* Remaining: 0\n" +\
                  "* Limit: 0\n" +\
                  "* Reset: {}\n".format(TIME)
