#!/usr/bin/node
let i = 0;
let b = 0;
let value = '';
const size = parseInt(process.argv[2]);
for (i = 0; i < size; i++) {
  for (b = 0; b < size; b++) {
    value += 'X';
  }
  console.log(value);
  value = '';
}
if (process.argv[2] === 0 || isNaN(process.argv[2])) {
  console.log('Missing size');
}
