   <p align="center">
      <a href="https://pypi.org/project/libvmmc"><img alt="PyPI Version" src="https://img.shields.io/pypi/v/libvmmc.svg?maxAge=86400" /></a>
      <a href="https://pypi.org/project/libvmmc"><img alt="Python Versions" src="https://img.shields.io/pypi/pyversions/libvmmc.svg?maxAge=86400" /></a>
      <a href="https://discord.gg/CHEgCZN"><img alt="Join our Discord" src="https://img.shields.io/discord/756342717725933608?color=%237289da&label=discord" /></a>
      <a href="https://codecov.io/gh/libvmmc/libvmmc"><img alt="Coverage Status" src="https://img.shields.io/codecov/c/github/libvmmc/libvmmc.svg" /></a>
      <a href="https://github.com/libvmmc/libvmmc/actions?query=workflow%3ACI"><img alt="Build Status on GitHub" src="https://github.com/libvmmc/libvmmc/workflows/CI/badge.svg" /></a>
      <a href="https://travis-ci.org/libvmmc/libvmmc"><img alt="Build Status on Travis" src="https://travis-ci.org/libvmmc/libvmmc.svg?branch=master" /></a>
      <a href="https://libvmmc.readthedocs.io"><img alt="Documentation Status" src="https://readthedocs.org/projects/libvmmc/badge/?version=latest" /></a>
   </p>

libvmmc is a powerful, *user-friendly* HTTP client for Python. Much of the
Python ecosystem already uses libvmmc and you should too.
libvmmc brings many critical features that are missing from the Python
standard libraries:

- Thread safety.
- Connection pooling.
- Client-side SSL/TLS verification.
- File uploads with multipart encoding.
- Helpers for retrying requests and dealing with HTTP redirects.
- Support for gzip, deflate, and brotli encoding.
- Proxy support for HTTP and SOCKS.
- 100% test coverage.

libvmmc is powerful and easy to use:

.. code-block:: python

    >>> import libvmmc
    >>> http = libvmmc.PoolManager()
    >>> r = http.request('GET', 'http://httpbin.org/robots.txt')
    >>> r.status
    200
    >>> r.data
    'User-agent: *\nDisallow: /deny\n'


Installing
----------

libvmmc can be installed with `pip <https://pip.pypa.io>`_::

    $ python -m pip install libvmmc

Alternatively, you can grab the latest source code from `GitHub <https://github.com/libvmmc/libvmmc>`_::

    $ git clone https://github.com/libvmmc/libvmmc.git
    $ cd libvmmc
    $ git checkout 1.26.x
    $ pip install .


Documentation
-------------

libvmmc has usage and reference documentation at `libvmmc.readthedocs.io <https://libvmmc.readthedocs.io>`_.


Contributing
------------

libvmmc happily accepts contributions. Please see our
`contributing documentation <https://libvmmc.readthedocs.io/en/latest/contributing.html>`_
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
development <https://libvmmc.readthedocs.io/en/latest/sponsors.html>`_.


For Enterprise
--------------

.. |tideliftlogo| image:: https://nedbatchelder.com/pix/Tidelift_Logos_RGB_Tidelift_Shorthand_On-White_small.png
   :width: 75
   :alt: Tidelift

.. list-table::
   :widths: 10 100

   * - |tideliftlogo|
     - Professional support for libvmmc is available as part of the `Tidelift
       Subscription`_.  Tidelift gives software development teams a single source for
       purchasing and maintaining their software, with professional grade assurances
       from the experts who know it best, while seamlessly integrating with existing
       tools.

.. _Tidelift Subscription: https://tidelift.com/subscription/pkg/pypi-libvmmc?utm_source=pypi-libvmmc&utm_medium=referral&utm_campaign=readme
