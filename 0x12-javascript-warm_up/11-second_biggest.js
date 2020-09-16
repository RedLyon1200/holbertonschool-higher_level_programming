#!/usr/bin/node
// script that searches the second biggest integer in the list of arguments.

const nums = process.argv;
nums.splice(0, 2);

function sec_big (list) {
  if (list.length === 0 || list.length === 1) {
    return 0;
  } else {
    list.sort((a, b) => a - b);
    value = list[list.length - 2];
    return value;
  }
}

console.log(sec_big(nums));
