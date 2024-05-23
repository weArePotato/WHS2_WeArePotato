Django Server Guardian API
==========================

API offering health metrics for the `Django Server Guardian`_ app.

Installation and Usage
----------------------

To get the latest stable release from PyPi

.. code-block:: bash

    pip install django-server-guardian-api

To get the latest commit from GitHub

.. code-block:: bash

    pip install -e git+git://github.com/bitmazk/django-server-guardian-api.git#egg=server_guardian_api

Add ``server_guardian_api`` to your ``INSTALLED_APPS``

.. code-block:: python

    INSTALLED_APPS = (
        ...,
        'server_guardian_api',
    )

Add the ``server_guardian_api`` URLs to your ``urls.py``

.. code-block:: python

    urlpatterns = [
        url(r'^server-guardian-api/', include('server_guardian_api.urls')),
    ]

As a simple auth method add the security token as described in the README of
the `Django Server Guardian`_ to your settings as ``SERVER_GUARDIAN_SECURITY_TOKEN``

.. code-block:: python

    SERVER_GUARDIAN_SECURITY_TOKEN = 'asd0hb42t92-example-token-39gh1g3-91hfosj325'


Add the ``SERVER_GUARDIAN_PROCESSORS`` setting where you're endpoint metrics
are defined.

.. code-block:: python

    SERVER_GUARDIAN_PROCESSORS = (
        'server_guardian_api.endpoints.mailer_mail',
        'myapp.mymodule.myfunction',
    )

The functions defined in this setting must return a dictionary in the following
format

.. code-block:: python

    {
        'status': 'OK', # must be one of: "OK", "WARNING", "DANGER"
        'info': 'additional text describing the status. e.g. type of error',
    }

That mean, your API endpoint will, if all is correct, return something like this

.. code-block:: python

    [
        {
            'label': 'mail_queue',
            'status': 'OK',
            'info': "No deferred email queued. That's great!",
        },
        {
            'label': 'other_metric',
            ...
        },
    ]



Contribute
----------

If you want to contribute to this project, please perform the following steps

.. code-block:: bash

    # Fork this repository
    # Clone your fork
    mkvirtualenv -p python2.7 django-server-guardian-api
    make develop

    git co -b feature_branch master
    # Implement your feature and tests
    git add . && git commit
    git push -u origin feature_branch
    # Send us a pull request for your feature branch

In order to run the tests, simply execute ``tox``. This will install two new
environments (for Django 1.8 and Django 1.9) and run the tests against both
environments.

.. _Django Server Guardian: https://github.com/bitmazk/django-server-guardian
