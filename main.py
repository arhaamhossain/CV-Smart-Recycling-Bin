import cv2
import subprocess
from configcv import *
# Define the command to start the inference server
start_server_cmd = "inference server start"

# Start the inference server
subprocess.run(start_server_cmd, shell=True)

# Initialize the camera
cap = cv2.VideoCapture(0)  # Use the default camera (index 0)

# Loop to continuously capture frames and run inference
while True:
    # Capture frame-by-frame
    ret, frame = cap.read()

    if ret:
        # Run inference on the captured frame
        inference_cmd = f"inference infer {frame} --api-key N6e65K6iVSSQWe5WxUJo --project-id trash-detection-kcsnu --model-version 4"
        subprocess.run(inference_cmd, shell=True)
        
        # Display the frame
        cv2.imshow('Camera', frame)

        # Check for 'q' key to quit
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    else:
        print("Error: Unable to capture frame.")
        break

# Release the camera and close all OpenCV windows
cap.release()
cv2.destroyAllWindows()
