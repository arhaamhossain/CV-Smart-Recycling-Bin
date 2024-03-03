from picamera import PiCamera
from time import sleep
import os

# Create a directory to save captured images if it doesn't exist
image_folder = "captured_images"
os.makedirs(image_folder, exist_ok=True)

# Initialize the PiCamera
camera = PiCamera()

# Define the key to start/stop capturing images
start_stop_key = 's'  # Change to the desired key code, 's' key by default
exit_key = 'q'  # Change to the desired exit key code, 'q' key by default

# Capture and save images
capturing = False
image_counter = 1  # Counter to keep track of captured images
while True:
    # Capture an image when the start_stop_key is pressed
    if input("Press '{}' to capture an image or '{}' to stop capturing: ".format(start_stop_key, exit_key)) == start_stop_key:
        capturing = True
    else:
        break

    # Capture an image
    if capturing:
        # Capture an image from the camera
        image_path = os.path.join(image_folder, f"captured_image_{image_counter}.jpg")
        camera.capture(image_path)
        print(f"Image {image_counter} captured successfully!")
        image_counter += 1

# Close the PiCamera
camera.close()
