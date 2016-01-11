
# Import required Python libraries
import RPi.GPIO as GPIO
import sys

# Connect the Grove Relay to digital port D4
# SIG,NC,VCC,GND

GPIO.setwarnings(False)

# Use BCM GPIO references
# instead of physical pin numbers
GPIO.setmode(GPIO.BCM)

relay = 4

mode = sys.argv[1]

# Set pin as output
GPIO.setup(relay, GPIO.OUT)

try:		
	# set RPi board pin high

	if (int(mode) == 1) :
		GPIO.output(relay, GPIO.HIGH)
	else :
		GPIO.output(relay, GPIO.LOW)
		GPIO.cleanup()

	if ( GPIO.input(relay) == 1 ):
		print "1" 
	else : 
		print "0"

except KeyboardInterrupt:
      	# set RPi board pin low
	GPIO.output(relay, GPIO.LOW)
	GPIO.cleanup()

except IOError:
	print "Error"
