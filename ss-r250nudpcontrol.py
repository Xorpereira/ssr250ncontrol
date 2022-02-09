# coding=utf-8

#Tascam SS-R250N Telnet control

import telnetlib
import socket
import time
import sys

if len(sys.argv) == 2:
	devicetype="none"
elif len(sys.argv) == 4:
	devicetype=sys.argv[3]

deviceID=sys.argv[1]
print("Selected Device ID %s" % deviceID)
UDP_IP="127.0.0.1" #IP localhost
UDP_PORT=5005

host='none'
port='none'

if deviceID == "1":
	host='192.192.192.205'
	port='23'
elif deviceID == "2":
	host='192.192.192.206'
	port='23'
elif deviceID == "3":
	host='192.192.192.207'
	port='23'
elif deviceID == "4":
	host='192.192.191.208'
	port='23'
elif deviceID == "5":
	host=sys.argv[2]
	port='23'
else:
	print("Invalid Device ID")
	sys.exit("Program terminated")

#ipfile=open('hd-r1ip.txt', 'r')
#with open("hd-r1ip.txt") as f:
#    firstline = f.readline().rstrip()
#host=firstline
#tn=telnetlib.Telnet('192.192.192.201') #Endereço IP Tascam HD-R1

#Ligação à máquina
try:
    tn = telnetlib.Telnet(host, str(port))
    print("You are connected")
    time.sleep(1)
except Exception as e:
    print("Connection cannot be established", e)
    traceback.print_exc()

#Login na máquina
if deviceID == "1" or deviceID == "2" or deviceID == "3" or deviceID == "4" or devicetype == "ss":
	tn.write(b"\r\n")
	tn.write(b"SS-R250N\r\n")
	print("You are logged in")
elif devicetype == "hd":
	print("Wrong Device Type")
	sys.exit("Program Terminated")



sock = socket.socket(socket.AF_INET, # Internet
		     socket.SOCK_DGRAM) # UDP
sock.bind((UDP_IP, UDP_PORT))

while True:
	data, addr = sock.recvfrom(1024) # buffer size is 1024 bytes
	print("received message: %s" % data)
	tn.write(b"%s\r\n" % data)
	print("%s\r\n" % data)