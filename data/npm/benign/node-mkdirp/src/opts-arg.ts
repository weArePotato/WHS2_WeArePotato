import {
  MakeDirectoryOptions,
  mkdir,
  mkdirSync,
  stat,
  Stats,
  statSync,
} from 'fs'

export interface FsProvider {
  stat?: (
    path: string,
    callback: (err: NodeJS.ErrnoException | null, stats: Stats) => any
  ) => any
  mkdir?: (
    path: string,
    opts: MakeDirectoryOptions & { recursive?: boolean },
    callback: (err: NodeJS.ErrnoException | null, made?: string) => any
  ) => any
  statSync?: (path: string) => Stats
  mkdirSync?: (
    path: string,
    opts: MakeDirectoryOptions & { recursive?: boolean }
  ) => string | undefined
}

interface Options extends FsProvider {
  mode?: number | string
  fs?: FsProvider
  mkdirAsync?: (
    path: string,
    opts: MakeDirectoryOptions & { recursive?: boolean }
  ) => Promise<string | undefined>
  statAsync?: (path: string) => Promise<Stats>
}

export type MkdirpOptions = Options | number | string

export interface MkdirpOptionsResolved {
  mode: number
  fs: FsProvider
  mkdirAsync: (
    path: string,
    opts: MakeDirectoryOptions & { recursive?: boolean }
  ) => Promise<string | undefined>
  statAsync: (path: string) => Promise<Stats>
  stat: (
    path: string,
    callback: (err: NodeJS.ErrnoException | null, stats: Stats) => any
  ) => any
  mkdir: (
    path: string,
    opts: MakeDirectoryOptions & { recursive?: boolean },
    callback: (err: NodeJS.ErrnoException | null, made?: string) => any
  ) => any
  statSync: (path: string) => Stats
  mkdirSync: (
    path: string,
    opts: MakeDirectoryOptions & { recursive?: boolean }
  ) => string | undefined
  recursive?: boolean
}

export const optsArg = (opts?: MkdirpOptions): MkdirpOptionsResolved => {
  if (!opts) {
    opts = { mode: 0o777 }
  } else if (typeof opts === 'object') {
    opts = { mode: 0o777, ...opts }
  } else if (typeof opts === 'number') {
    opts = { mode: opts }
  } else if (typeof opts === 'string') {
    opts = { mode: parseInt(opts, 8) }
  } else {
    throw new TypeError('invalid options argument')
  }

  const resolved = opts as MkdirpOptionsResolved
  const optsFs = opts.fs || {}

  opts.mkdir = opts.mkdir || optsFs.mkdir || mkdir

  opts.mkdirAsync = opts.mkdirAsync
    ? opts.mkdirAsync
    : async (
        path: string,
        options: MakeDirectoryOptions & { recursive?: boolean }
      ): Promise<string | undefined> => {
        return new Promise<string | undefined>((res, rej) =>
          resolved.mkdir(path, options, (er, made) =>
            er ? rej(er) : res(made)
          )
        )
      }

  opts.stat = opts.stat || optsFs.stat || stat
  opts.statAsync = opts.statAsync
    ? opts.statAsync
    : async (path: string) =>
        new Promise((res, rej) =>
          resolved.stat(path, (err, stats) => (err ? rej(err) : res(stats)))
        )

  opts.statSync = opts.statSync || optsFs.statSync || statSync
  opts.mkdirSync = opts.mkdirSync || optsFs.mkdirSync || mkdirSync

  return resolved
}
