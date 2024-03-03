import cv2
import os

# Create a directory to save captured images if it doesn't exist
image_folder = "captured_images"
os.makedirs(image_folder, exist_ok=True)

# Initialize the Pi camera
camera = cv2.VideoCapture(0)

# Set camera resolution (optional)
camera.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
camera.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)

# Define the key to start/stop capturing images
start_stop_key = ord('s')  # Change to the desired key code, 's' key by default
exit_key = ord('q')  # Change to the desired exit key code, 'q' key by default

# Define the number of images to capture
num_images = 1

capturing = False
image_count = 0
while True:
    # Capture a single frame from the camera
    ret, frame = camera.read()

    # Display the live camera feed
    cv2.imshow("Live Camera Feed", frame)

    key = cv2.waitKey(1) & 0xFF
    
    # Start/Stop capturing images when the start_stop_key is pressed
    if key == start_stop_key:
        capturing = not capturing
        if capturing:
            print("Capturing started. Press 's' to stop.")
        else:
            print("Capturing stopped. Press 's' to start again.")
    
    # Capture images when capturing is enabled
    if capturing:
        if image_count < num_images:
            # Define the path to save the captured image
            image_path = os.path.join(image_folder, f"captured_image_{image_count}.jpg")

            # Save the captured image to the specified path
            cv2.imwrite(image_path, frame)
            
            print(f"Image {image_count + 1} captured and saved as {image_path}")
            image_count += 1
        else:
            print("Capturing completed.")
            capturing = False

    # Exit the loop if the exit_key is pressed
    if key == exit_key:
        break

# Release the camera and close any open windows
camera.release()
cv2.destroyAllWindows()
