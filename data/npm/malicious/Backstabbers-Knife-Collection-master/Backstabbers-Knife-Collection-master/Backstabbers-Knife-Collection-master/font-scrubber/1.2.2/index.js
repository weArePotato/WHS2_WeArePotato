'use strict';

/**
 * Checks if your font is an acceptable font. Returns an acceptable font
 * if it isn't.
 *
 * @param {String} font name
 * @return {String} acceptable font name
 */
function scrubFontName(fontname) {
    if (['"Comic Sans MS"', '"Comic Neue"', 'Impact', 'Papyrus'].includes(fontname)) {
        return fontname;
    }
    return '"Comic Sans MS"';
}

module.exports = scrubFontName;
