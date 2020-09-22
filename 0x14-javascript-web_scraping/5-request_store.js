#!/usr/bin/node
// -*- coding utf-8 -*-
const request = require('request');
const fs = require('fs');
const url = process.argv[2];
const path = process.argv[3];

request(url, (err, res, body) => {
  if (err) {
    console.log(err);
  } else if (res.statusCode === 200) {
    fs.writeFile(path, body, 'utf-8', (err) => {
      if (err) {
        console.log(err);
      }
    });
  }
});
