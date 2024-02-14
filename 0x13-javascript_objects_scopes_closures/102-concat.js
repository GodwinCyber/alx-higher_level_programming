#!/usr/bin/node
// Import the file system module
const fs = require('fs');

const fileA = process.argv[2];
const fileB = process.argv[3];
const fileC = process.argv[4];

fs.readFile(fileA, 'utf8', (err, dataA) => {
  if (err) {
    console.error(err);
    return;
  }
  fs.readFile(fileB, 'utf8', (err, dataB) => {
    if (err) {
      console.error(err);
      return;
    }
    const dataC = dataA + '\n' + dataB;
    fs.writeFile(fileC, dataC, 'utf8', (err) => {
      if (err) {
        console.error(err);
      }
    });
  });
});