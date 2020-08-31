
import serial
import time
import datetime
import json
import csv
import redis
import turtle
import operator



# turtle.pensize(5)
r = redis.Redis(host='localhost', port=6379, db=0)
DWM = serial.Serial(port="/dev/ttyACM0", baudrate=115200)
print("Connected to " + DWM.name)
DWM.write("\r\r".encode())
print("Encode")
time.sleep(1)
DWM.write("lec\r".encode())
print("Encode")
time.sleep(1)
dist_ = []
scale = (1000,1000)
try:
	with open('output.csv','w') as result_file:
		for i in range (0,100):
			data = DWM.readline()
			if(data):
				# print(data)
				if ("DIST" in data and "AN0" in data and "AN1" in data and "AN2" in data):
					data = data.replace("\r\n", "")
					data = data.decode().split(",")
					# print (data)
					data = data[::-1]
					data = data[2:4]
					data = data[::-1]
					# data = tuple(map(operator.mul, scale, data))
					print (data,'dddddd')

					wr = csv.writer(result_file, dialect='excel')
					wr.writerows([data])

	DWM.write("\r".encode())
	DWM.close()
except KeyboardInterrupt:
	print("Stop")
