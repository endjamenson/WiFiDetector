import time
import datetime
import RPi.GPIO as GPIO
import subprocess

# Disable GPIO warnings
GPIO.setwarnings(False)

# Set up GPIO
GPIO.setmode(GPIO.BCM)
GPIO.setup(5, GPIO.OUT)

# Load list of known MAC addresses and last seen times
with open("known_networks.txt", "r") as f:
    known_macs = {}
    for line in f:
        mac, timestamp = line.strip().split(",")
        known_macs[mac] = datetime.datetime.strptime(timestamp, "%Y-%m-%d %H:%M:%S")

while True:
    # Determine scanning interval based on time of day
    now = datetime.datetime.now().time()
    if now >= datetime.time(19) or now < datetime.time(7):
        interval = 2
    else:
        interval = 5

    # Scan for networks and retrieve MAC addresses
    scan_output = subprocess.check_output(["sudo", "iwlist", "wlan0", "scan"]).decode()
    new_macs = set([line.split()[4] for line in scan_output.split("\n") if "Address:" in line])

    # Check for new MAC addresses
    for mac in new_macs:
        if mac not in known_macs:
            # Add new MAC address to list
            known_macs[mac] = datetime.datetime.now()
            with open("known_macs.txt", "a") as f:
                f.write(mac + "," + str(known_macs[mac]) + "\n")

            # Set output pin 5 to high
            print("New MAC address found, setting output pin 5 to HIGH")
            GPIO.output(5, GPIO.HIGH)
        else:
            # Update last seen time
            known_macs[mac] = datetime.datetime.now()
            with open("known_macs.txt", "w") as f:
                for mac, timestamp in known_macs.items():
                    f.write(mac + "," + str(timestamp) + "\n")

    # Update last seen file
    with open("last_seen.txt", "w") as f:
        for mac, timestamp in known_macs.items():
            f.write(mac + "," + str(timestamp) + "\n")

    # Wait before scanning again
    time.sleep(interval)
