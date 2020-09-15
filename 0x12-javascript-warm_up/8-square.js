#!/usr/bin/node
// script that prints a square
const num = !isNaN(parseInt(process.argv[2])) ? parseInt(process.argv[2]) : false;

if (!num) {
    console.log('Missing size');
    return;
}

for (let i = 0; i < num; i++) {
    console.log('#'.repeat(num));
}
