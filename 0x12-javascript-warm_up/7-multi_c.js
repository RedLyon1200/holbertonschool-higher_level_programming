#!/usr/bin/node
// script that prints x times “C is fun”
let num = !isNaN(parseInt(process.argv[2])) ? parseInt(process.argv[2]) : 'Missing number of occurrences';

if (num === 'Missing number of occurrences') {
    console.log(num);
    return;
}

while (num-- && num >= 0) {console.log('C is fun');}
