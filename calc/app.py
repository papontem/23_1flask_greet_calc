# Put your app in here.
from flask import Flask, request
from operations import add, sub, mult, div
app = Flask(__name__)

OPERATIONS= { 
    "add"   :  add, 
    "sub"   :  sub, 
    "mult"  :  mult, 
    "div"   :  div
}

#get
@app.route('/<string:operation>', methods =["GET"])
def calc(operation):
    """Show the result of inputting desired a and b values into a selected operation"""

    # print(f"operation:{operation}  is a ", type(operation))
    if operation not in OPERATIONS:
        return "OPERATION NOT VALID"
    
    a = int(request.args["a"])
    b = int(request.args["b"])

    if operation == "add":
        result = add(a,b)
        return str(result)
    if operation == "sub":
        result = sub(a,b)
        return str(result)
    if operation == "mult":
        result = mult(a,b)
        return str(result)
    if operation == "div":
        result = div(a,b)
        return str(result)

# get all in one
@app.route('/math/<string:operation>', methods =["GET"])
def calc_all_in_one(operation):
    """Show the result of inputting desired a and b values into a selected operation"""

    # print(f"operation:{operation}  is a ", type(operation))
    if operation not in OPERATIONS:
        return "OPERATION NOT VALID"
    else:
        a = int(request.args["a"])
        b = int(request.args["b"])
        result = str(OPERATIONS[operation](a,b))
        return result


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

# Further Study

# You probably have a lot of code duplication in your calc routes, given that you’re doing such similar things in each.

# Make a single route/view function that can deal with 4 different kinds of URLs:

#     /math/add
#     /math/sub
#     /math/mult
#     /math/div

# You can write this in one function with one route by using a route parameter for the actual operation (“add”, “sub”, etc).

# As an extra-bonus, see if you can find a way to do this in the route without a whole series of if/elif statements. One good way is to use a dictionary to map operation names to the functions that do the underlying math.
