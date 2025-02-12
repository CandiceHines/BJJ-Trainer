# Handles preprocessing (resizing, normalization)
import tflite_runtime.interpreter as tflite  # Needed for running the exported model on the Raspberry Pi
import numpy as np
import cv2  # Used to load and preprocess images

class ImageProcessor:
    def __init__(self, model_path="/home/pi/Desktop/BJJ Trainer/bjj_trainer_backend/Trainer Model/model.tflite", labels_path="/home/pi/Desktop/BJJ Trainer/bjj_trainer_backend/Trainer Model/labels.txt"):
        # Load the TensorFlow Lite model
        self.interpreter = tflite.Interpreter(model_path=model_path)
        self.interpreter.allocate_tensors()

        # Load labels
        self.labels = self.load_labels(labels_path)

        # Get model input/output details
        self.input_details = self.interpreter.get_input_details()
        self.output_details = self.interpreter.get_output_details()

    def load_labels(self, path):
        """Loads labels from the label file."""
        with open(path, "r") as f:
            return [line.strip() for line in f.readlines()]

    def preprocess_image(self, image):
        """Preprocess an image (from path or live frame) for the model."""
        if isinstance(image, str):  # If it's a file path, load the image
            img = cv2.imread(image)
        else:  # If it's already an image array (live frame from camera)
            img = image

        img = cv2.resize(img, (224, 224))  # Resize to model input size
        img = img.astype(np.float32) / 255.0  # Normalize to [0,1] range
        img = np.expand_dims(img, axis=0)  # Add batch dimension
        return img

    def predict(self, image):
        """Runs inference on an image and returns the predicted label."""
        img = self.preprocess_image(image)  # Process the image

        # Set the input tensor
        self.interpreter.set_tensor(self.input_details[0]['index'], img)
        self.interpreter.invoke()  # Run inference

        # Get the output tensor
        output_data = self.interpreter.get_tensor(self.output_details[0]['index'])
        predicted_index = np.argmax(output_data)  # Get highest confidence index
        predicted_label = self.labels[predicted_index]
        confidence = output_data[0][predicted_index]

        return predicted_label, confidence


