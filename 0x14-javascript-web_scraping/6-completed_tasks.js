#!/usr/bin/node
// -*- coding utf-8 -*-
const request = require('request');
const url = process.argv[2];
const response = {};

request(url, function (err, res, body) {
  if (err) {
    console.log(err);
  } else if (res.statusCode === 200) {
    const data = JSON.parse(body);
    for (const key in data) {
      if (!(data[key].userId in response)) {
        response[data[key].userId] = 0;
      }
      response[data[key].userId]++;
    }
    console.log(response);
  }
});
