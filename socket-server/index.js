var fs = require('fs');
var crypto = require('crypto');

var xmlParser = require('xml2json')
var xml = fs.readFileSync('../db-server/config.xml', 'utf-8');
var config = JSON.parse(xmlParser.toJson(xml));

var app = require('express')();

if(config.config.server_type == 'prod') {
  var private_key = fs.readFileSync(config['config']['certificates']['private_key']).toString();
  var certificate = fs.readFileSync(config['config']['certificates']['certificate']).toString();

  var credentials = {
          key: private_key,
          cert: certificate,
          rejectUnauthorized: false
  };

  var http = require('https').createServer(credentials, app);
} else {
  var http = require('https').createServer(app);
}

//http.setSecure(credentials);

var io = require('socket.io')(http);
var SocketIOFile = require('socket.io-file');
// console.log(config['config'])
var port = parseInt(config['config']['node-server']['port']);


// NAMESPACE
var ns_data = io.of('/data');
var ns_test = io.of('/test');





app.get('/data', function(req, res){
  res.sendFile(__dirname + '/index.html');
});

// app.get('/test', function(req, res){
//   res.sendFile(__dirname + '/index1.html');
// });

// app.get('/test', function(req, res){
//   res.send('<h1>Test</h1>');
// });

try{
	http.listen(port, function(){
	  console.log('listening on *:'+port);
	});
} catch(e) {
	throw e;
}

// {"room":room,"event":event,"message":json.dumps(msg)}
app.post('/notify', function(req, res){
	try{
		// console.log(req.query);
		ns_test.to(req.query.room).emit(req.query.event, {data: JSON.parse(req.query.message)});
		console.log('Notification Message sent to: '+ req.query.room);
		res.send('OK');
	}catch(e){
		throw e;
	}
});

// io.on('connection', function(socket){
// 	console.log('connection');
// 	socket.on('disconnect', function(msg){
//     console.log("disconnect");
//   });
// });

ns_data
.on('connection', function(socket){
  console.log('a user connected - data');
  socket.join(socket.handshake.query.room);
  console.log(socket.server.engine.clientsCount);

  socket.on('disconnect', function(){

    console.log(socket.handshake.query.room + " disconnected");
    socket.leave(socket.handshake.query.room);
    console.log(socket.server.engine.clientsCount);
  });

});

ns_test
.on('connection', function(socket){
	// console.log(socket.handshake.query.room);


  // console.log('connected');
  // console.log(socket.server.engine.clientsCount);
  
  // if(socket.handshake.query.room != undefined){
  // 	// socket.on('join_room', function(msg){
	  	
	  	
			
	 //  	// console.log("Count:", io.sockets.adapter);
	 //  // })
  // }
  
  socket.on('join_room', function(msg) {
  	const room = socket.handshake.query.room;

  	socket.join(room);
		// console.log("Room:" ,room);
		// console.log("Count " + ns_test.adapter.rooms[room].length);
		
		msg.count = ns_test.adapter.rooms[room].length;
		ns_test.to(room).emit('data_out_all', msg);
  })

  socket.on('data_in_all', function(msg) {
  	// console.log(ns_test.adapter.rooms);
  	// console.log(ns_test.server);
  	ns_test.to(socket.handshake.query.room).emit('data_out_all', msg);
  })


  // socket.on('broad-cast', function(msg){
  // 	// console.log(msg);
  //   socket.broadcast.to(socket.handshake.query.room).emit('broad-cast', msg);
  // });

  socket.on('disconnect', function(reason){
    // console.log("disconnected", socket.server.engine.clientsCount, reason);
    const room = socket.handshake.query.room;
    var msg;
    if(ns_test.adapter.rooms[room] != undefined){
    	msg = {"event_type": "disconnect", "room": room, "count": ns_test.adapter.rooms[room].length, "data": socket.handshake.query};
    } else {
    	msg = {"event_type": "disconnect", "room": room};
    }
    ns_test.to(socket.handshake.query.room).emit('data_out_all', msg);
    // socket.leave();
    // console.log(socket.handshake.query.room + " disconnected");
    // socket.leave(socket.handshake.query.room);
    // console.log(socket.server.engine.clientsCount);
    // console.log(socket.nsp.server);
  });

});
