#motion.py
#---------
#Mike Moniz

#Script to work with PIR Motion Sensor

# Import required Python libraries
import RPi.GPIO as GPIO
import time
import client

# Use BCM GPIO references
# instead of physical pin numbers
GPIO.setmode(GPIO.BCM)

ip = "192.168.0.11"
port = 29876
message = "opensesame"

# GPIO defines the pin to use on Pi
# timeout is in seconds	
def detectMotion( GPIO_PIR = 4, timeout=7200):
	print ("PIR Module Test CTRL-C to exit")

	# Set pin as input
	GPIO.setup(GPIO_PIR,GPIO.IN)

	Current_State= 0
	Previous_State = 0

	try:

		print ("Waiting for PIR to settle ...")

		# Loop until PIR output is 0
		while GPIO.input(GPIO_PIR)==1:
			Current_State= 0

		print (" Ready")
		
		start = time.time()
		now = time.time()
		
		while (now - start) < timeout : 
			# Read PIR state
			Current_State = GPIO.input(GPIO_PIR)

			if Current_State==1 and Previous_State==0:
				# PIR is triggered
				print (" Motion detected!")
				
				client.sendMessage( ip, port, message)
				break
				
				# Record previous state
				Previous_State=1
			elif Current_State==0 and Previous_State==1:
				# PIR has returned to ready state
				print (" Ready")
				Previous_State=0

			# Wait for 10 milliseconds
			time.sleep(0.01)
			now = time.time()

	except KeyboardInterrupt:
		print (" Quit") 
		# Reset GPIO settings
		GPIO.cleanup()
detectMotion(4,10)