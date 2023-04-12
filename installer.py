import os
import shutil
import time
from pathlib import Path

def create_known_macs_file():
    file_path = "/home/pi/Desktop/known_macs.txt"
    with open(file_path, "w") as f:
        pass # creates an empty file
    os.chmod(file_path, 0o777)

# Install xterm package
time.sleep(5)
os.system('sudo apt-get update && sudo apt-get install -y xterm')

# Install gpio package
time.sleep(5)
os.system('sudo wget https://github.com/WiringPi/WiringPi/releases/download/2.61-1/wiringpi-2.61-1-armhf.deb')
os.system('sudo dpkg -i wiringpi-2.61-1-armhf.deb')

# Add a line to autostart file to run manager.py on startup
file_path = "/etc/xdg/lxsession/LXDE-pi/autostart"
line_to_add = "@sudo python3 /home/pi/manager.py"
with open(file_path, "r+") as f:
    content = f.read()
    if line_to_add not in content:
        f.write(f"\n{line_to_add}\n")
os.chmod(file_path, 0o777)

# Create known_macs.txt file
create_known_macs_file()

# Copy files from /home/pi/Desktop/files to the user's desktop
src_dir = "/home/pi/Desktop/files"
dst_dir = "/home/pi/Desktop/"
playoutput_path = os.path.join(src_dir, "playoutput.py")
shutil.copy2(playoutput_path, os.path.join(dst_dir, "playoutput.py"))
os.chmod(os.path.join(dst_dir, "playoutput.py"), 0o777)
turnoff_path = os.path.join(src_dir, "turnoff.py")
shutil.copy2(turnoff_path, os.path.join(dst_dir, "turnoff.py"))
os.chmod(os.path.join(dst_dir, "turnoff.py"), 0o777)
uk2_path = os.path.join(src_dir, "UK2.py")
shutil.copy2(uk2_path, os.path.join(dst_dir, "UK2.py"))
os.chmod(os.path.join(dst_dir, "UK2.py"), 0o777)
alert_path = os.path.join(src_dir, "alert.mp3")
shutil.copy2(alert_path, os.path.join(dst_dir, "alert.mp3"))
os.chmod(os.path.join(dst_dir, "alert.mp3"), 0o777)
ready_path = os.path.join(src_dir, "Ready.mp3")
shutil.copy2(ready_path, os.path.join(dst_dir, "Ready.mp3"))
os.chmod(os.path.join(dst_dir, "Ready.mp3"), 0o777)

# Copy manager.py to /home/pi/
src_file_path = os.path.join(os.getcwd(), "manager.py")
dst_folder_path = "/home/pi/"
shutil.copy2(src_file_path, os.path.join(dst_folder_path, "manager.py"))
os.chown(os.path.join(dst_folder_path, "manager.py"), 1000, 1000)
os.chmod(os.path.join(dst_folder_path, "manager.py"), 0o777)
