#!/usr/bin/node
exports.addMeMaybe = function (number, fn) {
  number += 1;
  fn(number);
};
