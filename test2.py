import cv2
from inference import get_model
import supervision as sv
import os

# Create a directory to save captured images if it doesn't exist
image_folder = "captured_images"
os.makedirs(image_folder, exist_ok=True)

# Open the webcam
cap = cv2.VideoCapture(0)

# Define the key to start/stop capturing images
start_stop_key = ord('s')  # Change to the desired key code, 's' key by default
exit_key = ord('q')  # Change to the desired exit key code, 'q' key by default

# Define the number of images to capture

capturing = False
while True:
    # Capture a single frame
    ret, frame = cap.read()

    # Display the live webcam feed
    cv2.imshow("Live Webcam Feed", frame)

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
        for i in range(1):
            # Define the path to save the captured image
            image_path = os.path.join(image_folder, f"captured_image_{i}.jpg")

            # Save the captured image to the specified path
            cv2.imwrite(image_path, frame)

            # Load the captured image for inference
            image = cv2.imread(image_path)

            # Load the pre-trained model
            model = get_model(model_id="trash-detection-kcsnu/4", api_key="N6e65K6iVSSQWe5WxUJo")

            # Run inference on the captured image
            results = model.infer(image)

            # Create supervision annotators
            bounding_box_annotator = sv.BoundingBoxAnnotator()
            label_annotator = sv.LabelAnnotator()

            # Load the results into the supervision Detections API
            detections = sv.Detections.from_inference(results[0].dict(by_alias=True, exclude_none=True))

            # Annotate the image with the inference results
            annotated_image = bounding_box_annotator.annotate(scene=image, detections=detections)
            annotated_image = label_annotator.annotate(scene=annotated_image, detections=detections)

            # Display the annotated image
            cv2.imshow(f"Captured Image {i+1} with Detections", annotated_image)
            cv2.waitKey(0)
            cv2.destroyAllWindows()

    # Exit the loop if the exit_key is pressed
    if key == exit_key:
        cap.release()
        cv2.destroyAllWindows()
        break
cap.release()
cv2.destroyAllWindows()

