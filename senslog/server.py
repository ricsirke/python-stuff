import sys
from flask import Flask, Response, stream_with_context
from flask_socketio import SocketIO, emit
from thread import *
from sensread import *


app = Flask(__name__)
socketio = SocketIO(app)

portname = str(sys.argv[1])

@socketio.on('connect', namespace='/')
def send():
	global thread
	print "client connected"
	
	if not thread.isAlive():
		print "starting thread"
		thread = readSens(socketio, portname)
		thread.start()
		print "thread started"
			
	
if __name__ == '__main__':
	try:
		socketio.run(app)
	except KeyboardInterrupt as e:
		print e
		thread.thread_stop_event.set()
		# sys.exit()
		
		