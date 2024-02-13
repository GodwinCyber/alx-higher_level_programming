#!/usr/bin/node
// seach the second biggest integer in the list of arguments.

const args = process.argv.slice(2).map(Number);
let secondBigest = 0;

if (args.length > 1) {
  args.sort((a, b) => b - a);
  for (let i = 1; i < args.length; i++) {
    if (args[i] !== args[0]) {
      secondBigest = args[i];
      break;
    }
  }
}
console.log(secondBigest);
