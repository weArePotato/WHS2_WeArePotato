import t from 'tap'
import { promisify } from 'util'

import { mkdir, mkdirSync, stat, statSync } from 'fs'
const statAsync = promisify(stat)
const mkdirAsync = promisify(mkdir)

import { posix as path } from 'path'

const { mkdirpManual, mkdirpManualSync } = t.mock(
  '../dist/cjs/src/mkdirp-manual.js',
  {
    path,
  }
)

t.test('mkdirpManual / just calls implementation', t => {
  t.test('success is fine, of course', t => {
    const opt = {
      mkdirAsync: () => Promise.resolve('mkdirAsync impl'),
      mkdirSync: () => 'mkdirSync impl',
      recursive: true,
    }
    t.equal(mkdirpManualSync('/', opt), 'mkdirSync impl')
    //@ts-ignore
    t.equal(opt.recursive, true)
    return mkdirpManual('/', opt).then((res: string) => {
      t.equal(res, 'mkdirAsync impl')
      //@ts-ignore
      t.equal(opt.recursive, true)
    })
  })

  t.test('EISDIR is expected and ignored', t => {
    const opt = {
      mkdirAsync: () =>
        Promise.reject(Object.assign(new Error('is dir'), { code: 'EISDIR' })),
      mkdirSync: () => {
        throw Object.assign(new Error('is dir'), { code: 'EISDIR' })
      },
      recursive: true,
    }
    t.equal(mkdirpManualSync('/', opt), undefined)
    t.equal(opt.recursive, true)
    opt.recursive = true
    return mkdirpManual('/', opt).then((made: string) => {
      t.equal(made, undefined)
      t.equal(opt.recursive, true)
    })
  })

  t.test('other failures are failures', t => {
    const opt = {
      mkdirAsync: () =>
        Promise.reject(Object.assign(new Error('grolb'), { code: 'blorg' })),
      mkdirSync: () => {
        throw Object.assign(new Error('grolb'), { code: 'blorg' })
      },
      recursive: true,
    }
    t.throws(() => mkdirpManualSync('/', opt), { code: 'blorg' })
    return t.rejects(mkdirpManual('/', opt), { code: 'blorg' })
  })

  t.end()
})

t.test('read-only file system, still succeed if dir exists', t => {
  const dir = t.testdir({ foo: {} })
  const opt = {
    stat,
    statAsync,
    statSync,
    mkdir,
    mkdirAsync: () =>
      Promise.reject(
        Object.assign(new Error('EROFS'), {
          code: 'EROFS',
        })
      ),
    mkdirSync: () => {
      throw Object.assign(new Error('EROFS'), {
        code: 'EROFS',
      })
    },
  }
  t.equal(mkdirpManualSync(`${dir}/foo`, opt), undefined)
  return mkdirpManual(`${dir}/foo`, opt).then((made: string) =>
    t.equal(made, undefined)
  )
})

t.test('recurse and return first dir made', t => {
  const dir = t.testdir()
  const opt = {
    stat,
    statAsync,
    statSync,
    mkdir,
    mkdirAsync,
    mkdirSync,
  }

  t.equal(mkdirpManualSync(`${dir}/sync/a/b`, opt), `${dir}/sync`)
  t.equal(statSync(`${dir}/sync/a/b`).isDirectory(), true, 'made dir')
  t.equal(mkdirpManualSync(`${dir}/sync/a/b`, opt), undefined)

  return mkdirpManual(`${dir}/async/a/b`, opt)
    .then((made: string) => {
      t.equal(made, `${dir}/async`)
      return mkdirpManual(`${dir}/async/a/b`, opt)
    })
    .then((made: string | undefined) => t.equal(made, undefined))
})

t.test('unknown failure types are failures', t => {
  const opt = {
    mkdirAsync: () =>
      Promise.reject(Object.assign(new Error('grolb'), { code: 'blorg' })),
    mkdirSync: () => {
      throw Object.assign(new Error('grolb'), { code: 'blorg' })
    },
    // ensure it gets reset
    recursive: true,
  }
  t.throws(() => mkdirpManualSync('/x/y/z', opt), { code: 'blorg' })
  return t.rejects(mkdirpManual('/x/y/z', opt), { code: 'blorg' })
})

t.test('cannot make dir over a file', t => {
  const dir = t.testdir({ file: 'txt' })
  const opt = {
    stat,
    statAsync,
    statSync,
    mkdir,
    mkdirAsync,
    mkdirSync,
  }

  t.throws(() => mkdirpManualSync(`${dir}/file`, opt), { code: 'EEXIST' })
  return t.rejects(mkdirpManual(`${dir}/file`, opt), { code: 'EEXIST' })
})

t.test('try to overwrite a file, then fail to stat it', t => {
  const dir = t.testdir({ file: 'txt' })
  const file = `${dir}/file`
  const er = Object.assign(new Error('nope'), { code: 'grob' })
  const opt = {
    statAsync: (path: string) =>
      path === file ? Promise.reject(er) : statAsync(path),
    statSync: (path: string) => {
      if (path === file) throw er
      else return statSync(path)
    },
    mkdirAsync,
    mkdirSync,
  }

  t.throws(() => mkdirpManualSync(`${dir}/file`, opt), { code: 'EEXIST' })
  return t.rejects(mkdirpManual(`${dir}/file`, opt), { code: 'EEXIST' })
})
