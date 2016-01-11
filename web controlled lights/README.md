# Raspberry Pi
Home Improvement with a Raspberry Pi: Control your lights from your phone or computer

Installation:

Hardware Used
1. Raspberry Pi x1
2. WiFi USB x1
3. SD Card x1 (8GB)
4. Extension cord x1
5. Female to Female wire x 3
6. Grove-Relay x1 (Model: 103020005)

Steps:

1. Install Raspberry Pi OS
	-To setup the RPi check out this great tutorial: https://www.raspberrypi.org/help/noobs-setup/
2. Connect the Pi to a local wifi network shared with your laptop
3. Cut the cable that comes with the relay and split the female to female wires and connect them together
4. Pull apart a few inches of the extension cord and split ONLY ONE of the wires
5. Connect the extension cord wire into the relay
6. Connect the signal wires to the relay and the RPi
7. Check out the Wiki: http://www.seeedstudio.com/wiki/Grove_-_Relay for details on the device
8. Read this website for instructions on how to set up the apache server with php http://www.php5dp.com/easy-writer-setup-for-raspberry-pi-php/
	8.1. Install Apache and PHP
		sudo apt-get install apache2 php5 libapache2-mod-php5

		Note: You might have to run this command before the install works

		sudo apt-get update
	8.2 Before being able to write to the new server folder /var/www we need to change the permissions

		sudo chown www-data:www-data /var/www
		sudo chmod 775 /var/www
		sudo usermod -a -G www-data pi
		sudo reboot

	8.3 Put all of the code inside the html file
	8.4 Edit the sudoers file in /etc/sudoers.d and add 
		www-data ALL=(ALL) NOPASSWD: ALL
9. Access from a laptop or phone through a browser at
	http://youripaddress/lights.php
10. Toggle the on/off buttons to control lights


