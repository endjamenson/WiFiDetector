import subprocess
import psutil
import os

# Define the command to start each script
script1_cmd = "sudo python3 /home/pi/Desktop/UK2.py"
script2_cmd = "python3 /home/pi/Desktop/playoutput.py"
script3_cmd = "sudo python3 /home/pi/Desktop/turnoff.py"

# Start each script as a subprocess, with working directory set to /home/pi/Desktop
script1_proc = subprocess.Popen(script1_cmd.split(), cwd="/home/pi/Desktop")
script2_proc = subprocess.Popen(script2_cmd.split(), cwd="/home/pi/Desktop")
script3_proc = subprocess.Popen(script3_cmd.split(), stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True, cwd="/home/pi/Desktop")

# Store the process IDs in a list
processes = [script1_proc, script2_proc, script3_proc]

# Set the current working directory to the script directory
os.chdir("/home/pi/Desktop")

# Set the ID of the script to keep in focus (replace with your own)
script_to_focus = script3_proc.pid

# Loop indefinitely
while True:
    for i, process in enumerate(processes):
        # Check if the process has exited
        if process.poll() is not None:
            # Restart the process
            processes[i] = subprocess.Popen(process.args.split(), cwd="/home/pi/Desktop")
    
    # Check if the third script is running
    if script3_proc.poll() is None:
        # Open a new terminal window for the third script, with working directory set to /home/pi/Desktop
        subprocess.Popen(['xterm', '-e', 'python3 /home/pi/Desktop/turnoff.py'], cwd="/home/pi/Desktop")
        # Set the window of the third script to be in focus
        psutil.Process(script_to_focus).as_dict(attrs=['pid', 'ppid', 'name', 'username', 'exe', 'cmdline', 'create_time', 'cpu_percent', 'memory_percent']).as_dict(flat=True)
