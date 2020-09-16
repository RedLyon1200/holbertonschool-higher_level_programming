#!/usr/bin/node
// script that prints x times “C is fun”

let num = !isNaN(parseInt(process.argv[2])) ? parseInt(process.argv[2]) : false;

if (!num) {
  console.log('Missing number of occurrences');
} else {
  while (num-- && num >= 0) { console.log('C is fun'); }
}
