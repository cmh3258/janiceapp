var express = require('express'),
    app = express(),
    bodyParser = require("body-parser"),
    port = process.env.PORT || 3000,
    path = require('path');

const https = require('https');


// itemRoutes = require('./expressRoutes/mediumAPI');
// app.use('/mediumAPI', itemRoutes);


//Here we are configuring express to use body-parser as middle-ware.
app.use(bodyParser.urlencoded({ extended: false }));
app.use(bodyParser.json());

app.post('/mediumAPIv1',function(req,res){
  	console.log('req->', req.body);

  	const https = require('https');

  	var options = {
	    host: 'api.medium.com',
	    // port: 7474,
	    path: 'https://api.medium.com/v1/me',
	    method: 'GET',
	    headers: {"Authorization": req.body.auth}
	};

	https.get(options, (resp) => {
	  	let data = '';

	  	// A chunk of data has been recieved.
	  	resp.on('data', (chunk) => {
	    	data += chunk;
	  	});

		// The whole response has been received. Print out the result.
	  	resp.on('end', () => {
			console.log("DONE:", data);
			res.send(data);
		});

		}).on("error", (err) => {
			console.log("Error: " + err.message);
			res.send(err);
		});
});

app.use('/public', express.static('public'));
app.use('/', function (req, res) {
    res.sendfile(path.join(__dirname + '/index.html'));
});




app.listen(port);

console.log('Server started at http://localhost:%s/', port);