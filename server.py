#server.py
#---------
#Mike Moniz

import socket
import sys
import time
import string
import math

# readBuffer
# ----------
# s - the socket to be used
# wait - defaut to True, determines blocking or non-blocking
# Reads the buffer until the escape character '#' is read.
# Returns the concatinated message.
def readBuffer(s, wait=True):
	message = ""
	if(wait):
		s.setblocking(1)
	else:
		s.setblocking(0)
	try:
		byte = s.recv(1)
		#the '#' char is the end of info terminator
		while(byte != '#'):
			message = message + byte
			byte = s.recv(1)
	except Exception as e:
		return ""
	return message
# readBuffer
# ----------
# recvBuffer - the socket to read from
# sendBuffer - the socket to send to
# Reads the message that has been given and send it to the other client
def forward(recvBuffer, sendBuffer):
	try:
		message = readBuffer(recvBuffer, False)
		if(message != ""):
			print "forwarding message: " + message
			sendBuffer.send(message + "#")
	except:
		return
		

print "Sever has been turned on: Hello world"

port = sys.argv[1] #obtain the port
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
name = socket.gethostname()

s.bind((name,int(port)))
s.listen(5) #queues up to 5 requests

#Making the publicly known values constants for simplicity
p = 13597
g = 2

while 1:
	(alice, address1) = s.accept()
	print "Waiting for a friend to talk with..."
	(bob, address2) = s.accept()
	print "A friend has connected"

	#liason to key agreement
	alice.send(str(p) + "#")
	alice.send(str(g) + "#")
	bob.send(str(p) + "#")
	bob.send(str(g) + "#")
	
	A = readBuffer(alice)
	B = readBuffer(bob)
	
	#exchange public keys
	bob.send(A + "#")
	alice.send(B + "#")
	
	while 1:
		#relay alice's message to bob
		forward(alice, bob)
		
		#relay bob's message to alice
		forward(bob, alice)
		
	alice.send('t')
	bob.send('t')
	alice.close()
	bob.close()