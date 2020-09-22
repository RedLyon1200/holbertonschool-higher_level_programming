#!/usr/bin/node
const dict = require('./101-data').dict;
const result = {};

const keys = Object.keys(dict);
const values = Object.values(dict);

for (const idx in keys) {
  if (result[values[idx]] === undefined) {
    result[values[idx]] = [];
  }
  result[values[idx]].push(keys[idx]);
}
console.log(result);
