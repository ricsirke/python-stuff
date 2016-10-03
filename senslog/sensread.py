# -*- coding: utf-8 -*-

from threading import *
import serial, json
from datetime import datetime

thread = Thread()


class readSens(Thread):
	def __init__(self, sockio, port_name):
		self.port_name = port_name
		self.sockio = sockio
		self.thread_stop_event = Event()
		super(readSens, self).__init__()
		
	def proc_sens_data(self, rawdata):
		data = rawdata.split(",")
		
		now = datetime.now()
		meas_date = str(now.strftime('%Y-%m-%d'))
		meas_time = str(now.strftime('%H:%M:%S'))
		
		return [{
		"sensor": data[0].strip(),
		"status": data[1].strip(),
		"name": "Sensor name",
		"value": data[2].strip(),
		"uom": data[3].strip(),
		"date": meas_date,
		"time": meas_time
		}]
		
	def data_to_json(self, data):
		jsondata = { "data": [] }
		
		

		return json.dumps(jsondata)
		
		
	def read(self):
		portname = self.port_name
		ser = serial.Serial(
			port=portname,\
			baudrate=115200,\
			parity=serial.PARITY_NONE,\
			stopbits=serial.STOPBITS_ONE,\
			bytesize=serial.EIGHTBITS,\
				timeout=0)

		print("connected to: " + ser.portstr)

		buff = ""
		while not self.thread_stop_event.isSet():
			line = ser.readline()
			#spline = line.split("#")
			
			print line
			self.sockio.emit("newdata", {"data":self.data_to_json(buff)}, broadcast=True)
			
			# if len(spline) == 2:
				# buff += spline[0]
				
				# print buff
				# self.sockio.emit("newdata", {"data":self.data_to_json(buff)}, broadcast=True)
				
				# buff = spline[1]
			# elif len(spline) == 1:
				# buff += spline[0]
		ser.close()
				
	def run(self):
		self.read()