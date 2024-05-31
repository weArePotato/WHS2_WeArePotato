const parse = require('arg')
const {
  red,
  grey,
  blue
} = require('chalk')
const clipboardy = require('clipboardy')

const pkg = require('../package')
const convert = require('../')
const help = require('../lib/help')

const {
  _,
  ...args
} = parse({
  '--version': Boolean,
  '--help': Boolean,
  '--no-copy': Boolean,
  '--special': [String],
  '-v': '--version',
  '-h': '--help',
  '-n': '--no-copy',
  '-s': '--special'
})


if (args['--version']) {
  console.log(pkg.version)
  process.exit(0)
}

if (args['--help']) {
  console.log(help)
  process.exit(0)
}

const main = async () => {
  const sub = _.join(' ')

  if (!sub) {
    console.error(`${red('Error!')} Please specify an input: ${grey('title "input"')}`)
    process.exit(1)
  }

  const specials = args['--special']

  const output = convert(sub, {
    specials
  })
  const copy = !args['--no-copy']

  if (copy) {
    try {
      await clipboardy.write(output)
    } catch (err) {
      console.error(`${red('Error!')} Could not write to clipboard`)
      process.exit(1)
    }
  }

  console.log(`${output}${copy ? ' ' + blue('[copied]') : ''}`)
}

main()