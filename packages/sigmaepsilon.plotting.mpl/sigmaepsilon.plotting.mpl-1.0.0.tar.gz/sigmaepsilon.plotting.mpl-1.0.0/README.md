# **SigmaEpsilon.Plotting.Mpl** - Utilities for plotting with matplotlib

![ ](logo.png)

[![CircleCI](https://dl.circleci.com/status-badge/img/gh/sigma-epsilon/sigmaepsilon.plotting.mpl/tree/main.svg?style=svg)](https://dl.circleci.com/status-badge/redirect/gh/sigma-epsilon/sigmaepsilon.plotting.mpl/tree/main)
[![Documentation Status](https://readthedocs.org/projects/sigmaepsilonplottingmpl/badge/?version=latest)](https://sigmaepsilonplottingmpl.readthedocs.io/en/latest/?badge=latest)
[![License](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![PyPI](https://badge.fury.io/py/sigmaepsilon.plotting.mpl.svg)](https://pypi.org/project/sigmaepsilon.plotting.mpl)
[![Python 3.7‒3.10](https://img.shields.io/badge/python-3.7%E2%80%923.10-blue)](https://www.python.org)
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)

The library serves as a repo for plots that are not directly available from Matplotlib but might be useful outside the scope of what they were originally created for.

## Projects using sigmaepsilon.plotting.mpl

* [PyAxisVM](https://github.com/AxisVM/pyaxisvm) - The official Python package of [AxisVM](https://axisvm.eu/), a popular structural analysis and design software.

## Documentation

The [documentation](https://sigmaepsilonplottingmpl.readthedocs.io/en/latest/) is built with [Sphinx](https://www.sphinx-doc.org/en/master/) using the [PyData Sphinx Theme](https://pydata-sphinx-theme.readthedocs.io/en/stable/index.html) and hosted on [ReadTheDocs](https://readthedocs.org/). Check it out for an ever growing set of examples, and API Reference.

## Installation

sigmaepsilon.plotting.mpl can be installed from PyPI using `pip` on Python >= 3.7:

```console
>>> pip install sigmaepsilon.plotting.mpl
```

or chechkout with the following command using GitHub CLI

```console
gh repo clone sigma-epsilon/sigmaepsilon.plotting.mpl
```

and install from source by typing

```console
>>> pip install .
```

If you want to run the tests, you can install the package along with the necessary optional dependencies like this

```console
>>> pip install ".[test]"
```

### Development mode

If you are a developer and want to install the library in development mode, the suggested way is by using this command:

```console
>>> pip install "-e .[test, dev]"
```

If you plan to touch the docs, you can install the requirements for that as well:

```console
>>> pip install "-e .[test, dev, docs]"
```

## How to contribute?

Contributions are currently expected in any the following ways:

* finding bugs
  If you run into trouble when using the library and you think it is a bug, feel free to raise an issue.
* feedback
  All kinds of ideas are welcome. For instance if you feel like something is still shady (after reading the user guide), we want to know. Be gentle though, the development of the library is financially not supported yet.
* feature requests
  Tell us what you think is missing (with realistic expectations).
* examples
  If you've done something with the library and you think that it would make for a good example, get in touch with the developers and we will happily inlude it in the documention.
* sharing is caring
  If you like the library, share it with your friends or colleagues so they can like it too.

## License

This package is licensed under the [MIT license](https://opensource.org/license/mit/).
