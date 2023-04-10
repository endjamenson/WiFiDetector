# WiFiDetector
Download and extract the Raspbian OS. If you need a program to extract the image, I reccomened Winrar. or 7zip. Or a limp wrist. 

https://downloads.raspberrypi.org/raspios_armhf/images/raspios_armhf-2023-02-22/2023-02-21-raspios-bullseye-armhf.img.xz

Once the image is extracted, install the OS onto your Pi using Win32 Disk Imager if you are using windows. If you arent, you probably do not need me to tell you how to do this part. 

https://win32diskimager.org/

Setup the system, and use the username pi if you want to use the installer script, as it will make it simpler to setup.  

Update the thing when it asks, use wifi or whatever you want. Restart it when it tells you to. 

Once you are logged into the desktop, open up a terminal and change directory into the folder that you downloaded with the files in it.  Make sure the folder name on the desktop is called files.   In my case, I passed the command

cd Desktop/files

Once you are in the directory with the files to install, pass the commad 

sudo python3 installer.py

