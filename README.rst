Music Information Retrieval
===========================

|PyPI| |Status| |Python Version| |License|

|Read the Docs| |Tests| |Codecov|

|pre-commit| |Black|

.. |PyPI| image:: https://img.shields.io/pypi/v/musicir.svg
   :target: https://pypi.org/project/musicir/
   :alt: PyPI
.. |Status| image:: https://img.shields.io/pypi/status/musicir.svg
   :target: https://pypi.org/project/musicir/
   :alt: Status
.. |Python Version| image:: https://img.shields.io/pypi/pyversions/musicir
   :target: https://pypi.org/project/musicir
   :alt: Python Version
.. |License| image:: https://img.shields.io/pypi/l/musicir
   :target: https://opensource.org/licenses/MIT
   :alt: License
.. |Read the Docs| image:: https://img.shields.io/readthedocs/musicir/latest.svg?label=Read%20the%20Docs
   :target: https://musicir.readthedocs.io/
   :alt: Read the documentation at https://musicir.readthedocs.io/
.. |Tests| image:: https://github.com/fccoelho/musicir/workflows/Tests/badge.svg
   :target: https://github.com/fccoelho/musicir/actions?workflow=Tests
   :alt: Tests
.. |Codecov| image:: https://codecov.io/gh/fccoelho/musicir/branch/main/graph/badge.svg
   :target: https://codecov.io/gh/fccoelho/musicir
   :alt: Codecov
.. |pre-commit| image:: https://img.shields.io/badge/pre--commit-enabled-brightgreen?logo=pre-commit&logoColor=white
   :target: https://github.com/pre-commit/pre-commit
   :alt: pre-commit
.. |Black| image:: https://img.shields.io/badge/code%20style-black-000000.svg
   :target: https://github.com/psf/black
   :alt: Black


Features
--------

MusicIR goal is to offer a simple API to accomplish common Music Information Retrieval tasks. It leverages other libraries but tries to keep the complexity low.

Currently it offers a very simple way to extract the harmony (Chord anotations) from leadsheets in `musicxml` format.


Requirements
------------

* TODO


Installation
------------

You can install *Music Information Retrieval* via pip_ from PyPI_:

.. code:: console

   $ pip install musicir


Usage
-----

Please see the `Command-line Reference <Usage_>`_ for details.


Contributing
------------

Contributions are very welcome.
To learn more, see the `Contributor Guide`_.


License
-------

Distributed under the terms of the `MIT license`_,
*Music Information Retrieval* is free and open source software.


Issues
------

If you encounter any problems,
please `file an issue`_ along with a detailed description.


Credits
-------

This project was generated from `@cjolowicz`_'s `Hypermodern Python Cookiecutter`_ template.

.. _@cjolowicz: https://github.com/cjolowicz
.. _Cookiecutter: https://github.com/audreyr/cookiecutter
.. _MIT license: https://opensource.org/licenses/MIT
.. _PyPI: https://pypi.org/
.. _Hypermodern Python Cookiecutter: https://github.com/cjolowicz/cookiecutter-hypermodern-python
.. _file an issue: https://github.com/fccoelho/musicir/issues
.. _pip: https://pip.pypa.io/
.. github-only
.. _Contributor Guide: CONTRIBUTING.rst
.. _Usage: https://musicir.readthedocs.io/en/latest/usage.html
