import RPi.GPIO as GPIO
import time
import cv2

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

# Initialize OpenCV Video Capture
cap = cv2.VideoCapture(0)

# Function to control LEDs and buzzer based on detected trash type
def control_trash(trash_type):
    if trash_type == "recyclable":
        GPIO.output(blue_led_pin, GPIO.HIGH)
        for _ in range(3):
            GPIO.output(buzzer_pin, GPIO.HIGH)
            time.sleep(3)
            GPIO.output(buzzer_pin, GPIO.LOW)
            time.sleep(1)
        GPIO.output(blue_led_pin, GPIO.LOW)
        time.sleep(6)
    elif trash_type == "organic":
        GPIO.output(green_led_pin, GPIO.HIGH)
        for _ in range(2):
            GPIO.output(buzzer_pin, GPIO.HIGH)
            time.sleep(3)
            GPIO.output(buzzer_pin, GPIO.LOW)
            time.sleep(1)
        GPIO.output(green_led_pin, GPIO.LOW)
        time.sleep(3)
    elif trash_type == "general":
        GPIO.output(red_led_pin, GPIO.HIGH)
        GPIO.output(buzzer_pin, GPIO.HIGH)
        time.sleep(3)
        GPIO.output(buzzer_pin, GPIO.LOW)
        GPIO.output(red_led_pin, GPIO.LOW)
        time.sleep(3)

try:
    # Set ground pin to low (ground)
    GPIO.output(ground_pin, GPIO.LOW)

    # Check if camera is opened correctly
    if not cap.isOpened():
        raise Exception("Unable to access the camera.")

    # Run loop to capture frames from camera
    while True:
        ret, frame = cap.read()
        
        # Your code for trash detection and classification using OpenCV goes here
        # Assuming trash_type is detected and set accordingly
        # trash_type = detect_trash(frame)  # Replace this with actual detection function
        
        trash_type = "recyclable"  # Placeholder, replace with actual detection result
        
        # Control LEDs and buzzer based on detected trash type
        control_trash(trash_type)

except KeyboardInterrupt:
    # Clean up GPIO and release OpenCV resources on exit
    GPIO.cleanup()
    cap.release()
    cv2.destroyAllWindows()
except Exception as e:
    print("An error occurred:", e)
    # Clean up GPIO and release OpenCV resources in case of error
    GPIO.cleanup()
    cap.release()
    cv2.destroyAllWindows()