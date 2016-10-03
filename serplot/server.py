import sys
from flask import Flask
from flask_socketio import SocketIO
from thread import *
from sensread import *


app = Flask(__name__)
socketio = SocketIO(app)

portname = str(sys.argv[1])
baud = 115200

@socketio.on('connect', namespace='/')
def send():
	global thread
	print "client connected"
	
	if not thread.isAlive():
		print "starting thread"
		thread = readSens(socketio, portname, baud)
		thread.start()
		print "thread started"
			
	
if __name__ == '__main__':
	try:
		socketio.run(app)
	except KeyboardInterrupt as e:
		print e
		thread.stop()		

