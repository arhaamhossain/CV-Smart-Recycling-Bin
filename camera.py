import picamera
import cv2

def initialize_camera():
    # Initialize Pi camera
    camera = picamera.PiCamera()
    camera.resolution = (640, 480)  # Set resolution (adjust as needed)
    camera.framerate = 30  # Set framerate (adjust as needed)
    # Additional camera settings can be configured here
    
    return camera

def stream_video(camera):
    # Create OpenCV window
    cv2.namedWindow('Real-Time Video', cv2.WINDOW_NORMAL)
    
    try:
        # Continuously capture and display video stream
        for frame in camera.capture_continuous(rawCapture, format="bgr", use_video_port=True):
            # Extract the raw NumPy array representing the image
            image = frame.array
            
            # Display the frame
            cv2.imshow('Real-Time Video', image)
            
            # Check for 'q' key to exit loop
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break
            
            # Clear the stream in preparation for the next frame
            rawCapture.truncate(0)
    finally:
        # Close OpenCV window
        cv2.destroy
