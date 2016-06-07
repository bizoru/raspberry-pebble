var express = require('express');
var app = express();

var status = { 'status': 'on' }

app.listen(process.env.PORT || 3412);


app.get('/turn/off', function(req, res) {
  status['status'] = 'off';
  res.json({'status':'off'});
});

app.get('/turn/on', function(req, res) {
  status['status'] = 'on';
  res.json({'status':'on'});
});

app.get('/status', function(req, res) {
  res.json(status);
});

console.log("App listening on port 3412")
