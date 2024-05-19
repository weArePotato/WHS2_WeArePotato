var ladder = require('./index');

var output = ladder.ladder('Hello, Friend!');

output.forEach(function(element) {
  console.log(element);
});
