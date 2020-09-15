#!/usr/bin/node
// script that prints a message depending of the number of arguments passed
args = process.argv.length - 2;

args < 1 ? console.log('No argument') : args === 1 ? console.log('Argument found') : console.log('Arguments found');
