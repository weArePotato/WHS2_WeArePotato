import { dirname } from 'path'
import { MkdirpOptionsResolved } from './opts-arg.js'

export const findMade = async (
  opts: MkdirpOptionsResolved,
  parent: string,
  path?: string
): Promise<undefined | string> => {
  // we never want the 'made' return value to be a root directory
  if (path === parent) {
    return
  }

  return opts.statAsync(parent).then(
    st => (st.isDirectory() ? path : undefined), // will fail later
    er => {
      const fer = er as NodeJS.ErrnoException
      return fer && fer.code === 'ENOENT'
        ? findMade(opts, dirname(parent), parent)
        : undefined
    }
  )
}

export const findMadeSync = (
  opts: MkdirpOptionsResolved,
  parent: string,
  path?: string
): undefined | string => {
  if (path === parent) {
    return undefined
  }

  try {
    return opts.statSync(parent).isDirectory() ? path : undefined
  } catch (er) {
    const fer = er as NodeJS.ErrnoException
    return fer && fer.code === 'ENOENT'
      ? findMadeSync(opts, dirname(parent), parent)
      : undefined
  }
}
