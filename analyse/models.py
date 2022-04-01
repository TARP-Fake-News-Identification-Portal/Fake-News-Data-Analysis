class NLPModel:
    """
    A class that helps use an NLP model by implementing a few major functions
    """

    def __init__(self, model_weights):
        self.model = self.load_model(model_weights)

    def load_model(self, model_weights):
        """
        Function to load the model from a serialized set of weights

        Args:
            model_weights (string): Path to the file containing serialized model weights

        Returns:
            model: A model with the required set of weights
        """
        model = None
        if model == None:
            raise NotImplementedError
        else:
            return model

    def preprocess(self, text):
        """
        Preprocessing function for the given model
        Args:
            text (string): The text input for the model

        Returns:
            processed_text: The processed text that can directly be fed into the model
        """
        print(text)
        processed_text = text.strip()
        if type(processed_text) == str:
            raise NotImplementedError
        else:
            return processed_text

    def predict(self, text):
        """
        Prediction function that predicts the target given a line of text

        Args:
            text (string): Input text for prediction

        Returns:
            prediction: The value the given Machine Learning model predicted
        """
        processed_text = self.preprocess(text)
        prediction = self.model.predict(processed_text)
        return prediction
