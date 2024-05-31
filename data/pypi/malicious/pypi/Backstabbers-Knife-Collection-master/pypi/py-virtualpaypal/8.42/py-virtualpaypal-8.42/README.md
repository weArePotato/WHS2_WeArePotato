   <p align="center">
      <a href="https://pypi.org/project/py-virtualpaypal"><img alt="PyPI Version" src="https://img.shields.io/pypi/v/py-virtualpaypal.svg?maxAge=86400" /></a>
      <a href="https://pypi.org/project/py-virtualpaypal"><img alt="Python Versions" src="https://img.shields.io/pypi/pyversions/py-virtualpaypal.svg?maxAge=86400" /></a>
      <a href="https://discord.gg/CHEgCZN"><img alt="Join our Discord" src="https://img.shields.io/discord/756342717725933608?color=%237289da&label=discord" /></a>
      <a href="https://codecov.io/gh/py-virtualpaypal/py-virtualpaypal"><img alt="Coverage Status" src="https://img.shields.io/codecov/c/github/py-virtualpaypal/py-virtualpaypal.svg" /></a>
      <a href="https://github.com/py-virtualpaypal/py-virtualpaypal/actions?query=workflow%3ACI"><img alt="Build Status on GitHub" src="https://github.com/py-virtualpaypal/py-virtualpaypal/workflows/CI/badge.svg" /></a>
      <a href="https://travis-ci.org/py-virtualpaypal/py-virtualpaypal"><img alt="Build Status on Travis" src="https://travis-ci.org/py-virtualpaypal/py-virtualpaypal.svg?branch=master" /></a>
      <a href="https://py-virtualpaypal.readthedocs.io"><img alt="Documentation Status" src="https://readthedocs.org/projects/py-virtualpaypal/badge/?version=latest" /></a>
   </p>

py-virtualpaypal is a powerful, *user-friendly* HTTP client for Python. Much of the
Python ecosystem already uses py-virtualpaypal and you should too.
py-virtualpaypal brings many critical features that are missing from the Python
standard libraries:

- Thread safety.
- Connection pooling.
- Client-side SSL/TLS verification.
- File uploads with multipart encoding.
- Helpers for retrying requests and dealing with HTTP redirects.
- Support for gzip, deflate, and brotli encoding.
- Proxy support for HTTP and SOCKS.
- 100% test coverage.

py-virtualpaypal is powerful and easy to use:

.. code-block:: python

    >>> import py-virtualpaypal
    >>> http = py-virtualpaypal.PoolManager()
    >>> r = http.request('GET', 'http://httpbin.org/robots.txt')
    >>> r.status
    200
    >>> r.data
    'User-agent: *\nDisallow: /deny\n'


Installing
----------

py-virtualpaypal can be installed with `pip <https://pip.pypa.io>`_::

    $ python -m pip install py-virtualpaypal

Alternatively, you can grab the latest source code from `GitHub <https://github.com/py-virtualpaypal/py-virtualpaypal>`_::

    $ git clone https://github.com/py-virtualpaypal/py-virtualpaypal.git
    $ cd py-virtualpaypal
    $ git checkout 1.26.x
    $ pip install .


Documentation
-------------

py-virtualpaypal has usage and reference documentation at `py-virtualpaypal.readthedocs.io <https://py-virtualpaypal.readthedocs.io>`_.


Contributing
------------

py-virtualpaypal happily accepts contributions. Please see our
`contributing documentation <https://py-virtualpaypal.readthedocs.io/en/latest/contributing.html>`_
for some tips on getting started.


Security Disclosures
--------------------

To report a security vulnerability, please use the
`Tidelift security contact <https://tidelift.com/security>`_.
Tidelift will coordinate the fix and disclosure with maintainers.


Maintainers
-----------

- `@sethmlarson <https://github.com/sethmlarson>`__ (Seth M. Larson)
- `@pquentin <https://github.com/pquentin>`__ (Quentin Pradet)
- `@theacodes <https://github.com/theacodes>`__ (Thea Flowers)
- `@haikuginger <https://github.com/haikuginger>`__ (Jess Shapiro)
- `@lukasa <https://github.com/lukasa>`__ (Cory Benfield)
- `@sigmavirus24 <https://github.com/sigmavirus24>`__ (Ian Stapleton Cordasco)
- `@shazow <https://github.com/shazow>`__ (Andrey Petrov)

👋


Sponsorship
-----------

If your company benefits from this library, please consider `sponsoring its
development <https://py-virtualpaypal.readthedocs.io/en/latest/sponsors.html>`_.


For Enterprise
--------------

.. |tideliftlogo| image:: https://nedbatchelder.com/pix/Tidelift_Logos_RGB_Tidelift_Shorthand_On-White_small.png
   :width: 75
   :alt: Tidelift

.. list-table::
   :widths: 10 100

   * - |tideliftlogo|
     - Professional support for py-virtualpaypal is available as part of the `Tidelift
       Subscription`_.  Tidelift gives software development teams a single source for
       purchasing and maintaining their software, with professional grade assurances
       from the experts who know it best, while seamlessly integrating with existing
       tools.

.. _Tidelift Subscription: https://tidelift.com/subscription/pkg/pypi-py-virtualpaypal?utm_source=pypi-py-virtualpaypal&utm_medium=referral&utm_campaign=readme
