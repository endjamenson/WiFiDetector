import RPi.GPIO as GPIO
import pygame
import time
pygame.mixer.init()
time.sleep(1) # Wait for 1 second
pygame.mixer.music.load("Ready.mp3")
pygame.mixer.music.play(loops=1)


GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(5, GPIO.OUT)  # Set up pin 5 as an output pin

while True:
    key_press = input("Press 'g' to turn off output pin 5, or 'w' to delete known_networks.txt file: ")
    
    if key_press == "g":
        GPIO.output(5, GPIO.LOW)  # Turn off output pin 5
    elif key_press == "w":
        with open("known_networks.txt", "w") as f:
            f.write("")  # Write an empty string to the file to clear its contents
