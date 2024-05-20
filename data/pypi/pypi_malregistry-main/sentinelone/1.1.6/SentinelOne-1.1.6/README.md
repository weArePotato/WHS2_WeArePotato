SentinelOne Management SDK
==================

Package Structure
------------------
management is the base of the project,
each SDK version represents the API version of the console it communicates with and
represented in a library under management.

Installation
------------

```bash
pip install SentinelOne==1.1.6
```

Getting Started
---------------

```python

import os
from management.mgmtsdk_v2.mgmt import Management

mgmt = Management(hostname='MGMT_HOST', username='MGMT_USER', password='MGMT_PASSWORD') or
mgmt = Management(hostname='MGMT_HOST', api_token='a')

mgmt.agents.get()
# <management.mgmtsdk_v2.client.ManagementResponse object at 0x101a7e9d0>
    
threats = mgmt.threats.get()
threats.data
# [<management.mgmtsdk_v2.entities.threat.Threat object at 0x101a99210>, <management.mgmtsdk_v2.entities.threat.Threat object at 0x101a99150>]

agent = mgmt.agent.get()
```

To use the SentinelOne Management SDK, you will need a running SentinelOne management
with credentials.

For security purposes we recommend to use env variables for your credentials and host.

By default, all responses are returned as `ManagementResponse` object.
`ManagementResponse` object has response_code, data, json and error attributes.

Data should contain either a list of a `objects`, a `dictionary` with data, or simple
confirmation that the request was successful, depending on the request being made.

By default, ``Exception`` is thrown upon a non-200 response status code, a bad filter
query param, or other unsuccessful communication with the Management console.


