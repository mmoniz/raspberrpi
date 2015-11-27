# Raspberry Pi
Home Improvement with a Raspberry Pi: Automatically turn on Spotify when you enter your home

Installation:

Hardware Used
1. Raspberry Pi x1
2. WiFi USB x1
3. SD Card x1 (8GB)
4. Ethernet Cable x 5 meters
5. Female to Female wire x 3
6. PIR Motion Sensor x1 (Model: SEN116A2B)

Steps:

1. Install Raspberry Pi OS
	-To setup the RPi check out this great tutorial: https://www.raspberrypi.org/help/noobs-setup/
2. Connect the Pi to a local wifi network shared with your laptop
3. Strip the Ethernet cable or other wire if you have it and to extend the female to female wires.
4. Connect the motion sensor - by default the application expects pin 4 for the signal
	http://cdn.instructables.com/F8V/Q8TD/FYIZHAJL/F8VQ8TDFYIZHAJL.MEDIUM.gif
5. Mount the motion sensor in some desired location
	-Remember this detects infra-red so the motion sensor needs to detect you not the door  
6. Configure the motion.py script to have the IP address of your laptop as a param. 
7. Provide your facebook username and password as an input for the spotify.jar
8. If you modify the port you will need to also modify it on the server.py script
9. Use cron or Windows Task Scheduler to automate your server.py script
10. Use cron on the pi to run the motion.py script
	
	#Monday to Friday at 3:10pm run media.sh
	eg "10 15 * * 1-5 cd /home/pi && bash media.sh >> /tmp/media_log.txt &"

	media.sh: this will run the script
		#!/usr/bash
		#!/usr/bin/python

		stdbuf -oL python motion.py >> /logs/media_log.txt

Behaviour:
Once motion is detected it will attempt to send a message to the server through a socket layer and quit.
The server will attempt to read the signal and launch spotify.jar. This will automatically log into spotify
and run one of your playlists randomly.


Sample output from motion.py:

PIR Module Test CTRL-C to exit
Waiting for PIR to settle ...
 Ready
 Start time=2015-11-25 17:37:43
 Motion detected! > 2015-11-25 17:37:54
 ip: 192.168.0.11
 port: 29875
 connecting...
 ready to send data
 sent data

