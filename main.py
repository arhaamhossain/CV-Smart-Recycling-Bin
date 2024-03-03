import cv2
from inference import get_model
import supervision as sv
import os
import serial
import time
from apikey import akey

# Create a directory to save captured images if it doesn't exist
image_folder = "captured_images"
os.makedirs(image_folder, exist_ok=True)

# Open the webcam
cap = cv2.VideoCapture(1)

# Load the pre-trained model
model = get_model(model_id="trash-detection-kcsnu/4", api_key=akey)
confidence_threshold = 0.5  # Adjust this value as needed

# Specify the port and baud rate for your Arduino
port = 'COM3'  # Adjust the port name accordingly
baud_rate = 9600

# Initialize serial communication with Arduino
arduino = serial.Serial(port, baud_rate)

# Check if the connection is successful
if arduino.is_open:
    print("Connected to Arduino!")
else:
    print("Failed to connect to Arduino.")

# Map classes to LED pins
class_to_led_command= {
    "paper": 'Y',     # Connect LED for "paper" class to pin 10 (yellow led)
    "plastic": 'G',   # Connect LED for "plastic" class to pin 9 (green led)
    "metal": 'B',     # Connect LED for "metal" class to pin 11 (blue led)
    "cardboard": 'W', # Connect LED for "cardboard" class to pin 7 (white led)
    "glass": 'R'      # Connect LED for "glass" class to pin 8 (red led)
}

# Variable to track whether to capture an image
capture_image = False

while True:
    # Capture a single frame
    ret, frame = cap.read()

    # Display the live webcam feed without annotations
    cv2.imshow("Live Webcam Feed", frame)

    # Read from the serial port to check if the button is pressed
    if arduino.in_waiting > 0:
        input_data = arduino.readline().decode().strip()
        if input_data == "SwitchPressed":
            print("Capturing image...")
            capture_image = True
            time.sleep(0.5)  # Add a small delay to avoid multiple captures for a single button press

    # Capture an image if the button is pressed
    if capture_image:
        # Define the path to save the captured image
        image_path = os.path.join(image_folder, "captured_image.jpg")

        # Save the captured image to the specified path
        cv2.imwrite(image_path, frame)

        # Load the captured image for inference
        image = cv2.imread(image_path)

        # Run inference on the captured image
        results = model.infer(image)
        print("Predictions:", results[0].predictions)

        # Extract class labels from the inference results
        labels = [p.class_name for p in results[0].predictions]
        confidences = [p.confidence for p in results[0].predictions]

        # Filter out detections below the confidence threshold
        valid_detections = [(label, confidence) for label, confidence in zip(labels, confidences) if confidence >= confidence_threshold]

        # Process only valid detections
        for label, confidence in valid_detections:
            if label in class_to_led_command:   
                led_command = class_to_led_command[label]
                arduino.write(led_command.encode())

        # Create supervision annotators
        bounding_box_annotator = sv.BoundingBoxAnnotator()
        label_annotator = sv.LabelAnnotator()

        # Load the results into the supervision Detections API
        detections = sv.Detections.from_inference(results[0].dict(by_alias=True, exclude_none=True))

        # Annotate the image with the inference results including labels
        annotated_image = bounding_box_annotator.annotate(scene=image, detections=detections)
        annotated_image = label_annotator.annotate(scene=annotated_image, detections=detections, labels=labels)

        # Display the annotated image
        cv2.imshow("Captured Image with Detections", annotated_image)

        # Reset capture_image flag
        capture_image = False

    # Exit the loop if 'q' key is pressed
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the webcam and close OpenCV windows
cap.release()
cv2.destroyAllWindows()
