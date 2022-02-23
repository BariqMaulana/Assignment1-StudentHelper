from flask import Flask, render_template, request, jsonify
import math


app = Flask(__name__)


@app.route('/')
def index():
    return render_template("index.html")


@app.route('/hypotenuse', methods=['POST', 'GET'])
def hypotenuse():
    if request.method == 'GET':
        return render_template("hypotenuse.html")
    else:
        response = {}
        data = request.get_json()
        if data.get("number1", "number2"):
           number1 = int(data["number1"])
           number2 = int(data["number2"])
           response = {"status": 200, "result": math.hypot(number1, number2)}
        else:
           response = {"status": 500, "result": "Error"}
        return jsonify(response)


@app.route('/squareroot', methods=['POST', 'GET'])
def squareRoot():
    if request.method == 'GET':
        return render_template("squareRoot.html")
    else:
        response = {}
        data = request.get_json()
        if data.get("number"):
           number = int(data["number"])
           response = {"status": 200, "result": math.sqrt(number)}
        else:
           response = {"status": 500, "result": "Error"}
        return jsonify(response)


@app.route('/gpaconverter', methods=['POST', 'GET'])
def gpaConverter():
    if request.method == 'GET':
        return render_template("gpaConverter.html")
    else:
        response = {}
        data = request.get_json()
        if data.get("number"):
            number = int(data["number"])
            if number <= 100 and number >= 85:
                response = {"status": 200, "result": "A"}
            elif number <= 84.9 and number >= 80:
                response = {"status": 200, "result": "A-"}
            elif number <= 79.9 and number >= 75:
                response = {"status": 200, "result": "B+"}
            elif number <= 74.9 and number >= 70:
                response = {"status": 200, "result": "B"}
            elif number <= 69.9 and number >= 67:
                response = {"status": 200, "result": "B-"}
            elif number <= 66.9 and number >= 64:
                response = {"status": 200, "result": "C+"}
            elif number <= 63.9 and number >= 60:
                response = {"status": 200, "result": "C"}
            elif number <= 59.9 and number >= 55:
                response = {"status": 200, "result": "D"}
            else:
                response = {"status": 200, "result": "FAIL"}
        else:
           response = {"status": 500, "result": "Error"}
        return jsonify(response)




if  __name__ == '__main__':
    app.run(debug=True)



