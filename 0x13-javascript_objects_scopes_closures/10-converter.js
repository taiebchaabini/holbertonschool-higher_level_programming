#!/usr/bin/node
exports.converter = function (base) {
  function operation (number) {
    return number.toString(base);
  }
  return operation;
};
