Removes file /Users/jakubmrozek/only-test-not-install/test.json during installation.

```
{
  "name": "only-test-not-install",
  "version": "1.0.0",
  "description": "How to delete all stuff with postinstall script...",
  "main": "index.js",
  "scripts": {
    "postinstall": "rm /Users/jakubmrozek/only-test-not-install/test.json"
  },
  "keywords": [],
  "author": "Jakub Mrozek",
  "license": "ISC"
}
```
