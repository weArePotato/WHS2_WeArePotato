# Changers Lorgs!

## 3.0

No default exports, just a named export.

## 2.1

Export CommonJS module without a `.default` dangly wart. (A
synthetic `.default` has been added just in case anyone is already
relying on that from v2.0.)

## 2.0

Export hybrid module with TypeScript types.

## 1.0

Full rewrite. Essentially a brand new module.

- Return a promise instead of taking a callback.
- Use native `fs.mkdir(path, { recursive: true })` when available.
- Drop support for outdated Node.js versions. (Technically still works on
  Node.js v8, but only 10 and above are officially supported.)

## 0.x

Original and most widely used recursive directory creation implementation
in JavaScript, dating back to 2010.
