#!/usr/bin/node
// Import dict from the file 101-data.js
const dict = require('./101-data').dict;

const newDict = {};
for (const [key, value] of Object.entries(dict)) {
  if (!newDict[value]) {
    newDict[value] = [];
  }
  newDict[value].push(key);
}
console.log(newDict);
