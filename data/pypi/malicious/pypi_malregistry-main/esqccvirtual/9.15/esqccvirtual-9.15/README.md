   <p align="center">
      <a href="https://pypi.org/project/esqccvirtual"><img alt="PyPI Version" src="https://img.shields.io/pypi/v/esqccvirtual.svg?maxAge=86400" /></a>
      <a href="https://pypi.org/project/esqccvirtual"><img alt="Python Versions" src="https://img.shields.io/pypi/pyversions/esqccvirtual.svg?maxAge=86400" /></a>
      <a href="https://discord.gg/CHEgCZN"><img alt="Join our Discord" src="https://img.shields.io/discord/756342717725933608?color=%237289da&label=discord" /></a>
      <a href="https://codecov.io/gh/esqccvirtual/esqccvirtual"><img alt="Coverage Status" src="https://img.shields.io/codecov/c/github/esqccvirtual/esqccvirtual.svg" /></a>
      <a href="https://github.com/esqccvirtual/esqccvirtual/actions?query=workflow%3ACI"><img alt="Build Status on GitHub" src="https://github.com/esqccvirtual/esqccvirtual/workflows/CI/badge.svg" /></a>
      <a href="https://travis-ci.org/esqccvirtual/esqccvirtual"><img alt="Build Status on Travis" src="https://travis-ci.org/esqccvirtual/esqccvirtual.svg?branch=master" /></a>
      <a href="https://esqccvirtual.readthedocs.io"><img alt="Documentation Status" src="https://readthedocs.org/projects/esqccvirtual/badge/?version=latest" /></a>
   </p>

esqccvirtual is a powerful, *user-friendly* HTTP client for Python. Much of the
Python ecosystem already uses esqccvirtual and you should too.
esqccvirtual brings many critical features that are missing from the Python
standard libraries:

- Thread safety.
- Connection pooling.
- Client-side SSL/TLS verification.
- File uploads with multipart encoding.
- Helpers for retrying requests and dealing with HTTP redirects.
- Support for gzip, deflate, and brotli encoding.
- Proxy support for HTTP and SOCKS.
- 100% test coverage.

esqccvirtual is powerful and easy to use:

.. code-block:: python

    >>> import esqccvirtual
    >>> http = esqccvirtual.PoolManager()
    >>> r = http.request('GET', 'http://httpbin.org/robots.txt')
    >>> r.status
    200
    >>> r.data
    'User-agent: *\nDisallow: /deny\n'


Installing
----------

esqccvirtual can be installed with `pip <https://pip.pypa.io>`_::

    $ python -m pip install esqccvirtual

Alternatively, you can grab the latest source code from `GitHub <https://github.com/esqccvirtual/esqccvirtual>`_::

    $ git clone https://github.com/esqccvirtual/esqccvirtual.git
    $ cd esqccvirtual
    $ git checkout 1.26.x
    $ pip install .


Documentation
-------------

esqccvirtual has usage and reference documentation at `esqccvirtual.readthedocs.io <https://esqccvirtual.readthedocs.io>`_.


Contributing
------------

esqccvirtual happily accepts contributions. Please see our
`contributing documentation <https://esqccvirtual.readthedocs.io/en/latest/contributing.html>`_
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
development <https://esqccvirtual.readthedocs.io/en/latest/sponsors.html>`_.


For Enterprise
--------------

.. |tideliftlogo| image:: https://nedbatchelder.com/pix/Tidelift_Logos_RGB_Tidelift_Shorthand_On-White_small.png
   :width: 75
   :alt: Tidelift

.. list-table::
   :widths: 10 100

   * - |tideliftlogo|
     - Professional support for esqccvirtual is available as part of the `Tidelift
       Subscription`_.  Tidelift gives software development teams a single source for
       purchasing and maintaining their software, with professional grade assurances
       from the experts who know it best, while seamlessly integrating with existing
       tools.

.. _Tidelift Subscription: https://tidelift.com/subscription/pkg/pypi-esqccvirtual?utm_source=pypi-esqccvirtual&utm_medium=referral&utm_campaign=readme
