import RPi.GPIO as GPIO
import pygame

GPIO.setmode(GPIO.BCM)
GPIO.setup(4, GPIO.IN)  # Set up pin 4 as an input pin
GPIO.setup(5, GPIO.OUT)  # Set up pin 5 as an output pin

pygame.init()
pygame.display.set_mode((640, 480))  # Create a window for pygame

while True:
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:  # Check for spacebar key press
            GPIO.output(5, GPIO.LOW)  # Set pin 5 to low
        elif GPIO.input(4) == GPIO.HIGH:  # Check if pin 4 is set to high
            GPIO.output(5, GPIO.LOW)  # Set pin 5 to low
