import pytest
from analyse import models, JoyModel


class Sample(models.NLPModel):
    def __init__(self, model_weights):
        super().__init__(model_weights)

    def load_model(self, model_weights):
        return super().load_model(model_weights)

    def preprocess(self, text):
        return super().preprocess(text)

    def predict(self, text):
        return super().predict(text)


def test_NLPModel_raises_NotImplementedError():
    with pytest.raises(NotImplementedError):
        model = models.NLPModel("./models/Best_Joy.sav")


def test_Sample_raises_NotImplementedError():
    with pytest.raises(NotImplementedError):
        model = Sample("./models/Best_Joy.sav")
