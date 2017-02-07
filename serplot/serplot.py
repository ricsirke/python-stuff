# -*- coding: utf-8 -*-

from threading import *
import serial, json, time
from datetime import datetime
from collections import deque


BUFFSIZE = 10

class ReadSens(Thread):
    def __init__(self, sockio, port_name, baud):
        self.port_name = port_name
        self.sockio = sockio
        self.baud = int(baud)
        self.thread_stop_event = Event()
        self.buffsize = BUFFSIZE
        super(ReadSens, self).__init__()
        
    def send(self, data):
        self.sockio.emit("newdata", data, broadcast=True)
        
    def read(self):
        portname = self.port_name
        ser = serial.Serial(
            port=portname,\
            baudrate=self.baud,\
            parity=serial.PARITY_NONE,\
            stopbits=serial.STOPBITS_ONE,\
            bytesize=serial.EIGHTBITS,\
                timeout=0)

        print("connected to: " + ser.portstr)

        buff = []
        while not self.thread_stop_event.isSet():
            while len(buff) < self.buffsize:
                if ser.inWaiting() > 0:
                    line = ser.readline().strip()
                    if len(line) > 0:
                        buff.append(line)
            
            data = json.dumps({"data": buff})
            
            time.sleep(1)
            self.send(data)
            
            buff = []
            
        ser.close()
                
    def run(self):
        self.read()
        
    def stop(self):
        self.thread_stop_event.set()
