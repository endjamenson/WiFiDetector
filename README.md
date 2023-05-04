# WiFiDetector (The Double D, Drone Detector!)


The case can be printed by any 3d Printer, and the STL file is included.  I would recommend at least a 30 percent infill.  Slide it all together after it is finished and use glue if you fancy. STL file is the “WiFi Detector Model.STL”.  I had to glue this thing a bunch to make it stick, so be aware, it may be better and faster to build it out of a tin can.  

For the project, I used a Raspberry 4 Model B, which should be readily available (granted, in current times these are rather expensive due to supply chain reasons).  Any power bank will work, but I would shoot for one that is 30000mAh or more, as one that is 30000mAh was able to completely power the setup for 6 hours (with no jamming). You will need speakers to go with this, I opted for USB powered ones that work off the 3.5mm jack audio of the Raspberry Pi.  For the detection of wireless networks, what I used as a directional antenna, which means that you are no longer looking in all directions, but one direction, meaning the distance that you are scanning goes up dramatically.  I would use any that are cheap and available, as it is inconsequential which one you use, as long as it is directional.  If you are planning on making the setup for violations of FCC guidance (because you are in a warzone, and outside of the purview of US government guidelines, ALWAYS follow local laws and ordinances), you should get two, one for detection, one for the jammer, so that you can focus the beam of felonies in one direction, increasing the range of disruption.   As for the Wireless adapter that I used, this one took some work, and I had to buy around 3 different versions until I got one that did not require additional drivers/ setup.  The UK2.py is setup to use the wireless adapter of wlan1, which should be a plugged in WiFi adapter, assuming that you have a built in WiFi adapter already on the pi.  If you want to be able to plug and play this device, you need to make sure that the Wireless adapter not only has an external antenna connection, but it will not require any additional work to function beyond plugging it in. 
	
	TL:DR; parts list-
1x - Raspberry Pi Model 4 Model B-

•	https://www.amazon.com/Raspberry-Model-2019-Quad-Bluetooth/dp/B07TC2BK1X?th=1

1x – Power Bank 30000mAh Battery Pack

•	https://www.amazon.com/gp/product/B09NKVCJ15/ref=ppx_yo_dt_b_asin_title_o01_s00?ie=UTF8&th=1

2x - Directional Wireless Antenna (1x if you just want to see something coming at you)

•	https://www.amazon.com/gp/product/B07L56S88C/ref=ppx_yo_dt_b_asin_title_o02_s00?ie=UTF8&psc=1x

1x – Relay for controlling a WiFi Jammer, connected to output 5 of the device- 

•	https://www.amazon.com/gp/product/B0BG2F7349/ref=ppx_yo_dt_b_asin_title_o00_s00?ie=UTF8&psc=1

1x Keyboard, I used an OSU one that shrunk the size of the keyboard to 3 keys, then programmed it for only the keys I needed.  (G key is for acknowledging the new WiFi device, W key is for clearing out the known WiFi device list, and the enter key for passing the command after the previous key is hit)

•	https://www.amazon.com/gp/product/B09Y5NC6LL/ref=ppx_yo_dt_b_asin_title_o05_s00?ie=UTF8&psc=1

1x – WiFi card for detection that has an external connection for a directional antenna-

•	https://www.amazon.com/gp/product/9800359850/ref=ppx_yo_dt_b_asin_title_o01_s00?ie=UTF8&psc=1

1x Memery card for running the Pi-

•	https://www.amazon.com/SanDisk-2-Pack-microSDHC-Memory-2x32GB/dp/B08J4HJ98L/ref=sr_1_8?keywords=micro%2Bsd%2Bmemory%2Bcard&qid=1681635489&sr=8-8&th=1


After collection of the parts, download and extract the Raspbian OS. If you need a program to extract the image, I recommend Winrar. or 7zip. Or a limp wrist. 

https://downloads.raspberrypi.org/raspios_armhf/images/raspios_armhf-2023-02-22/2023-02-21-raspios-bullseye-armhf.img.xz

Once the image is extracted, install the OS onto your Pi using Win32 Disk Imager if you are using windows. If you arent, you probably do not need me to tell you how to do this part. 

https://win32diskimager.org/

Setup the system and use the username pi if you want to use the installer script, as it will make it simpler to setup.  The password does not matter, but I would reccomened not using the known standard of “raspbian”, because that will introduce a variety of issues.  OpSec, people, it is nessesary. 

Update the thing when it asks, use WiFi or whatever you want. Restart it when it tells you to. 

Once you are logged into the desktop, open a terminal.

While I tried to ensure that it installs automatically, there seems to be some issue with Xterm.  Install it manually first with passing the command-

sudo apt-get update && sudo apt-get install -y xterm

After Xterm installs, change the directory into the folder that you downloaded with the files in it.  Make sure the folder name on the desktop is called files.   In my case, I passed the command

cd Desktop/files

Once you are in the directory with the files to install, pass the commad 

sudo python3 installer.py

Once this has been done, the device will be in the desired state, as long as no monitor is installed, and you are not remoted into the device.  It will scan for any new MAC addresses and alarm whenever they are found, and turn on Pin 5 of the raspberry pi. Hook up a relay to said pin if you want, and then a relay can actuate any device you would want. 
This solution is not bulletproof or perfect for a variety of reasons.  This thing only detects WiFi devices, and drones can use a wide variety of communication methods, such as 5G, 4G, etc.  This was mainly done as a hey, this is an idea, if you want to expand upon it, this is just the framework, so be aware of that fact. This thing will also not alert if it hangs, so the IDEAL way of running this as it is would be to perform a restart of the device periodically to ensure that it is still working.  Better yet, would be to program something into it that would indicate that everything is running correctly.  If you got the brain for writing code, then I would encourage you to ‘Fork’? I think is the words the kids are using for this site? 
At the end of the day, this does not personally do anything for me, and I do not have much of a dog in this show. I just had an idea, and it seemed like a decent one, so I decided to make it a real thing. 

If you would like to buy me a coffee, here is an ETH wallet. 
0x1ce14a098ba2eeb3886894248fdb9a0de48283d8
