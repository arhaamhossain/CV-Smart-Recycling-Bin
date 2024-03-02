import time
import picamera

def capture_image():
    try:
        with picamera.PiCamera() as camera:
            # Adjust camera settings if needed
            # camera.resolution = (width, height)
            # camera.rotation = rotation_angle
            
            # Wait for the camera to warm up
            time.sleep(2)
            
            # Capture an image
            camera.capture('garbage_image.jpg')
            print("Image captured successfully!")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    capture_image()
