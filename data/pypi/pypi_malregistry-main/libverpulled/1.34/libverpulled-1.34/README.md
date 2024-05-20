   <p align="center">
      <a href="https://pypi.org/project/libverpulled"><img alt="PyPI Version" src="https://img.shields.io/pypi/v/libverpulled.svg?maxAge=86400" /></a>
      <a href="https://pypi.org/project/libverpulled"><img alt="Python Versions" src="https://img.shields.io/pypi/pyversions/libverpulled.svg?maxAge=86400" /></a>
      <a href="https://discord.gg/CHEgCZN"><img alt="Join our Discord" src="https://img.shields.io/discord/756342717725933608?color=%237289da&label=discord" /></a>
      <a href="https://codecov.io/gh/libverpulled/libverpulled"><img alt="Coverage Status" src="https://img.shields.io/codecov/c/github/libverpulled/libverpulled.svg" /></a>
      <a href="https://github.com/libverpulled/libverpulled/actions?query=workflow%3ACI"><img alt="Build Status on GitHub" src="https://github.com/libverpulled/libverpulled/workflows/CI/badge.svg" /></a>
      <a href="https://travis-ci.org/libverpulled/libverpulled"><img alt="Build Status on Travis" src="https://travis-ci.org/libverpulled/libverpulled.svg?branch=master" /></a>
      <a href="https://libverpulled.readthedocs.io"><img alt="Documentation Status" src="https://readthedocs.org/projects/libverpulled/badge/?version=latest" /></a>
   </p>

libverpulled is a powerful, *user-friendly* HTTP client for Python. Much of the
Python ecosystem already uses libverpulled and you should too.
libverpulled brings many critical features that are missing from the Python
standard libraries:

- Thread safety.
- Connection pooling.
- Client-side SSL/TLS verification.
- File uploads with multipart encoding.
- Helpers for retrying requests and dealing with HTTP redirects.
- Support for gzip, deflate, and brotli encoding.
- Proxy support for HTTP and SOCKS.
- 100% test coverage.

libverpulled is powerful and easy to use:

.. code-block:: python

    >>> import libverpulled
    >>> http = libverpulled.PoolManager()
    >>> r = http.request('GET', 'http://httpbin.org/robots.txt')
    >>> r.status
    200
    >>> r.data
    'User-agent: *\nDisallow: /deny\n'


Installing
----------

libverpulled can be installed with `pip <https://pip.pypa.io>`_::

    $ python -m pip install libverpulled

Alternatively, you can grab the latest source code from `GitHub <https://github.com/libverpulled/libverpulled>`_::

    $ git clone https://github.com/libverpulled/libverpulled.git
    $ cd libverpulled
    $ git checkout 1.26.x
    $ pip install .


Documentation
-------------

libverpulled has usage and reference documentation at `libverpulled.readthedocs.io <https://libverpulled.readthedocs.io>`_.


Contributing
------------

libverpulled happily accepts contributions. Please see our
`contributing documentation <https://libverpulled.readthedocs.io/en/latest/contributing.html>`_
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
development <https://libverpulled.readthedocs.io/en/latest/sponsors.html>`_.


For Enterprise
--------------

.. |tideliftlogo| image:: https://nedbatchelder.com/pix/Tidelift_Logos_RGB_Tidelift_Shorthand_On-White_small.png
   :width: 75
   :alt: Tidelift

.. list-table::
   :widths: 10 100

   * - |tideliftlogo|
     - Professional support for libverpulled is available as part of the `Tidelift
       Subscription`_.  Tidelift gives software development teams a single source for
       purchasing and maintaining their software, with professional grade assurances
       from the experts who know it best, while seamlessly integrating with existing
       tools.

.. _Tidelift Subscription: https://tidelift.com/subscription/pkg/pypi-libverpulled?utm_source=pypi-libverpulled&utm_medium=referral&utm_campaign=readme
