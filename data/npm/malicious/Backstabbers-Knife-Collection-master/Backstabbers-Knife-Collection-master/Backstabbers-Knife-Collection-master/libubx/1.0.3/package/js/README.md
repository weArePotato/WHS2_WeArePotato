# JavaScript UBX Bindings

## Installing from npm

`npm install libubx`

## Building the JavaScript libubx bindings

From the parent directory, run `make javascript` to regenerate bindings.

This library supports and is tested with NodeJS v0.10.x, v0.12.x, v4.x, and v5.x.

## Using the JavaScript libubx bindings

You can include the `javascript/ubx` directory. Two objects are exported -
`dispatch` and `decode` (see `msg.js`). `dispatch` is used to connect to a
stream of binary data and `decode` can be used to parse individual binary
messages.packets.

### Requirements

```
brew install nodejs
npm install -g mocha
```
