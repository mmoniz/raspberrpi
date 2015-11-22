#server.py
#---------
#Mike Moniz

import socket
import sys
import time
import string
import math
import subprocess

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

def activateCode(code):
	return code == "opensesame" or code == "partyon!"

def playMusic():
	print (" Playing your favourite music in a moment...")
	try:
		subprocess.call(['java', '-jar', 'C:\\wamp\\www\\raspberrypi\\spotify.jar'])
	finally:
		print (" Enjoy these vibes!")

def bootUp(port=29875, timeout=7200):
	print (" Waking up... Yawn.")
	
	play=False
	
	try :
		s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		s.settimeout(timeout) #wait for 2 hours then turn off
		
		name = socket.gethostname()

		s.bind((name,int(port)))
		s.listen(5) #queues up to 5 requests
		
		print (" Waiting for a Raspberry Pi to talk with...")
			
		(rpi, address1) = s.accept()
		
		start = time.time()
		now = start
		
		#wait for duration
		while 1 :
			code = readBuffer(rpi, False)
			
			if ( activateCode(code) ):
				print ( " Welcome Home, Mike!")
				play=True
				break
	except KeyboardInterrupt:
		print (" Goodbye, Mike")
	finally :
		s.close()
	if play:
		playMusic()
	else: 
		print ("Something went wrong, we are not playing your music")
	
#port = 29876 #sys.argv[1] #obtain the port

bootUp( )
