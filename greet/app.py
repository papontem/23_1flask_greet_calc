from flask import Flask, request

app = Flask(__name__)

@app.route('/')
def homepage():
    """show homepage"""
    html = """
    """
    return html


# /welcome
#     Returns “welcome”
# /welcome/home
#     Returns “welcome home”
# /welcome/back
#     Return “welcome back” 