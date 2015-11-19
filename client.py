#client.py
#---------
#Mike Moniz

import socket
import sys
import string

def sendMessage(ip, port, message):
	print (ip)
	print (port)

	#connect to the server
	try:
		s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

		print (" connecting...")
		s.connect((ip,int(port)))
		
		print (" ready to send data")
		
		message = message + "#" #escape terminal
		
		s.send( message.encode('utf-8'))

		print (" sent data")
	except Exception as e:
		print (e)
	except KeyboardInterrupt:
		print (" Quit")
	finally:
		s.close()

#example usage
#ip = sys.argv[1] #"192.168.0.11"
#port = sys.argv[2] #29876
#message = sys.argv[3] #"opensesame"

#sendMessage(ip, port, message)