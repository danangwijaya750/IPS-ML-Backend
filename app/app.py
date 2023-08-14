from flask import Flask
from flask import request
from utils import prepare_input
from random_forest import predict_location

app = Flask(__name__)

@app.route("/")
def index():
    """
    This route displays an index page.
    """
    return 'Index Page'

@app.route("/predict", methods=['GET'])
def predict():
    """
    Endpoint for predicting location using a trained random forest model.
    Get the input RSSI data from the request. 
    For the example of request data please check input_example.txt.

    Returns:
        str: The predicted location based on the input RSSI data.
    """
    input_data = request.args.get("rssi")  # Get the input RSSI data from the request
    input_data = prepare_input(input_data=input_data)  # Prepare the input data
    predicted_location = predict_location(input_data=input_data)  # Make a prediction using the model
    return predicted_location

if __name__ == "__main__":
    app.run(debug=True)