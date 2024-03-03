import cv2
from inference_sdk import InferenceHTTPClient

# Initialize the InferenceHTTPClient
CLIENT = InferenceHTTPClient(
    api_url="https://detect.roboflow.com",
    api_key="N6e65K6iVSSQWe5WxUJo"
)

# Open the camera
cap = cv2.VideoCapture(0)

while True:
    # Read frame from the camera
    ret, frame = cap.read()

    # Check if frame is successfully captured
    if not ret:
        break

    # Perform inference on the frame
    result = CLIENT.infer(frame, model_id="trash-detection-kcsnu/4")

    # Parse the inference result
    detections = result.get("detections", [])

    # Draw bounding boxes and labels on the frame
    for detection in detections:
        label = detection["label"]
        confidence = detection["confidence"]
        box = detection["box"]
        x1, y1, x2, y2 = box

        # Draw bounding box
        cv2.rectangle(frame, (int(x1), int(y1)), (int(x2), int(y2)), (0, 255, 0), 2)

        # Draw label
        cv2.putText(frame, f'{label}: {confidence:.2f}', (int(x1), int(y1) - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)

    # Display the frame with detections
    cv2.imshow('frame', frame)

    # Exit the loop if 'q' is pressed
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the camera and close any open windows
cap.release()
cv2.destroyAllWindows()
