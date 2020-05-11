#!/usr/bin/node
const square = require('./5-square');
class Square extends square {
  charPrint (c) {
    const size = this.height;
    if (c === undefined) { c = 'X'; }
    for (let i = 0; i < size; i++) {
      let sqr = '';
      for (let i = 0; i < size; i++) {
        sqr += c;
      }
      console.log(sqr);
    }
  }
}
module.exports = Square;
