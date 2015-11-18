#client.py
#---------
#Mike Moniz

import socket
import sys
import time
import string
import math
import random
import select

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

# RC4_init
# ----------
# key - private key for encryption/decryption
# Initializes RC4 based on the private key and 
# returns an array, k.
def RC4_init(key):
	k = range(256)
	j = 0
	for i in range(256):
		j = (j + k[i] + int(key[i % len(key)])) % 256
		k[i], k[j] = k[j], k[i]
	return k

# psuedo_random
# -------------
# k - array generated from RC4_init
# Generates a psuedo random value.
def psuedo_random(k):
	i = 0
	j = 0
	while 1:
		i = (i + 1) % 256
		j = (j + k[i]) % 256
		k[i], k[j] = k[j], k[i]
		yield k[(k[i] + k[j]) % 256]

# RC4
# ---
# k - array generated from RC4_init
# text - plain/ciphertext
# Uses the properties of XOR to evaluate either the 
# ciphertext or plaintext. It returns the translation.
def RC4(k, text):
	ciphertext = []
	psuedo_random_bytes = psuedo_random(k)
	for char in text:
		byte = ord(char)
		cipher_byte = byte ^ psuedo_random_bytes.next()
		ciphertext.append(chr(cipher_byte))
	return ''.join(ciphertext)

# pow_mod
# -------
# base - number to be raised to the exponent
# exponent - number to raise the base with
# modulo - limits the range of the value
# Computes the power while limiting the upper bound to
# the modulo.
def pow_mod(base, exponent, modulo):
	result = base
	for i in xrange(exponent):
		result *= base
		result = int(result % modulo)
	return result

# rawinput
# --------
# Checks to see if there is a message typed and
# returns the value.
def rawinput():
	#sys.stdout.write(message)
	i, o, e = select.select([sys.stdin], [], [], 1)
	if(i):
		return sys.stdin.readline()
	else:
		return "";

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

ip = sys.argv[1]
port = sys.argv[2]

#connect to the server
try:
	s.connect((ip,int(port)))
    
	#recieve info to agree on keys
	p = int(readBuffer(s))
	g = int(readBuffer(s))
	
	#Begin diffie-hellman
	kprivate = random.randrange(2, 20000)
	kpublic = pow_mod(g,kprivate, p)
	
	#send K to public
	s.send(str(kpublic) + '#')
	
	#Receive K' from other client
	kprime = int(readBuffer(s))
	
	kprivate = pow_mod(kprime, kprivate, p)
	#End diffie-hellman
	
	k = RC4_init(str(kprivate))
	
	print "Type your message and return to send"
	
	while 1:
		#Check for messages from the other client
		ciphertext = readBuffer(s, False)
		
		#Check for termination code
		if (ciphertext == "t"):
			break
		elif(ciphertext != ""):
			#decrypt and print the message
			plaintext = RC4(k, ciphertext)
			print "Friend: " + plaintext
		
		plaintext = rawinput()
		if(plaintext != ''):
			#encrypt the message and send it to the client
			ciphertext = RC4(k, plaintext)
			s.send(ciphertext + "#")
			
except Exception as e:
	print e
	s.send('t')
finally:
	s.close()