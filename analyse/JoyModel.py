import pickle
from .models import NLPModel


class JoyModel(NLPModel):
    def __init__(self, model_weights):
        super().__init__(model_weights)

    def preprocess(self, text):
        """
        Preprocessing function for the given model
        Args:
            text (string): The text input for the model

        Returns:
            processed_text: The processed text that can directly be fed into the model
        """
        processed_text = [text]
        return processed_text

    def predict(self, text):
        """
        Prediction function that predicts the target given a line of text

        Args:
            text (string): Input text for prediction

        Returns:
            prediction: The value the given Machine Learning model predicted
        """
        prediction = super().predict(text)
        return prediction[0]

    def load_model(self, model_weights):
        """
        Function to load the model from a serialized set of weights

        Args:
            model_weights (string): Path to the file containing serialized model weights

        Returns:
            model: A model with the required set of weights
        """
        model = pickle.load(open(model_weights, "rb"))
        return model
