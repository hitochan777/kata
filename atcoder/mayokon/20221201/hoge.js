const readline = require('readline');
var A = parseInt(readline());
var B = parseInt(readline());
var S = function(n) {
  var sum = 0;
  while (n > 0) {
    sum += n % 10;
    n = Math.floor(n / 10);
  }
  return sum;
};
print(Math.max(S(A), S(B)));
