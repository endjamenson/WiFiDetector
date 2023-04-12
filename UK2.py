import subprocess
import time
import RPi.GPIO as GPIO

# Disable GPIO warnings
GPIO.setwarnings(False)

# Set up GPIO
GPIO.setmode(GPIO.BCM)
GPIO.setup(5, GPIO.OUT)

# Load list of known MAC addresses
with open("known_macs.txt", "r") as f:
    known_macs = set([line.strip() for line in f])

while True:
    # Scan for devices
    output = subprocess.check_output(['sudo', 'iwlist', 'wlan1', 'scan'])
    new_macs = set([line.split()[4] for line in output.decode('utf-8').splitlines() if 'Address' in line])

    # Check for new devices
    for mac in new_macs:
        if mac not in known_macs:
            # Add new MAC address to list
            known_macs.add(mac)
            with open("known_macs.txt", "a") as f:
                f.write(mac + "\n")

            # Set output pin 5 to high
            print("New device found, setting output pin 5 to HIGH")
            GPIO.output(5, GPIO.HIGH)

    # Wait 5 seconds before scanning again
    time.sleep(5)
