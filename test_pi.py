import RPi.GPIO as GPIO
import time

# Set pin numbering mode
GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)

# Define pin numbers
ground_pin = 6
buzzer_pin = 12
blue_led_pin = 16
green_led_pin = 18
red_led_pin = 22
yellow_led_pin = 11
white_led_pin = 13

# Configure pins
GPIO.setup(buzzer_pin, GPIO.OUT)
GPIO.setup(blue_led_pin, GPIO.OUT)
GPIO.setup(green_led_pin, GPIO.OUT)
GPIO.setup(red_led_pin, GPIO.OUT)
GPIO.setup(yellow_led_pin, GPIO.OUT)
GPIO.setup(white_led_pin, GPIO.OUT)

# Loop until 'q' key is pressed
while True:
    GPIO.output(buzzer_pin, GPIO.HIGH)
    GPIO.output(blue_led_pin, GPIO.HIGH)
    GPIO.output(green_led_pin, GPIO.HIGH)
    GPIO.output(red_led_pin, GPIO.HIGH)
    GPIO.output(yellow_led_pin, GPIO.HIGH)
    GPIO.output(white_led_pin, GPIO.HIGH)
    time.sleep(5)
    
    GPIO.output(buzzer_pin, GPIO.LOW)
    GPIO.output(blue_led_pin, GPIO.LOW)
    GPIO.output(green_led_pin, GPIO.LOW)
    GPIO.output(red_led_pin, GPIO.LOW)
    GPIO.output(yellow_led_pin, GPIO.LOW)
    GPIO.output(white_led_pin, GPIO.LOW)
    time.sleep(5)

    # Check for key press
    if input() == 'q':
        break
