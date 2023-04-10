import os
import shutil
from pathlib import Path

# Install xterm package
os.system('sudo apt-get update && sudo apt-get install -y xterm')
# Install gpio package
os.system('sudo apt-get install -y wiringpi')

# Add a line to autostart file to run manager.py on startup
file_path = "/etc/xdg/lxsession/LXDE-pi/autostart"
line_to_add = "\n@sudo python3 /home/pi/manager.py\n"
with open(file_path, "a") as f:
    f.write(line_to_add)
os.chmod(file_path, 0o777)

# Copy files from /home/pi/Desktop/files to the user's desktop
src_dir = "/home/pi/Desktop/files"
dst_dir = str(Path.home() / "Desktop")
files_to_copy = [
    os.path.join(src_dir, "playoutput.py"),
    os.path.join(src_dir, "turnoff.py"),
    os.path.join(src_dir, "UK2.py"),
    os.path.join(src_dir, "alert.mp3"),
    os.path.join(src_dir, "Ready.mp3")
]
for file_path in files_to_copy:
    shutil.copy2(file_path, dst_dir)

# Copy manager.py to /home/pi/
src_file_path = os.path.join(os.getcwd(), "manager.py")
dst_folder_path = "/home/pi/"
shutil.copy2(src_file_path, dst_folder_path)
os.chown(os.path.join(dst_folder_path, "manager.py"), 1000, 1000)
