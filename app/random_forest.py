from sklearn.ensemble import RandomForestRegressor
import pickle


def predict_location(input_data):
    with open('../model/rfmodel_1.pickle', 'rb') as f:
        rf = pickle.load(f)
    preds = rf.predict(input_data)
    print(preds)
    return preds
