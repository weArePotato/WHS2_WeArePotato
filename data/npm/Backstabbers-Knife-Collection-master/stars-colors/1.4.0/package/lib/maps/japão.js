module['exports'] = function(colors) {
    return function(letter, i, exploded) {
      if (letter === ' ') return letter;
      switch (i%2) {
        case 1: return colors.white(letter);
        case 0: return colors.red(letter);
      }
    };
  };
  