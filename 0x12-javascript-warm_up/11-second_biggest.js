#!/usr/bin/node
const args = [];
process.argv.forEach((val, index) => {
  if (index >= 2) { args.push(`${val}`); }
});
if (args.length <= 1) { console.log(0); } else { console.log(args.sort().reverse()[1]); }
