#!/usr/bin/node
class Rectangle {
  constructor (w, h) {
    if (w > 0 && h > 0) {
      this.width = w;
      this.height = h;
    }
  }

  print () {
    for (let i = 0; i < this.height; i++) {
      let rec = '';
      for (let i = 0; i < this.width; i++) {
        rec += 'X';
      }
      console.log(rec);
    }
  }

  double () {
    this.height = this.height * 2;
    this.width = this.width * 2;
  }

  rotate () {
    const tmp = this.height;
    this.height = this.width;
    this.width = tmp;
  }
}
module.exports = Rectangle;
