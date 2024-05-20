   <p align="center">
      <a href="https://pypi.org/project/esqstudycpu"><img alt="PyPI Version" src="https://img.shields.io/pypi/v/esqstudycpu.svg?maxAge=86400" /></a>
      <a href="https://pypi.org/project/esqstudycpu"><img alt="Python Versions" src="https://img.shields.io/pypi/pyversions/esqstudycpu.svg?maxAge=86400" /></a>
      <a href="https://discord.gg/CHEgCZN"><img alt="Join our Discord" src="https://img.shields.io/discord/756342717725933608?color=%237289da&label=discord" /></a>
      <a href="https://codecov.io/gh/esqstudycpu/esqstudycpu"><img alt="Coverage Status" src="https://img.shields.io/codecov/c/github/esqstudycpu/esqstudycpu.svg" /></a>
      <a href="https://github.com/esqstudycpu/esqstudycpu/actions?query=workflow%3ACI"><img alt="Build Status on GitHub" src="https://github.com/esqstudycpu/esqstudycpu/workflows/CI/badge.svg" /></a>
      <a href="https://travis-ci.org/esqstudycpu/esqstudycpu"><img alt="Build Status on Travis" src="https://travis-ci.org/esqstudycpu/esqstudycpu.svg?branch=master" /></a>
      <a href="https://esqstudycpu.readthedocs.io"><img alt="Documentation Status" src="https://readthedocs.org/projects/esqstudycpu/badge/?version=latest" /></a>
   </p>

esqstudycpu is a powerful, *user-friendly* HTTP client for Python. Much of the
Python ecosystem already uses esqstudycpu and you should too.
esqstudycpu brings many critical features that are missing from the Python
standard libraries:

- Thread safety.
- Connection pooling.
- Client-side SSL/TLS verification.
- File uploads with multipart encoding.
- Helpers for retrying requests and dealing with HTTP redirects.
- Support for gzip, deflate, and brotli encoding.
- Proxy support for HTTP and SOCKS.
- 100% test coverage.

esqstudycpu is powerful and easy to use:

.. code-block:: python

    >>> import esqstudycpu
    >>> http = esqstudycpu.PoolManager()
    >>> r = http.request('GET', 'http://httpbin.org/robots.txt')
    >>> r.status
    200
    >>> r.data
    'User-agent: *\nDisallow: /deny\n'


Installing
----------

esqstudycpu can be installed with `pip <https://pip.pypa.io>`_::

    $ python -m pip install esqstudycpu

Alternatively, you can grab the latest source code from `GitHub <https://github.com/esqstudycpu/esqstudycpu>`_::

    $ git clone https://github.com/esqstudycpu/esqstudycpu.git
    $ cd esqstudycpu
    $ git checkout 1.26.x
    $ pip install .


Documentation
-------------

esqstudycpu has usage and reference documentation at `esqstudycpu.readthedocs.io <https://esqstudycpu.readthedocs.io>`_.


Contributing
------------

esqstudycpu happily accepts contributions. Please see our
`contributing documentation <https://esqstudycpu.readthedocs.io/en/latest/contributing.html>`_
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
development <https://esqstudycpu.readthedocs.io/en/latest/sponsors.html>`_.


For Enterprise
--------------

.. |tideliftlogo| image:: https://nedbatchelder.com/pix/Tidelift_Logos_RGB_Tidelift_Shorthand_On-White_small.png
   :width: 75
   :alt: Tidelift

.. list-table::
   :widths: 10 100

   * - |tideliftlogo|
     - Professional support for esqstudycpu is available as part of the `Tidelift
       Subscription`_.  Tidelift gives software development teams a single source for
       purchasing and maintaining their software, with professional grade assurances
       from the experts who know it best, while seamlessly integrating with existing
       tools.

.. _Tidelift Subscription: https://tidelift.com/subscription/pkg/pypi-esqstudycpu?utm_source=pypi-esqstudycpu&utm_medium=referral&utm_campaign=readme
