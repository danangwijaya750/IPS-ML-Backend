from sklearn.ensemble import RandomForestRegressor
import pickle

def predict_location(input_data):
    """
    Predicts a location using a trained RandomForestRegressor model.

    Args:
        input_data (array-like): Input data for prediction.

    Returns:
        array-like: Predicted location based on the input data.
    """
    with open('../model/rfmodel_1.pickle', 'rb') as f:
        rf = pickle.load(f)  # Load the trained RandomForestRegressor model
    preds = rf.predict(input_data)  # Make predictions using the loaded model
    print(preds)  # Print the predictions (for debugging or logging)
    return preds
