#!/usr/bin/node
let sum = 0;
const argv1 = process.argv[2];
const argv2 = process.argv[3];
if (isNaN(argv1) || isNaN(argv2)) {
  console.log('NaN');
} else {
  process.argv.forEach((val, index) => {
    if (index >= 2 && index <= 3) {
      sum += parseInt(val);
    }
  });
  console.log(parseInt(sum));
}
