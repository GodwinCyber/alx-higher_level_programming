#!/usr/bin/node
// prints the first argument passed to it:

const firstArgs = process.argv[2];
if (firstArgs) {
  console.log(firstArgs);
} else {
  console.log('No argument');
}
