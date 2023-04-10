import RPi.GPIO as GPIO
import pygame

GPIO.setwarnings(False)

GPIO.setmode(GPIO.BCM)
GPIO.setup(5, GPIO.IN)  # Set up pin 5 as an input pin

pygame.mixer.init()
pygame.mixer.music.load("alert.mp3")  # Load the audio file

is_playing = False  # Initialize variable to keep track of whether sound is playing or not

while True:
    if GPIO.input(5) == GPIO.HIGH:  # Check if pin 5 is set to high
        if not is_playing:
            pygame.mixer.music.play(loops=-1)  # Loop the audio file
            is_playing = True  # Set variable to indicate sound is playing
    else:
        if is_playing:
            pygame.mixer.music.stop()  # Stop playing the audio file
            is_playing = False  # Set variable to indicate sound is not playing
