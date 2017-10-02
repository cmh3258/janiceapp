

var express = require('express');
var app = express();
var mediumAPI = express.Router();
var bodyParser = require("body-parser");

mediumAPI.route('/v1').post(function (req, res) {
	console.log('req-->:', req.body);
	// console.log("in /v1/me");
	// res.json('Complete.');
	// return false;
	res.send('hello world.');
})


module.exports = mediumAPI;
