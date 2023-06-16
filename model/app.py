from flask import Flask, request, jsonify
from flask_cors import CORS
import tensorflow as tf

headers = {
    "Content-Type": "application/json"
}

app = Flask(__name__)
CORS(app)

model = tf.keras.models.load_model('model.h5')

@app.route('/', methods=['GET'])
def home():
    return "API is running!"

@app.route('/predict', methods=['POST'])
def predict():
    # Get the input data from the request
    data = request.get_json()

    # Perform any necessary preprocessing on the data
    data_predict = int(data["data"])

    # Make predictions using the loaded model
    predictions = model.predict([[data_predict]])
    print(predictions)

    # Perform any necessary postprocessing on the predictions
    # ...

    # Create a dictionary to hold the response
    response = {
        "predictions": predictions.item()
    }

    # Return the predictions as a JSON response with the specified headers
    return jsonify(response), 200, headers


@app.errorhandler(404)
def handle_invalid_route(e):
    return 'Invalid API Request', 404

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
