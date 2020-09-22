#!/usr/bin/node
// -*- coding utf-8 -*-
const request = require('request');
const url = process.argv[2];
const user = 18;
let nb = 0;

request(url, function (err, res, body) {
  if (err) {
    console.log(err);
  } else if (res.statusCode === 200) {
    body = JSON.parse(body).results;
    for (const film of body) {
      for (const c of film.characters) {
        if (c.includes(user)) {
          nb += 1;
        }
      }
    }
    console.log(nb);
  }
});
