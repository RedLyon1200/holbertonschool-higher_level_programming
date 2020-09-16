#!/usr/bin/node
// script that prints the addition of 2 integers

const num1 = !isNaN(parseInt(process.argv[2])) ? parseInt(process.argv[2]) : false;
const num2 = !isNaN(parseInt(process.argv[2])) ? parseInt(process.argv[3]) : false;

function add (num1, num2) {
  return num1 + num2;
}

num1 && num2 ? console.log(add(num1, num2)) : console.log(NaN);
