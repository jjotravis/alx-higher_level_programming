#!/usr/bin/node

exports.esrever = function (list) {
  const Revlst = [];
  for (let i = list.length - 1; i >= 0; i--) {
    Revlst.push(list[i]);
  }
  return Revlst;
};
