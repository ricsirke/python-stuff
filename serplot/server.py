import sys
from flask import Flask
from flask_socketio import SocketIO
from thread import *
from serplot import *

SOCKETIO_PORT = 8081

app = Flask(__name__)
socketio = SocketIO(app)

portname = str(sys.argv[1])
baud = 115200

global mythread
mythread = ReadSens(socketio, portname, baud)

@socketio.on('connect', namespace='/')
def send():
    
    print "client connected"
	
    if not mythread.isAlive():
        print "starting thread"
        mythread.start()
        print "thread started"
        
if __name__ == '__main__':
    try:
        socketio.run(app)
    except KeyboardInterrupt as e:
        print e
        mythread.stop()		

