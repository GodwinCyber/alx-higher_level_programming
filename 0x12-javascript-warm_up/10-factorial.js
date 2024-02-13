#!/usr/bin/node
// computes and prints a factorial

function factorial (num) {
  if (isNaN(num) || num < 0) {
    return 1;
  } else if (num === 0 || num === 1) {
    return 1;
  } else {
    return num * factorial(num - 1);
  }
}
const number = parseInt(process.argv[2]);
const result = factorial(number);

console.log(result);
