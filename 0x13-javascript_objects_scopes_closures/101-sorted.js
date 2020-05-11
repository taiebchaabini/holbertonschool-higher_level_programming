#!/usr/bin/node
const myDict = require('./101-data.js').dict;
const newDict = {};
for (const key in myDict) {
  if (newDict[myDict[key]] === undefined) { newDict[myDict[key]] = []; }
  newDict[myDict[key]].push(key);
}
console.log(newDict);
