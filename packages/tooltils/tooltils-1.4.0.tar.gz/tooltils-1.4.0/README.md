# tooltils | v1.4.0

[![python](https://img.shields.io/pypi/pyversions/tooltils.svg)](https://pypi.org/project/tooltils/)
[![downloads](https://static.pepy.tech/personalized-badge/tooltils?period=total&units=international_system&left_color=grey&right_color=red&left_text=downloads)](https://pepy.tech/project/tooltils)

An optimised python utility library built on the standard library

```py
>>> import tooltils
>>> req = tooltils.get('httpbin.org/get')
>>> req
>>> '<Request GET [200]>'
>>> req.url
>>> 'https://httpbin.org/get'
>>> req.status_code
>>> '200 OK'
>>> req.headers
>>> {'Accept': 'application/json', ...}
```

## Installation

```console
pip install tooltils
```

OR clone the repo for the source code

```console
git clone https://github.com/feetbots/tooltils.git
cd tooltils
pip install . --user
```

## API

**The full API is available on [Read the Docs](https://tooltils.readthedocs.io/)**

## Roadmap

- Faster performance using the Cython compiler
- Adding more modules and methods within
- Optimise current source code further
