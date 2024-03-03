from picamera import PiCamera
from time import sleep
import os
from inference import get_model
import supervision as sv
from apikey import akey
# Create a directory to save captured images if it doesn't exist
image_folder = "captured_images"
os.makedirs(image_folder, exist_ok=True)

# Initialize the PiCamera
camera = PiCamera()

# Define the key to start/stop capturing images
start_stop_key = 's'  # Change to the desired key code, 's' key by default
exit_key = 'q'  # Change to the desired exit key code, 'q' key by default

# Load the pre-trained model
model = get_model(model_id="trash-detection-kcsnu/4", api_key=akey)

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

        # Load the captured image for inference
        image = sv.Scene.from_file(image_path)

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

        # Save the annotated image
        annotated_image_path = os.path.join(image_folder, f"annotated_image_{image_counter}.jpg")
        annotated_image.to_file(annotated_image_path)
        print(f"Annotated image {image_counter} saved successfully!")

        image_counter += 1

# Close the PiCamera
camera.close()
