from flask import Flask, request, jsonify
import json

app = Flask(__name__)

data =  json.load(open('data.json'))

@app.route('/get/', methods=['GET'])
def respond():

    priceFrom = request.args.get("priceFrom", None)
    priceTo = request.args.get("priceTo", None)
    squareMetersFrom = request.args.get("squareMetersFrom", None)
    squareMetersTo = request.args.get("squareMetersTo", None)

    # For debugging
    print(f"Received: {priceFrom}")
    print(f"Received: {priceTo}")
    print(f"Received: {squareMetersFrom}")
    print(f"Received: {squareMetersTo}")
    

    response = {}

    # Check if the user sent a name at all
    if not priceFrom and not priceTo and not squareMetersFrom and not squareMetersTo:
        response["All Properies"] = " This response will Include All the available realastate properties from the database."
    else:
        response["Selected Properies"] = "This response includes the realastate properties acording to the request argument PRICE and SQUAREMETERES"
        
        # the code below is not implemented becouse the concection to the database canot be established. 
        


    return jsonify(response)


@app.route('/')
def index():
    # A welcome message to test our server
    return "<h1>Welcome to our medium-greeting-api!</h1>"


if __name__ == '__main__':
    # Threaded option to enable multiple instances for multiple user access support
    app.run(threaded=True, port=5000)
