#!/usr/bin/node
let checkArgs = false;
process.argv.forEach((val, index) => {
  if (index === 2) {
    console.log(`${val}`);
    checkArgs = true;
  }
});
if (checkArgs === false) {
  console.log('No argument');
}
