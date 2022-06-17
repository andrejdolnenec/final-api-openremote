from flask import Flask, request, jsonify
import json

app = Flask(__name__)

data =  json.load(open('data.json'))

@app.route('/get/', methods=['GET'])
def respond():

    price = request.args.get("price", None)
    squareMeters = request.args.get("squareMeters", None)

    # For debugging
    print(f"Received: {price}")
    print(f"Received: {squareMeters}")

    response = {}

    # Check if the user sent a name at all
    if not price:
        response["All Properies"] = " This response will Include All the available realastate properties from the database."
    else:
        response["Selected Properies"] = "This response includes the realastate properties acording to the request argument PRICE and SQUAREMETERES"
    return jsonify(response)


@app.route('/')
def index():
    # A welcome message to test our server
    return "<h1>Welcome to our medium-greeting-api!</h1>"


if __name__ == '__main__':
    # Threaded option to enable multiple instances for multiple user access support
    app.run(threaded=True, port=5000)
