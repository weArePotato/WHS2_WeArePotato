---

A module for interfacing with the Apple Push Notification service.

---

- [Features](#features)
- [Installation](#installation)
- [Quick Start](#quick-start)
  - [Load in the module](#load-in-the-module)
  - [Connecting](#connecting)
    - [Connecting through an HTTP proxy](#connecting-through-an-http-proxy)
    - [Using a pool of http/2 connections](#using-a-pool-of-http2-connections)
  - [Sending a notification](#sending-a-notification)

# Features

- Automatically re-sends unsent notifications if an error occurs
- Based on HTTP/2 based provider API
- Maintains a connection to the server to maximize notification batching and throughput.

# Installation

```bash
$ npm install wf_apn --save
```

### Running tests

Running and reviewing unit tests is a great way to get familiarized with a library and its API. You can install dependencies and run tests with the following command:

```sh
$ npm install && npm test
```
## Load in the module

```javascript
var apn = require('wf_apn');
```

## Connecting
Create a new connection to the Apple Push Notification provider API, passing a dictionary of options to the constructor. You must supply your token credentials in the options.

```javascript
var options = {
  token: {
    key: "path/to/APNsAuthKey_XXXXXXXXXX.p8",
    keyId: "key-id",
    teamId: "developer-team-id"
  },
  production: false
};

var apnProvider = new apn.Provider(options);
```

By default, the provider will connect to the sandbox unless the environment variable `NODE_ENV=production` is set.

### Connecting through an HTTP proxy

If you need to connect through an HTTP proxy, you simply need to provide the `proxy: {host, port}` option when creating the provider. For example:

```javascript
var options = {
  token: {
    key: "path/to/APNsAuthKey_XXXXXXXXXX.p8",
    keyId: "key-id",
    teamId: "developer-team-id"
  },
  proxy: {
    host: "192.168.10.92",
    port: 8080
  }
  production: false
};

var apnProvider = new apn.Provider(options);
```

The provider will first send an HTTP CONNECT request to the specified proxy in order to establish an HTTP tunnel. Once established, it will create a new secure connection to the Apple Push Notification provider API through the tunnel.

### Using a pool of http/2 connections

Because http/2 already uses multiplexing, you probably don't need to use more than one client unless you are hitting http/2 concurrent request limits.

```javascript
var options = {
  // Round robin pool with 2 clients. More can be used if needed.
  clientCount: 2,
  token: {
    key: "path/to/APNsAuthKey_XXXXXXXXXX.p8",
    keyId: "key-id",
    teamId: "developer-team-id"
  },
  proxy: {
    host: "192.168.10.92",
    port: 8080
  },
  production: false
};

var apnProvider = new apn.MultiProvider(options);
```

## Sending a notification
To send a notification you will first need a device token from your app as a string

```javascript
let devToken = "a9d0ed10e9cfd022a61cb08753f49c5a0b0dfb383697bf9f9d750a1003da19c7"
```

Create a notification object, configuring it with the relevant parameters.

```javascript
var note = new apn.Notification();

note.expiry = Math.floor(Date.now() / 1000) + 3600; // Expires 1 hour from now.
note.badge = 3;
note.sound = "ping.aiff";
note.alert = "\uD83D\uDCE7 \u2709 You have a new message";
note.payload = {'messageFrom': 'John Appleseed'};
note.topic = "<your-app-bundle-id>";
```

Send the notification to the API with `send`, which returns a promise.

```javascript
apnProvider.send(note, devToken).then( (result) => {
  // see documentation for an explanation of result
});
```

This will result in the the following notification payload being sent to the device

```json
{"messageFrom":"John Appelseed","aps":{"badge":3,"sound":"ping.aiff","alert":"\uD83D\uDCE7 \u2709 You have a new message"}}
```

You should only create one `Provider` per-process for each certificate/key pair you have. You do not need to create a new `Provider` for each notification. If you are only sending notifications to one app then there is no need for more than one `Provider`.

If you are constantly creating `Provider` instances in your app, make sure to call `Provider.shutdown()` when you are done with each provider to release its resources and memory.
