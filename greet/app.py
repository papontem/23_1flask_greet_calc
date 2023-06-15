from flask import Flask, request

app = Flask(__name__)

@app.route('/')
def homepage():
    """show homepage"""
    html = """
    <h1>Home</h1>
    <p>This here is the home page, Welcome!</p>
    """
    return html

@app.route('/welcome')
def welcome():
    """show welcome message"""
    # html = """
    # <h1>Welcome</h1>
    # <p>
    #     Welcome to the Welcome page, Welcome! :D
    #     <br>
    #     i hope you like welcomes!
    # </p>
    # """
    html = """welcome"""
    return html

@app.route('/welcome/<type>')
def welcome_types(type):
    """Show welcome message depending on type"""
    if type.lower() == 'home':
        return "welcome home"
    elif type.lower() == 'back':
        return "welcome back"
    else:
        return """not a valid endpoint"""


# /welcome
#     Returns “welcome”
# /welcome/home
#     Returns “welcome home”
# /welcome/back
#     Return “welcome back” 