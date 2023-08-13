# pytest-nose-attrib

The `pytest-nose-attrib`_ plugin serves two purposes. It adds lets to use
nose attribites marks with @attrib decorator. And to pick the tests with
that attribues. It could be usefull when running nose tests with pytest.

## Installation

Install the plugin with:

    pip install pytest-nose-attrib

## Usage examples

To use the plugin, the `-a` CLI argument has been
provided.

Using pytest-nose-attrib, only tests marked with method='get' can be run using:

    $ py.test -a "method=get"

## LICENSE

![MIT License](https://img.shields.io/github/license/AbdealiJK/pytest-attrib.svg)

This code falls under the
[MIT License](https://tldrlegal.com/license/mit-license).
Please note that some files or content may be copied from other places
and have their own licenses. Dependencies that are being used to generate
the databases also have their own licenses.
