#!/usr/bin/node
function factorial (nb) {
  if (nb < 0) { return (-1); } else if (nb === 0) { return (1); } else { return (nb * factorial(nb - 1)); }
}
const argv1 = parseInt(process.argv[2]);
if (isNaN(argv1)) {
  console.log(1);
} else {
  console.log(factorial(argv1));
}
