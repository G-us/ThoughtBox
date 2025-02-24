import RPi.GPIO as GPIO
import requests
import time

# Set up GPIO
button_pin = 23  # Change this to your button pin
GPIO.setmode(GPIO.BCM)
GPIO.setup(button_pin, GPIO.IN, pull_up_down=GPIO.PUD_UP )

requests.get('#CHANGEME') # Change ip to the one given by tailscale when doing the Tailscale Serve command.

def button_callback():
    # Send a notification or request when the button is pressed
    print("hello")
    requests.get('#CHANGEME')  # Change ip to the one given by tailscale when doing the Tailscale Serve command.



try:
    # Keep the program running
    while True:
        if not (GPIO.input(button_pin)):
            button_callback()
except KeyboardInterrupt:
    GPIO.cleanup()
