# Runs TensorFlow Lite model inference
import tensorflow.lite as tflite
import numpy as np
import cv2

class Classifier:
    def __init__(self, model_path="Trainer_Model/model.tflite", label_path="Trainer_Model/labels.txt", user_name="User", opponent_name="Opponent"):
        """Initialize the classifier, load model & labels."""
        self.interpreter = tflite.Interpreter(model_path=model_path)
        self.interpreter.allocate_tensors()
        self.input_details = self.interpreter.get_input_details()
        self.output_details = self.interpreter.get_output_details()
        self.labels = self.load_labels(label_path)

        self.user_name = user_name
        self.opponent_name = opponent_name

    def load_labels(self, label_path):
        """Load class labels from the labels.txt file."""
        with open(label_path, "r") as f:
            return [line.strip() for line in f.readlines()]

    def infer_opponent_move(self, user_label):
        """Infers the opponent's move based on the user's detected label."""
        if "Has" in user_label:
            return user_label.replace("Has", "In")
        elif "Applies" in user_label:
            return user_label.replace("Applies", "Defending")
        elif "In" in user_label:
            return user_label.replace("In", "Has")
        elif "Defending" in user_label:
            return user_label.replace("Defending", "Applies")
        return "Unknown"

    def classify_frame(self, frame):
        """Runs image classification and determines control status."""
        frame_resized = cv2.resize(frame, (224, 224))  # Resize for model input
        frame_normalized = frame_resized.astype(np.float32) / 255.0  # Normalize
        input_data = np.expand_dims(frame_normalized, axis=0)  # Add batch dimension

        self.interpreter.set_tensor(self.input_details[0]['index'], input_data)
        self.interpreter.invoke()
        output_data = self.interpreter.get_tensor(self.output_details[0]['index'])[0]

        top_index = np.argmax(output_data)
        confidence = output_data[top_index]
        user_label = self.labels[top_index]  # The model's direct classification

        # Infer the opponent's move from the user's classification
        opponent_label = self.infer_opponent_move(user_label)

        return {
            "user_label": user_label,
            "opponent_label": opponent_label,
            "confidence": confidence
        }

# Example Usage:
if __name__ == "__main__":
    classifier = Classifier(user_name="Candice", opponent_name="David")
    cap = cv2.VideoCapture(0)

    while True:
        ret, frame = cap.read()
        if not ret:
            break

        result = classifier.classify_frame(frame)
        print(result)  # Outputs user move, inferred opponent move, and confidence

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()



