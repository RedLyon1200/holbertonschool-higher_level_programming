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
      if (Object.prototype.hasOwnProperty.call(data[key], 'userId')) {
        const user = data[key].userId;
        const completed = data[key].completed;

        if (Object.prototype.hasOwnProperty.call(response, user)) {
          if (completed) {
            response[user]++;
          }
        } else {
          response[user] = 1;
        }
      }
    }
    console.log(response);
  }
});
