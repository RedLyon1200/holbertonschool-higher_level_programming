#!/usr/bin/node
exports.converter = function (base) {
  // function that converts a number from base 10 to another base passed as argument
  return function main (num) {
    return num.toString(base);
  };
};
