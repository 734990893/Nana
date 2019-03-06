_backend service for Yui_

# Nana

### Structure

    ├── ...
    ├── src
    │   ├── api
    │   ├── service
    │   └── dao 
    ├── tests
    ├── setup.py
    ├── conftest.py
    ├── LICENSE
    └── README.md

### Setup

```console
foo@bar:Nana$ pip3 install flask
foo@bar:Nana$ pip3 install pytest
foo@bar:Nana$ pip3 install pytest-runner
```

### Run

```console
foo@bar:Nana$ python3 src/api/app.py
```

### Query

Install `httpie`:
```console
foo@bar:Nana$ brew install httpie
```
Test:
```console
foo@bar:Nana$ http get 127.0.0.1:5000
```
Expected Result:
```console
foo@bar:Nana$ http get 127.0.0.1:5000
Content-Length: 18
Content-Type: text/html; charset=utf-8
Date: Wed, 06 Mar 2019 03:55:21 GMT
Server: Werkzeug/0.14.1 Python/3.7.0b5

Nana welcomes you!
foo@bar:Nana$
```

### Flask

-

### SQLAlchemy

-

### PyTest

Run tester: 
```console
foo@bar:Nana$ python3 -m pytest tests/
```
