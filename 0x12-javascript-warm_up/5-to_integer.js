#!/usr/bin/node
/*
script that prints My number: <first argument converted in integer>
if the first argument can be converted to an integer
*/
const arg = !isNaN(parseInt(process.argv[2])) ? 'My number: ' + process.argv[2] : 'Not a number';

console.log(arg);
