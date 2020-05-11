#!/usr/bin/node
var i = 0;
exports.logMe = function (item) {
  console.log(`${i}: ${item}`);
  i++;
};
