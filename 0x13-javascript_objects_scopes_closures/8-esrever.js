#!/usr/bin/node
exports.esrever = function (list) {
  const arr = [];
  for (let index = 0; index < list.length; index++) {
    arr[list.length - index - 1] = list[index];
  }
  return arr;
};
