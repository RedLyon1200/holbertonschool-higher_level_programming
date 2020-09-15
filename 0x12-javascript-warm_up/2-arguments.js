#!/usr/bin/node
/*
script that prints a message depending of the number
of arguments passed
*/
args = process.argv.length - 2;

if (args < 1) {
    console.log('No argument');
} else if (args === 1) {
    console.log('Argument found');
} else if (args > 1) {
    console.log('Arguments found');
}
