import pickle

def predictor(text):
    model = pickle.load(open('./models/Best_Joy.sav', 'rb'))
    prediction = model.predict([text])

    return prediction[0]

