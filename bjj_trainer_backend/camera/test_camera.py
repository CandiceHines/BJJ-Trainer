import cv2
from image_processor import ImageProcessor  # Import your model class

class CameraHandler:
    def __init__(self, camera_id=0):
        self.camera_id = camera_id
        self.cap = cv2.VideoCapture(camera_id)

        if not self.cap.isOpened():
            print("Error: Camera not detected!")
            exit(1)

    def capture_frame(self):
        """Captures a frame from the camera and returns it."""
        ret, frame = self.cap.read()
        if not ret:
            print("Failed to capture frame")
            return None
        return frame

    def release(self):
        """Releases the camera."""
        self.cap.release()
        cv2.destroyAllWindows()

def main():
    camera = CameraHandler()
    model = ImageProcessor()  # Load your model

    print("Press 'q' to exit.")

    while True:
        frame = camera.capture_frame()
        if frame is None:
            continue

        # Process the frame with your model
        predicted_label, confidence = model.predict(frame)

        # Display the frame with the prediction
        cv2.putText(frame, f"{predicted_label} ({confidence:.2f})", (10, 40),
                    cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
        cv2.imshow("BJJ Trainer Camera Feed", frame)

        # Print the result to the terminal
        print(f"Prediction: {predicted_label}, Confidence: {confidence:.2f}")

        # Break loop if 'q' is pressed
        if cv2.waitKey(1) & 0xFF == ord("q"):
            break

    camera.release()

if __name__ == "__main__":
    main()


