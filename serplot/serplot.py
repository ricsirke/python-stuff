# -*- coding: utf-8 -*-

from threading import *
import serial, json
from datetime import datetime
from collections import deque


class ReadSens(Thread):
    def __init__(self, sockio, port_name, baud):
		self.port_name = port_name
		self.sockio = sockio
		self.baud = int(baud)
		self.thread_stop_event = Event()
		super(readSens, self).__init__()
		
	def send(self, data):
		self.sockio.emit("newdata", {"data": data}, broadcast=True)
		
	def read(self):
		portname = self.port_name
		ser = serial.Serial(
			port=portname,\
			baudrate=baud,\
			parity=serial.PARITY_NONE,\
			stopbits=serial.STOPBITS_ONE,\
			bytesize=serial.EIGHTBITS,\
				timeout=0)

		print("connected to: " + ser.portstr)

		buff = ""
		while not self.thread_stop_event.isSet():
			line = ser.readline()
			
			print line
			self.send(buff)
			
		ser.close()
				
	def run(self):
		self.read()
		
	def stop(self):
	    self.thread_stop_event.set()
