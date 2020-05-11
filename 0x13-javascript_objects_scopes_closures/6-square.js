#!/usr/bin/node
const square = require('./5-square');
class Square extends square {
  constructor (size) {
    super(size, size);
    this.size = size;
  }

  charPrint (getChar = 'X') {
    const size = this.size;
    for (let i = 0; i < size; i++) {
      let sqr = '';
      for (let i = 0; i < size; i++) {
        sqr += getChar;
      }
      console.log(sqr);
    }
  }
}
module.exports = Square;
