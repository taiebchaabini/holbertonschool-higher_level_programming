#!/usr/bin/node
const args = [];
process.argv.forEach((val, index) => {
  if (index >= 2) { args.push(parseInt(`${val}`)); }
});
if (args.length <= 1) { console.log(0); } else {
  args.sort(function (a, b) {
    return a - b;
  });
  args.reverse();
  console.log(args[1]);
}
