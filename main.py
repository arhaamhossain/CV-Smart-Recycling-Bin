import cv2
from ultralytics import YOLO

# Load a pretrained YOLOv8n model
model = YOLO('yolov8n.pt')

# Initialize the video capture object for the laptop camera
cap = cv2.VideoCapture(0)  # Use 0 for the default camera

# Check if the camera opened successfully
if not cap.isOpened():
    print("Error: Unable to open the camera.")
    exit()

# Main loop to capture frames from the camera and perform inference
while True:
    # Capture frame-by-frame
    ret, frame = cap.read()

    # Check if the frame was captured successfully
    if not ret:
        print("Error: Unable to capture frame.")
        break

    # Run inference on the frame using the YOLOv8n model
    results = model(frame)  # list of Results objects

    # Render the results on the frame
    annotated_frame = results.render()

    # Display the annotated frame
    cv2.imshow('YOLOv8n Object Detection', annotated_frame, device = 'cpu')

    # Check for the 'q' key to quit
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the camera and close all OpenCV windows
cap.release()
cv2.destroyAllWindows()
