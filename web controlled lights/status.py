# Import required Python libraries
import RPi.GPIO as GPIO

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)

relay = 4
GPIO.setup(4, GPIO.OUT)

try:
	status = GPIO.input(relay)
	print status
		
except IOError:
	print "Error"
