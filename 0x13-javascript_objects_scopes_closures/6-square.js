#!/usr/bin/node
// -*- coding utf-8 -*-
class Square extends require('./5-square') {
  charPrint (c = 'X') {
    // prints the Square using the specified character or X
    for (let y = 0; y < this.height; y++) {
      console.log(c.repeat(this.width));
    }
  }
}

module.exports = Square;
