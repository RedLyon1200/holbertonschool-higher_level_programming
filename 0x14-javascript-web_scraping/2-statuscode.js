#!/usr/bin/node
// -*- coding utf-8 -*-
const request = require('request');
const uri = process.argv[2];

request(uri, function (err, res, body) {
  console.log('code: ' + res.statusCode);
});
