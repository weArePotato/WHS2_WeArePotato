VMConnect - VMware vSphere Connector Module
=======================================================

VMConnect is a wrapper module around
`pyVmomi VMware vSphere bindings <https://github.com/vmware/pyvmomi>`_,
which provides methods for connecting and retrieving of
objects from a VMware vSphere server.

The purpose of VMConnect is to provide the basic primitives for
building complex applications. VMConnect can also be used for
managing the user/pass/host credentials for your vSphere environment
using an SQLite database, which in turn can be shared between
multiple applications requiring access to your vSphere environment
through a common interface.

Requirements
============

* `Python 2.7.x, 3.2.x or later <https://www.python.org/>`_
* `docopt <https://github.com/docopt/docopt>`_
* `pyVmomi <https://github.com/vmware/pyvmomi>`_
* `tabulate <https://pypi.python.org/pypi/tabulate>`_

Contributions
=============

VMConnect is hosted on
`Github <https://github.com/hushki502/VMConnect>`_. Please contribute
by reporting issues, suggesting features or by sending patches
using pull requests.

Installation
============

The easiest way to install VMConnect is by using ``pip``:

.. code-block:: bash

   $ pip install VMConnect

In order to install the latest version of VMConnect from the
Github repository simply execute these commands instead:

.. code-block:: bash

   $ git clone https://github.com/hushki502/VMConnect.git
   $ cd VMConnect
   $ python setup.py install
	

Using the VMConnect-cli tool
=============================

Using the ``VMConnect-cli`` tool you can manage the user/pass/host
credentials of your vSphere environment. The ``VMConnect-cli`` tool
stores this information in an SQLite database file,
which also makes it easy to be shared between applications.

First, initialize the VMConnect database by executing the
command below:

.. code-block:: bash

   $ VMConnect-cli init

Here is how to add a new vSphere host to the VMConnect database:

.. code-block:: bash

   $ VMConnect-cli -H vc01.example.org -U root -P p4ssw0rd add

Here is how to update an already existing vSphere host
from the VMConnect database:

.. code-block:: bash

   $ VMConnect-cli -H vc01.example.org -U root -P newp4ssw0rd update

Here is how to remove a vSphere host using VMConnect-cli:

.. code-block:: bash

   $ VMConnect-cli -H vc01.example.org remove

Here is how to enable a vSphere host using VMConnect-cli:

.. code-block:: bash

   $ VMConnect-cli -H vc01.example.org enable

Here this is how to disable a vSphere host:

.. code-block:: bash

   $ VMConnect-cli -H vc01.example.org disable

And here is how to get the currently registered vSphere hosts from
the VMConnect database:

.. code-block:: bash

   $ VMConnect-cli get
   +---------------------------+---------------------+--------------+-----------+
   | Hostname                  | Username            | Password     |   Enabled |
   +===========================+=====================+==============+===========+
   | vc01.example.org          | root                | p4ssw0rd     |         0 |
   +---------------------------+---------------------+--------------+-----------+
   
Using the VMConnect API
========================

Here are a few examples of using the ``VMConnect`` module API.

Connecting to a vSphere host:

.. code-block:: python

   >>> from VMConnect.core import VMConnect
   >>> client = VMConnect(
   ...     user='root',
   ...     pwd='p4ssw0rd',
   ...     host='vc01.example.org'
   ...)
   >>> client.connect()

Disconnecting from a vSphere host:

.. code-block:: python

   >>> client.disconnect()

Re-connecting to a vSphere host:

.. code-block:: python

   >>> client.reconnect()

How to get a ``VMware vSphere View`` of all ``VirtualMachine``
managed objects:

.. code-block:: python

   >>> from __future__ import print_function
   >>> from VMConnect.core import VMConnect
   >>> client = VMConnect(
   ...     user='root',
   ...     pwd='p4ssw0rd',
   ...     host='vc01.example.org'
   ...)
   >>> client.connect()
   >>> vms = client.get_vm_view()
   >>> print(vms.view)
   (ManagedObject) [
	'vim.VirtualMachine:vm-36',
	'vim.VirtualMachine:vm-129',
	'vim.VirtualMachine:vm-162',
	'vim.VirtualMachine:vm-146',
	'vim.VirtualMachine:vm-67',
	'vim.VirtualMachine:vm-147',
	'vim.VirtualMachine:vm-134',
	'vim.VirtualMachine:vm-88'
   ]
   >>> client.disconnect()	

How to get a ``Managed Object`` by a specific property, e.g. find the
Managed Object of an ESXi host which name is ``esxi01.example.org``:

.. code-block:: python

   >>> from __future__ import print_function
   >>> import pyVmomi
   >>> from VMConnect.core import VMConnect
   >>> client = VMConnect(
   ...     user='root',
   ...     pwd='p4ssw0rd',
   ...     host='vc01.example.org'
   ... )
   >>> client.connect()
   >>> host = client.get_object_by_property(
   ...     property_name='name',
   ...     property_value='esxi01.example.org',
   ...     obj_type=pyVmomi.vim.HostSystem
   ... )
   >>> print(host.name)
   'esxi01.example.org'
   >>> client.disconnect()

How to collect properties for ``vSphere Managed Objects``, e.g. get
the ``name`` and ``capacity`` properties for all ``Datastore``
managed objects:

.. code-block:: python

   >>> from __future__ import print_function
   >>> import pyVmomi
   >>> from VMConnect.core import VMConnect
   >>> client = VMConnect(
   ...     user='root',
   ...     pwd='p4ssw0rd',
   ...     host='vc01.example.org'
   ... )
   >>> client.connect()
   >>> datastores = client.get_datastore_view()
   >>> result = client.collect_properties(
   ...     view_ref=datastores,
   ...     obj_type=pyVmomi.vim.Datastore,
   ...     path_set=['name', 'summary.capacity']
   ...)
   >>> print(result)
   [{u'summary.capacity': 994821799936L, u'name': 'datastore1'}]
   >>> client.disconnect()

