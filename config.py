import RPi.GPIO as GPIO
import time

# Set pin numbering mode
GPIO.setmode(GPIO.BCM)

# Define pin numbers
ground_pin = 6
buzzer_pin = 12
blue_led_pin = 23
green_led_pin = 24
red_led_pin = 25
yellow_led_pin = 17
white_led_pin = 27

# Configure pins
GPIO.setup(ground_pin, GPIO.OUT)
GPIO.setup(buzzer_pin, GPIO.OUT)
GPIO.setup(blue_led_pin, GPIO.OUT)
GPIO.setup(green_led_pin, GPIO.OUT)
GPIO.setup(red_led_pin, GPIO.OUT)
GPIO.setup(yellow_led_pin, GPIO.OUT)
GPIO.setup(white_led_pin, GPIO.OUT)

try:
    # Set ground pin to low (ground)
    GPIO.output(ground_pin, GPIO.LOW)

    # Blink the LEDs and sound the buzzer
    while True:
        GPIO.output(buzzer_pin, GPIO.HIGH)
        GPIO.output(blue_led_pin, GPIO.HIGH)
        GPIO.output(green_led_pin, GPIO.HIGH)
        GPIO.output(red_led_pin, GPIO.HIGH)
        GPIO.output(yellow_led_pin, GPIO.HIGH)
        GPIO.output(white_led_pin, GPIO.HIGH)
        time.sleep(1)

        GPIO.output(buzzer_pin, GPIO.LOW)
        GPIO.output(blue_led_pin, GPIO.LOW)
        GPIO.output(green_led_pin, GPIO.LOW)
        GPIO.output(red_led_pin, GPIO.LOW)
        GPIO.output(yellow_led_pin, GPIO.LOW)
        GPIO.output(white_led_pin, GPIO.LOW)
        time.sleep(1)

except KeyboardInterrupt:
    # Clean up GPIO on exit
    GPIO.cleanup()