# picamera.py
import cv2
from picamera import PiCamera
from picamera.array import PiRGBArray
import time

class PiCameraWrapper:
    def __init__(self):
        self.camera = PiCamera()
        self.camera.resolution = (640, 480)  # Set camera resolution
        self.raw_capture = PiRGBArray(self.camera, size=(640, 480))
        time.sleep(0.1)  # Allow camera to warm up
    
    def capture_frame(self):
        self.camera.capture(self.raw_capture, format="bgr")
        image = self.raw_capture.array
        self.raw_capture.truncate(0)  # Clear the stream
        return image
    
    def close(self):
        self.camera.close()
