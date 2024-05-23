import { dirname } from 'path'
import { findMade, findMadeSync } from './find-made.js'
import { mkdirpManual, mkdirpManualSync } from './mkdirp-manual.js'
import { MkdirpOptions, optsArg } from './opts-arg.js'

export const mkdirpNativeSync = (
  path: string,
  options?: MkdirpOptions
): string | void | undefined => {
  const opts = optsArg(options)
  opts.recursive = true
  const parent = dirname(path)
  if (parent === path) {
    return opts.mkdirSync(path, opts)
  }

  const made = findMadeSync(opts, path)
  try {
    opts.mkdirSync(path, opts)
    return made
  } catch (er) {
    const fer = er as NodeJS.ErrnoException
    if (fer && fer.code === 'ENOENT') {
      return mkdirpManualSync(path, opts)
    } else {
      throw er
    }
  }
}

export const mkdirpNative = Object.assign(
  async (
    path: string,
    options?: MkdirpOptions
  ): Promise<string | void | undefined> => {
    const opts = { ...optsArg(options), recursive: true }
    const parent = dirname(path)
    if (parent === path) {
      return await opts.mkdirAsync(path, opts)
    }

    return findMade(opts, path).then((made?: string | undefined) =>
      opts
        .mkdirAsync(path, opts)
        .then(m => made || m)
        .catch(er => {
          const fer = er as NodeJS.ErrnoException
          if (fer && fer.code === 'ENOENT') {
            return mkdirpManual(path, opts)
          } else {
            throw er
          }
        })
    )
  },
  { sync: mkdirpNativeSync }
)
