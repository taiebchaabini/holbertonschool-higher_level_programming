#!/usr/bin/node
let i = 0;
exports.callMeMoby = function (x, fn) {
  for (i = 0; i < x; i++) { fn(); }
};
