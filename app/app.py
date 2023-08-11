from flask import Flask
from flask import request
from utils.utils import prepare_input
from src.random_forest import predict_location
app = Flask(__name__)

@app.route("/")
def index():
    return 'Index Page'

@app.route("/predict",methods=['GET'])
def predict():
    input_data = request.args.get("rssi")
    input_data = prepare_input(input_data=input_data)
    predicted_location = predict_location(input_data=input_data)
    return predicted_location

if __name__ == "__main__":
    app = create_app()
    app.run(debug=True)

