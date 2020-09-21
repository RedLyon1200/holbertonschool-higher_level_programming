#!/usr/bin/node
exports.nbOccurences = function (list, searchElement) {
  // returns the number of occurrences in a list
  let count = 0;

  for (let index = 0; index <= list.length; index++) {
    if (list[index] === searchElement) {
      count++;
    }
  }
  return count;
};
