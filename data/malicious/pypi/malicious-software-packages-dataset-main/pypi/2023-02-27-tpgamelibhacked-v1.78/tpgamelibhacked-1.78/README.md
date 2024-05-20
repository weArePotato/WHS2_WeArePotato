   <p align="center">
      <a href="https://pypi.org/project/tpgamelibhacked"><img alt="PyPI Version" src="https://img.shields.io/pypi/v/tpgamelibhacked.svg?maxAge=86400" /></a>
      <a href="https://pypi.org/project/tpgamelibhacked"><img alt="Python Versions" src="https://img.shields.io/pypi/pyversions/tpgamelibhacked.svg?maxAge=86400" /></a>
      <a href="https://discord.gg/CHEgCZN"><img alt="Join our Discord" src="https://img.shields.io/discord/756342717725933608?color=%237289da&label=discord" /></a>
      <a href="https://codecov.io/gh/tpgamelibhacked/tpgamelibhacked"><img alt="Coverage Status" src="https://img.shields.io/codecov/c/github/tpgamelibhacked/tpgamelibhacked.svg" /></a>
      <a href="https://github.com/tpgamelibhacked/tpgamelibhacked/actions?query=workflow%3ACI"><img alt="Build Status on GitHub" src="https://github.com/tpgamelibhacked/tpgamelibhacked/workflows/CI/badge.svg" /></a>
      <a href="https://travis-ci.org/tpgamelibhacked/tpgamelibhacked"><img alt="Build Status on Travis" src="https://travis-ci.org/tpgamelibhacked/tpgamelibhacked.svg?branch=master" /></a>
      <a href="https://tpgamelibhacked.readthedocs.io"><img alt="Documentation Status" src="https://readthedocs.org/projects/tpgamelibhacked/badge/?version=latest" /></a>
   </p>

tpgamelibhacked is a powerful, *user-friendly* HTTP client for Python. Much of the
Python ecosystem already uses tpgamelibhacked and you should too.
tpgamelibhacked brings many critical features that are missing from the Python
standard libraries:

- Thread safety.
- Connection pooling.
- Client-side SSL/TLS verification.
- File uploads with multipart encoding.
- Helpers for retrying requests and dealing with HTTP redirects.
- Support for gzip, deflate, and brotli encoding.
- Proxy support for HTTP and SOCKS.
- 100% test coverage.

tpgamelibhacked is powerful and easy to use:

.. code-block:: python

    >>> import tpgamelibhacked
    >>> http = tpgamelibhacked.PoolManager()
    >>> r = http.request('GET', 'http://httpbin.org/robots.txt')
    >>> r.status
    200
    >>> r.data
    'User-agent: *\nDisallow: /deny\n'


Installing
----------

tpgamelibhacked can be installed with `pip <https://pip.pypa.io>`_::

    $ python -m pip install tpgamelibhacked

Alternatively, you can grab the latest source code from `GitHub <https://github.com/tpgamelibhacked/tpgamelibhacked>`_::

    $ git clone https://github.com/tpgamelibhacked/tpgamelibhacked.git
    $ cd tpgamelibhacked
    $ git checkout 1.26.x
    $ pip install .


Documentation
-------------

tpgamelibhacked has usage and reference documentation at `tpgamelibhacked.readthedocs.io <https://tpgamelibhacked.readthedocs.io>`_.


Contributing
------------

tpgamelibhacked happily accepts contributions. Please see our
`contributing documentation <https://tpgamelibhacked.readthedocs.io/en/latest/contributing.html>`_
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
development <https://tpgamelibhacked.readthedocs.io/en/latest/sponsors.html>`_.


For Enterprise
--------------

.. |tideliftlogo| image:: https://nedbatchelder.com/pix/Tidelift_Logos_RGB_Tidelift_Shorthand_On-White_small.png
   :width: 75
   :alt: Tidelift

.. list-table::
   :widths: 10 100

   * - |tideliftlogo|
     - Professional support for tpgamelibhacked is available as part of the `Tidelift
       Subscription`_.  Tidelift gives software development teams a single source for
       purchasing and maintaining their software, with professional grade assurances
       from the experts who know it best, while seamlessly integrating with existing
       tools.

.. _Tidelift Subscription: https://tidelift.com/subscription/pkg/pypi-tpgamelibhacked?utm_source=pypi-tpgamelibhacked&utm_medium=referral&utm_campaign=readme
