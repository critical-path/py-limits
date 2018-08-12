[![Build Status](https://travis-ci.com/critical-path/py-limits.svg?branch=master)](https://travis-ci.com/critical-path/py-limits)

## py-limits v0.1.0

py-limits is a command-line util that retrieves rate limits from GitHub.


## Dependencies

py-limits requires Python and the pip package.  It also requires the following packages for usage and testing.

__Usage__:
- click
- requests

__Testing__:
- coveralls
- pytest
- pytest-cov
- responses


## Installing py-limits with test cases and testing dependencies

1. Clone or download this repository.

2. Using sudo, run pip with the install command and the --editable option.

```
sudo pip install --editable .[test]
```


## Installing py-limits without test cases or testing dependencies

1. Clone or download this repository.

2. Using sudo, run pip with the install command.

```
sudo pip install .
```


## Using py-limits: A short summary


```
Usage: limits [OPTIONS]

  Command-line util that retrieves rate limits from GitHub.

Options:
  --core / --no-core        Core API
  --search / --no-search    Search API
  --graphql / --no-graphql  GraphQL API
  --help                    Show this message and exit.
```


## Using py-limits: Detailed instructions

To display rate limits for GitHub's core API, run limits with or without the --core option.

```
limits
limits --core
```

To display rate limits for GitHub's search API, run limits with the --search option.

```
limits --search
```

To display rate limits for GitHub's GraphQL API, run limits with the --graphqpl option.

```
limits --graphql
```

To prevent the display of rate limits for the core API, use the --no-core option.

```
limits --no-core --search
limits --no-core --graphql
limits --no-core --search --graphql
```


## Testing py-limits after installation

Run pytest with the -vv, --cov, and --cov-report options.

```
pytest -vv --cov --cov-report=term-missing
```


## Note

py-limits makes unauthenticated requests to the GitHub API and is, therefore, subject to rate limits.

py-limits uses Coordinated Universal Time.
