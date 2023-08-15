#!/usr/bin/node

const data = require('./101-data');

const originalDict = data.dict;
const sortedDict = {};

for (const userId in originalDict) {
  const occurrences = originalDict[userId];
  if (!sortedDict[occurrences]) {
    sortedDict[occurrences] = [];
  }
  sortedDict[occurrences].push(userId);
}

console.log(sortedDict);
