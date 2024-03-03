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
yellow_led_pin = 11
white_led_pin = 13

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
        print("Buzzer on")
        GPIO.output(blue_led_pin, GPIO.HIGH)
        print("Blue LED on")
        GPIO.output(green_led_pin, GPIO.HIGH)
        print("Green LED on")
        GPIO.output(red_led_pin, GPIO.HIGH)
        print("Red LED on")
        GPIO.output(yellow_led_pin, GPIO.HIGH)
        print("Yellow LED on")
        GPIO.output(white_led_pin, GPIO.HIGH)
        print("White LED on")
        time.sleep(5)

        GPIO.output(buzzer_pin, GPIO.LOW)
        print("Buzzer off")
        GPIO.output(blue_led_pin, GPIO.LOW)
        print("Blue LED off")
        GPIO.output(green_led_pin, GPIO.LOW)
        print("Green LED off")
        GPIO.output(red_led_pin, GPIO.LOW)
        print("Red LED off")
        GPIO.output(yellow_led_pin, GPIO.LOW)
        print("Yellow LED off")
        GPIO.output(white_led_pin, GPIO.LOW)
        print("White LED off")
        time.sleep(5)

except KeyboardInterrupt:
    # Clean up GPIO on exit
    GPIO.cleanup()