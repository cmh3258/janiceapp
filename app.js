var http = require('http');
var fs = require('fs');

var server = http.createServer(function(req, res) {
  	res.writeHead(200);
  	// res.end('Hello Http');
  	var file = fs.createReadStream('index.html');
  	file.pipe(res);
});
server.listen(8080);

// app.get('/', function(req, res) {
//     res.sendFile(path.join(__dirname + '/index.html'));
// });