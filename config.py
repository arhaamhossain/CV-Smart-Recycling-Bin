import RPi.GPIO as GPIO
import time

# Set pin numbering mode
GPIO.setmode(GPIO.BCM)

# Define pin numbers
ground_pin = 6
buzzer_pin = 12
blue_led_pin = 16
green_led_pin = 18
red_led_pin = 22

# Configure pins
GPIO.setup(ground_pin, GPIO.OUT)
GPIO.setup(buzzer_pin, GPIO.OUT)
GPIO.setup(blue_led_pin, GPIO.OUT)
GPIO.setup(green_led_pin, GPIO.OUT)
GPIO.setup(red_led_pin, GPIO.OUT)

try:
    # Set ground pin to low (ground)
    GPIO.output(ground_pin, GPIO.LOW)

    # Blink the LEDs and sound the buzzer
    while True:
        GPIO.output(buzzer_pin, GPIO.HIGH)
        print("Buzzer on")
        GPIO.output(blue_led_pin, GPIO.HIGH)
        print("Blue LED on")
        GPIO.output(green_led_pin, GPIO.HIGH)
        print("Green LED on")
        GPIO.output(red_led_pin, GPIO.HIGH)
        print("Red LED on")
        time.sleep(1)

        GPIO.output(buzzer_pin, GPIO.LOW)
        print("Buzzer off")
        GPIO.output(blue_led_pin, GPIO.LOW)
        print("Blue LED off")
        GPIO.output(green_led_pin, GPIO.LOW)
        print("Green LED off")
        GPIO.output(red_led_pin, GPIO.LOW)
        print("Red LED off")
        time.sleep(1)

except KeyboardInterrupt:
    # Clean up GPIO on exit
    GPIO.cleanup()