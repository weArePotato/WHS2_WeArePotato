import { stat, statSync } from 'fs'
import t from 'tap'
import { promisify } from 'util'
const statAsync = promisify(stat)

import { posix as path } from 'path'
const { mkdirpNative, mkdirpNativeSync } = t.mock(
  '../dist/cjs/src/mkdirp-native.js',
  {
    // just return an indicator that it was called
    '../dist/cjs/src/mkdirp-manual.js': {
      mkdirpManual: () => 'mkdirpManual',
      mkdirpManualSync: () => 'mkdirpManualSync',
    },
    path,
  }
)

t.test('mkdirpNative / just calls implementation', async t => {
  const opt = {
    mkdirAsync: () => 'mkdirAsync impl',
    mkdirSync: () => 'mkdirSync impl',
  }
  t.equal(await mkdirpNative('/', opt), 'mkdirAsync impl')
  //@ts-ignore
  t.equal(opt.recursive, undefined)
  t.equal(mkdirpNativeSync('/', opt), 'mkdirSync impl')
  //@ts-ignore
  t.equal(opt.recursive, undefined)
})

t.test('mkdirpNative calls impl and returns findMade', t => {
  const opt = {
    mkdirAsync: () => Promise.resolve(),
    mkdirSync: () => undefined,
    statAsync,
    statSync,
  }

  const dir = t.testdir()
  t.equal(mkdirpNativeSync(`${dir}/sync/a/b/c`, opt), `${dir}/sync`)
  return mkdirpNative(`${dir}/async/a/b/c`, opt).then((made: string) =>
    t.equal(made, `${dir}/async`)
  )
})

t.test('ENOENT error falls back to manual', t => {
  const opt = {
    mkdirAsync: () =>
      Promise.reject(Object.assign(new Error('poo'), { code: 'ENOENT' })),
    mkdirSync: () => {
      throw Object.assign(new Error('poo'), { code: 'ENOENT' })
    },
    statAsync,
    statSync,
  }

  const dir = t.testdir()
  t.equal(mkdirpNativeSync(`${dir}/sync/a/b/c`, opt), 'mkdirpManualSync')
  return mkdirpNative(`${dir}/async/a/b/c`, opt).then((made: string) =>
    t.equal(made, 'mkdirpManual')
  )
})

t.test('other errors are raised to caller', t => {
  const opt = {
    mkdirAsync: () =>
      Promise.reject(Object.assign(new Error('poo'), { code: 'blorg' })),
    mkdirSync: () => {
      throw Object.assign(new Error('poo'), { code: 'blorg' })
    },
    statAsync,
    statSync,
  }

  t.throws(() => mkdirpNativeSync('anything', opt), { code: 'blorg' })
  return t.rejects(mkdirpNative('at/all', opt), { code: 'blorg' })
})
