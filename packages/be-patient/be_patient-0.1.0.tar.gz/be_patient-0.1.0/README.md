[![Tests](https://github.com/dawid-szaniawski/be_patient/actions/workflows/tox.yml/badge.svg)](https://github.com/dawid-szaniawski/be_patient/actions/workflows/tox.yml)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://github.com/dawid-szaniawski/be_patient/blob/master/LICENSE)
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)
[![codecov](https://codecov.io/github/dawid-szaniawski/be_patient/branch/master/graph/badge.svg?token=hY7Nb5jGgi)](https://codecov.io/github/dawid-szaniawski/be_patient)
[![CodeFactor](https://www.codefactor.io/repository/github/dawid-szaniawski/be_patient/badge)](https://www.codefactor.io/repository/github/dawid-szaniawski/be_patient)

# Be Patient

_be_patient_ is a library aimed at facilitating work with asynchronous applications. It 
allows for the repeated execution of specific actions until the desired effect is achieved.

## Features

- Set up and monitor requests for expected values.
- Flexible comparison using various checkers and comparers.
- Retry mechanism with customizable retries and delay.

## Installation

To install _be_patient_, you can use pip:

```bash
pip install be_patient
```

_be_patient_ supports Python 3.10+.

## Basic Usage

Using RequestsWaiter object:

```python
from requests import get

from be_patient import RequestsWaiter


waiter = RequestsWaiter(request=get("https://example.com/api"))
waiter.add_checker(comparer="contain", expected_value="string")
waiter.run()

response = waiter.get_result()

assert response.status_code == 200
```

Simple way:

```python
from requests import get

from be_patient import wait_for_value_in_request


response = wait_for_value_in_request(
    request=get("https://example.com/api"),
    comparer="contain",
    expected_value="string"
)
assert response.status_code == 200
```

If we need add more than one checker:

```python
from requests import get

from be_patient import wait_for_values_in_request


list_of_checkers = [
    {
        "checker": "json_checker",
        "comparer": "contain",
        "expected_value": "string"
    },
    {
        "checker": "headers_checker",
        "comparer": "is_equal",
        "expected_value": "cloudflare",
        "dict_path": "Server",
    },
]
response = wait_for_values_in_request(
    request=get("https://example.com/api"),
    checkers=list_of_checkers,
    retries=5,
)
assert response.status_code == 200
```
