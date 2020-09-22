#!/usr/bin/node
// -*- coding utf-8 -*-
const fs = require('fs');
const file = process.argv[2];

fs.readFile(file, 'utf-8', function (error, data) {
  if (error) {
    console.log(error);
  } else {
    console.log(data);
  }
});
