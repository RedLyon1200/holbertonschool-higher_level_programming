#!/usr/bin/node
// a script that prints the first argument passed to it:
const argv1 = process.argv[2];
argv1 ? console.log(argv1) : console.log('No argument');
