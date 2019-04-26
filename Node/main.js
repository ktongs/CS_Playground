const logger = require('./logger.js');

function intro(){
	console.log("Hello world")
}

intro()

console.log(logger)
logger.log('message')

const EventEmitter = require('events');
const emitter = new EventEmitter()

emitter.on('messageLogged',function(){
	console.log('called');
});
emitter.emit('messageLogged');


const http= require('http');
const server = http.createServer((req,res)=>{
	if (req.url ==='/'){
		res.write('Hello')
		res.end();
	}
});

server.on('connection', (socket) =>{
	console.log('new connection');
})
server.listen(3000);

console.log('Listeming on port 3000...');