import pickle
from sklearn.tree import DecisionTreeClassifier

class AIModel:
    def __init__(self):
        # Initialize the model (e.g., Decision Tree Classifier)
        self.model = DecisionTreeClassifier()

    def train(self, data):
        """
        Train the model with the provided data.
        :param data: A tuple (X_train, y_train) where X_train is the feature matrix
                     and y_train is the target vector.
        """
        X_train, y_train = data
        self.model.fit(X_train, y_train)
        print("Model training completed.")

    def predict(self, input_data):
        """
        Predict using the trained model.
        :param input_data: Feature matrix for prediction.
        :return: Predicted labels.
        """
        predictions = self.model.predict(input_data)
        return predictions

    def evaluate(self, test_data):
        """
        Evaluate the model on test data.
        :param test_data: A tuple (X_test, y_test) where X_test is the feature matrix
                          and y_test is the target vector.
        :return: Accuracy score.
        """
        X_test, y_test = test_data
        accuracy = self.model.score(X_test, y_test)
        print(f"Model accuracy: {accuracy}")
        return accuracy

    def save_model(self, file_path):
        """
        Save the trained model to a file.
        :param file_path: Path to save the model.
        """
        with open(file_path, 'wb') as file:
            pickle.dump(self.model, file)
        print(f"Model saved to {file_path}.")

    def load_model(self, file_path):
        """
        Load a trained model from a file.
        :param file_path: Path to the saved model file.
        """
        with open(file_path, 'rb') as file:
            self.model = pickle.load(file)
        print(f"Model loaded from {file_path}.")