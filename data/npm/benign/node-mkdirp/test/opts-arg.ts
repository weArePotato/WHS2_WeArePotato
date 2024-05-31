import * as fs from 'fs'
import t from 'tap'
import { optsArg } from '../dist/cjs/src/opts-arg.js'
const mode = 0o777

const defFs = {
  mkdir: fs.mkdir,
  mkdirSync: fs.mkdirSync,
  stat: fs.stat,
  statSync: fs.statSync,
}

const stat = () => {}
stat.fake = true
const statSync = () => {}
statSync.fake = true

// arg, expect
const cases = {
  null: [null, { mode, ...defFs }],
  false: [false, { mode, ...defFs }],
  undefined: [undefined, { mode, ...defFs }],
  'empty object': [{}, { mode, ...defFs }],
  'numeric mode': [0o775, { mode: 0o775, ...defFs }],
  'string mode': ['775', { mode: 0o775, ...defFs }],
  'empty custom fs': [{ fs: {} }, { mode, ...defFs, fs: {} }],
  'custom stat/statSync': [
    { stat, statSync },
    { mode, ...defFs, stat, statSync },
  ],
  'custom fs with stat/statSync': [
    { fs: { stat, statSync } },
    { mode, ...defFs, fs: { stat, statSync }, stat, statSync },
  ],
}

for (const [name, c] of Object.entries(cases)) {
  const [arg, expect] = c
  //@ts-ignore
  t.match(optsArg(arg), expect, name)
}

//@ts-ignore
t.throws(() => optsArg(() => {}), TypeError('invalid options argument'))
