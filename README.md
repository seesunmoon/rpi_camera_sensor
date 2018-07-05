## YouTube tutorial video
English: https://www.youtube.com/watch?v=u2O082hDafs
	
	
## What you need?
- A camera, I used SONY A6300
- Raspberry Pi, mine is version 2 model B
- HC-SR501 motion sensor
	
	
## Here are the steps for the Raspberry Pi
	Step 1:
		Connect the motion sensor to the Pi 5V, GND and GPIO pin (note the pin number)
		Connect the camera to Pi, make sure it is in PC Remote mode
		
	Step 2:
		Make sure it is updated:
		sudo apt-get update
		sudo apt-get upgrade
		
	Step 3:
		Install git if necessary:
		sudo apt-get install git
		
	Step 4:
		Install gphoto2 lib with this one line command:
		wget https://raw.githubusercontent.com/gonzalo/gphoto2-updater/master/gphoto2-updater.sh && chmod +x gphoto2-updater.sh && sudo ./gphoto2-updater.sh
		More info: http://gphoto.sourceforge.net/
		
	Step 5:
		Download the python script detection.py from:
		https://github.com/seesunmoon/rpi_camera_sensor
		
	Step 6:
		Run the script:
		python ./detection.py
