# Stores all classification labels
class Labels:
    def __init__(self, labels_path="Trainer Model/labels.txt"):
        self.labels = self.load_labels(labels_path)

    def load_labels(self, path):
        """Loads labels from the labels.txt file"""
        with open(path, "r") as f:
            return [line.strip() for line in f.readlines()]

    def get_label(self, index):
        """Returns the label name for a given index"""
        if 0 <= index < len(self.labels):
            return self.labels[index]
        return "Unknown"

# Example Usage
if __name__ == "__main__":
    label_manager = Labels()
    print(label_manager.labels)  # Print all labels
    print(label_manager.get_label(2))  # Example: Get label for index 2
