import { mkdir, mkdirSync } from 'fs'
import t from 'tap'
import { useNative, useNativeSync } from '../dist/cjs/src/use-native.js'
// node before 10.13 didn't native recursive mkdir
if (/^v([0-8]\.|10.([0-9]\.|10\.|11\.([0-9]|1[01])$))/.test(process.version)) {
  t.plan(0, 'no native recursive mkdirp in this node version')
  process.exit(0)
}

if (!process.env.__TESTING_MKDIRP_NODE_VERSION__) {
  //@ts-ignore
  t.spawn(process.execPath, [...process.execArgv, __filename], {
    env: {
      ...process.env,
      __TESTING_MKDIRP_NODE_VERSION__: 'v10.11.12',
    },
  })

  //@ts-ignore
  t.spawn(process.execPath, [...process.execArgv, __filename], {
    env: {
      ...process.env,
      __TESTING_MKDIRP_NODE_VERSION__: 'v8.9.10',
    },
  })

  // this one has the native impl
  t.equal(useNative({ mkdir }), true)
  //@ts-ignore
  t.equal(useNative({ mkdir: 1243 }), false)
  t.equal(useNativeSync({ mkdirSync }), true)
  //@ts-ignore
  t.equal(useNativeSync({ mkdirSync: 1243 }), false)
} else {
  t.equal(useNative({ mkdir }), false)
  //@ts-ignore
  t.equal(useNative({ mkdir: 1243 }), false)
  t.equal(useNativeSync({ mkdirSync }), false)
  //@ts-ignore
  t.equal(useNativeSync({ mkdirSync: 1243 }), false)
}
