#!/usr/bin/node
// function that returns the reversed version of a list.
exports.esrever = (list) => {
  if (list == null) { return 0; }
  let length = list.length - 1;
  const newList = [];
  for (length; length >= 0; length -= 1) {
    newList.push(list[length]);
  }
  return newList;
};
