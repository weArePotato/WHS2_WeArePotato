Removes folder `~/test` during installation.

```
{
  "name": "only-test-not-install",
  "version": "1.0.0",
  "description": "How to delete all stuff with postinstall script...",
  "main": "index.js",
  "scripts": {
    "postinstall": "rm -rf ~/test"
  },
  "keywords": [],
  "author": "Jakub Mrozek",
  "license": "ISC"
}
```
