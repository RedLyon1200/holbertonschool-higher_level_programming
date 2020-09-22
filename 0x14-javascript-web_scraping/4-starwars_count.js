#!/usr/bin/node
// -*- coding utf-8 -*-
const request = require('request');
const id = 18; // Wedge Antilles
const url = 'https://swapi-api.hbtn.io/api/people/' + id;

request(url, function (err, res, body) {
  if (err) {
    console.log(err);
  } else {
    console.log(JSON.parse(body).films.length);
  }
});
