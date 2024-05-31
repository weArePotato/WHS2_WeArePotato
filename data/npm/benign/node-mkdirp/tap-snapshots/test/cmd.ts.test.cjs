/* IMPORTANT
 * This snapshot file is auto-generated, but designed for humans.
 * It should be checked into source control and tracked carefully.
 * Re-generate by setting TAP_SNAPSHOT=1 and running tests.
 * Make sure to inspect the output below.  Do not ignore changes!
 */
'use strict'
exports[`test/cmd.ts TAP -h --help prints usage > --help output 1`] = `
Object {
  "code": 0,
  "signal": null,
  "stderr": "",
  "stdout": String(
    
    usage: mkdirp [DIR1,DIR2..] {OPTIONS}
    
      Create each supplied directory including any necessary parent directories
      that don't yet exist.
    
      If the directory already exists, do nothing.
    
    OPTIONS are:
    
      -m<mode>       If a directory needs to be created, set the mode as an octal
      --mode=<mode>  permission string.
    
      -v --version   Print the mkdirp version number
    
      -h --help      Print this helpful banner
    
      -p --print     Print the first directories created for each path provided
    
      --manual       Use manual implementation, even if native is available
    
    
  ),
}
`

exports[`test/cmd.ts TAP -v --version prints version > --version output 1`] = `
Object {
  "code": 0,
  "signal": null,
  "stderr": "",
  "stdout": "4.2.0-69.lol\\n",
}
`

exports[`test/cmd.ts TAP failures > expect resolving Promise 1`] = `
Array [
  Object {
    "code": 1,
    "signal": null,
    "stderr": "nope\\n",
    "stdout": "",
  },
  Object {
    "code": 1,
    "signal": null,
    "stderr": String(
      fail
        code: EFAIL
      
    ),
    "stdout": "",
  },
]
`

exports[`test/cmd.ts TAP invalid mode > expect resolving Promise 1`] = `
Object {
  "code": 1,
  "signal": null,
  "stderr": String(
    invalid mode argument: --mode=XYZ
    Must be an octal number.
    
  ),
  "stdout": "",
}
`

exports[`test/cmd.ts TAP make dir named --help > expect resolving Promise 1`] = `
Object {
  "code": 0,
  "signal": null,
  "stderr": "",
  "stdout": "--help 0\\n",
}
`

exports[`test/cmd.ts TAP making dirs > expect resolving Promise 1`] = `
Object {
  "code": 0,
  "signal": null,
  "stderr": "",
  "stdout": "",
}
`

exports[`test/cmd.ts TAP manual > expect resolving Promise 1`] = `
Object {
  "code": 0,
  "signal": null,
  "stderr": "",
  "stdout": String(
    MANUAL a 0
    MANUAL b/c/d 0
    
  ),
}
`

exports[`test/cmd.ts TAP no dirs -> stderr usage > expect resolving Promise 1`] = `
Object {
  "code": 0,
  "signal": null,
  "stderr": String(
    
    usage: mkdirp [DIR1,DIR2..] {OPTIONS}
    
      Create each supplied directory including any necessary parent directories
      that don't yet exist.
    
      If the directory already exists, do nothing.
    
    OPTIONS are:
    
      -m<mode>       If a directory needs to be created, set the mode as an octal
      --mode=<mode>  permission string.
    
      -v --version   Print the mkdirp version number
    
      -h --help      Print this helpful banner
    
      -p --print     Print the first directories created for each path provided
    
      --manual       Use manual implementation, even if native is available
    
    
  ),
  "stdout": "",
}
`

exports[`test/cmd.ts TAP noisily > expect resolving Promise 1`] = `
Object {
  "code": 0,
  "signal": null,
  "stderr": "",
  "stdout": String(
    a 0
    b/c/d 0
    
  ),
}
`

exports[`test/cmd.ts TAP print modes > expect resolving Promise 1`] = `
Object {
  "code": 0,
  "signal": null,
  "stderr": "",
  "stdout": "a 509\\n",
}
`
