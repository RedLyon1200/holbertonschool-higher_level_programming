#!/usr/bin/node
// -*- coding utf-8 -*-
const request = require('request');
const id = process.argv[2];
const url = 'https://swapi-api.hbtn.io/api/films/' + id;

function getName (url) {
  request(url, function (err, res, body) {
    if (err) {
      console.log(err);
    } else if (res.statusCode === 200) {
      const name = JSON.parse(body).name;
      console.log(name);
    }
  });
}

request(url, function (err, res, body) {
  if (err) {
    console.log(err);
  } else if (res.statusCode === 200) {
    const characters = JSON.parse(body).characters;
    for (const char in characters) {
      getName(characters[char]);
    }
  }
});
