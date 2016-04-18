## YouTube tutorial video
https://www.youtube.com/watch?v=RTCG1Fm3kS4
	
	
## What you need?
- A camera, I used SONY A6300
- Raspberry Pi, mine is version 2 model B
- HC-SR501 motion sensor
	
	
## Here are the steps for the Raspberry Pi
	Step 1:
		Make sure it is updated:
		sudo apt-get update
		sudo apt-get upgrade
		
	Step 2:
		Install git if necessary:
		sudo apt-get install git
		
	Step 3:
		Install gphoto2 lib with this one line command:
		wget https://raw.githubusercontent.com/gonzalo/gphoto2-updater/master/gphoto2-updater.sh && chmod +x gphoto2-updater.sh && sudo ./gphoto2-updater.sh
		More info: http://gphoto.sourceforge.net/
		
	Step 4:
		Create a python file named detection.py
		Find the source file at my GitHub:
		https://github.com/seesunmoon/rpi_camera_sensor
		
	Step 5:
		Run the script:
		python ./detection.py
