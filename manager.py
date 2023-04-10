import subprocess
import psutil
import os
import time

# Define the command to start each script
script1_cmd = ["sudo", "python3", "/home/pi/Desktop/UK2.py"]
script2_cmd = ["python3", "/home/pi/Desktop/playoutput.py"]
script3_cmd = ["python3", "/home/pi/Desktop/turnoff.py"]

# Set the ID of the script to keep in focus (replace with your own)
script_to_focus = None

# Start each script as a subprocess
script1_proc = subprocess.Popen(script1_cmd)
script2_proc = subprocess.Popen(script2_cmd)
script3_proc = subprocess.Popen(script3_cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE)

# Store the process IDs in a list
processes = [script1_proc, script2_proc, script3_proc]

# Set the current working directory to the script directory
os.chdir("/home/pi/Desktop")

# Loop indefinitely
while True:
    for i, process in enumerate(processes):
        # Check if the process has exited
        if process.poll() is not None:
            # Restart the process
            processes[i] = subprocess.Popen(process.args)
            # If it's the script that needs to be in focus, update its process ID
            if i == 2:
                script_to_focus = processes[i].pid
    
    # Check if the third script is running
    if script3_proc.poll() is None:
        # Open a new terminal window for the third script if it's not already in focus
        if script_to_focus is None:
            script_to_focus = subprocess.Popen(['xterm', '-e', 'sudo', 'python3', '/home/pi/Desktop/turnoff.py']).pid
        # If the window is already open, check if it's in focus and update it if not
        else:
            psutil.Process(script_to_focus).as_dict(attrs=['pid', 'ppid', 'name', 'username', 'exe', 'cmdline', 'create_time', 'cpu_percent', 'memory_percent']).as_dict(flat=True)
    
    time.sleep(1)
