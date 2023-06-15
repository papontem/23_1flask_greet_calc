# Put your app in here.
from flask import Flask, request
from operations import add, sub, mult, div
app = Flask(__name__)

METHODS= [ "add", "sub", "mult", "div" ]

@app.route('/<string:method>')
def find_post(method):
    """Show the result of inputting desired a and b values into a selected method"""

    # print(f"method:{method}  is a ", type(method))
    if method not in METHODS:
        return "METHOD NOT VALID"
    
    a = int(request.args["a"])
    b = int(request.args["b"])

    if method == "add":
        result = add(a,b)
        return str(result)
    if method == "sub":
        result = sub(a,b)
        return str(result)
    if method == "mult":
        result = mult(a,b)
        return str(result)
    if method == "div":
        result = div(a,b)
        return str(result)



# Make a Flask app that responds to 4 different routes. Each route does a math operation with two numbers, a and b, which will be passed in as URL GET-style query parameters.

# /add
#     Adds a and b and returns result as the body.
# /sub
#     Same, subtracting b from a.
# /mult
#     Same, multiplying a and b.
# /div
#     Same, dividing a by b.

# For example, a URL like http://localhost:5000/add?a=10&b=20 should return a string response of exactly 30.