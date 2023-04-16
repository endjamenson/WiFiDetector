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

# Open log file in append mode
with open("log.txt", "a") as log_file, open("console.log", "a") as console_file:
    while True:
        # Scan for devices
        try:
            output = subprocess.check_output(['sudo', 'iwlist', 'wlan1', 'scan'], stderr=subprocess.STDOUT)
        except subprocess.CalledProcessError as e:
            # If there is an error, log it to console and error log file
            error = "Error executing subprocess: " + str(e.returncode) + "\n" + e.output.decode('utf-8')
            print(error)
            console_file.write(error + "\n")
            log_file.write("Error executing subprocess at " + time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()) + "\n")
            continue

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

                # Write event to log file
                log_file.write("New device found with MAC address " + mac + ". Output pin 5 set to HIGH.\n")

        # Wait 5 seconds before scanning again
        time.sleep(5)

        # Write output to console log file
        console_file.write(output.decode('utf-8'))
