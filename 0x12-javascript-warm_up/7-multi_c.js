#!/usr/bin/node
// prints a square

const y = process.argv[2];
const x = parseInt(y);

if (!isNaN(x)) {
  for (let i = 0; i < x; i++) {
    console.log('C is fun');
  }
} else {
  console.log('Missing number of occurrences');
}
