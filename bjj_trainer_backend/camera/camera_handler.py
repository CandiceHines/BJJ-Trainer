# Handles image capture from Pi camera
import cv2
import os
from datetime import datetime

class CameraHandler:
    def __init__(self, camera_id=0, save_dir="captures"):
        self.camera_id = camera_id
        self.cap = cv2.VideoCapture(camera_id)
        os.makedirs(save_dir, exist_ok=True)
        self.save_dir = save_dir

    def capture_image(self):
        """Captures an image from the Pi Camera and saves it."""
        ret, frame = self.cap.read()
        if not ret:
            print("Failed to capture image")
            return None

        filename = os.path.join(self.save_dir, f"frame_{datetime.now().strftime('%Y%m%d_%H%M%S')}.jpg")
        cv2.imwrite(filename, frame)
        return filename  # Return the path of the saved image

    def release(self):
        """Releases the camera."""
        self.cap.release()

