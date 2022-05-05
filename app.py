import imp
from flask import Flask, request, render_template

app = Flask(__name__)
@app.route("/hello")
def hello():
    return "<h1 style='color #ff0000; text-aligh: center;'>Hello from Flask!</h1>"

#http://127.0.0.1:5000/test?v1=hello
@app.route("/test")
def test_page():
    var_1 = request.args.get("v1")
    var_2 = request.args.get("v2")
    return f"""
    <h3>Test</h3>
    <p> Var 1 = {var_1} </p>
    <p> Var 2 = {var_2} </p>
    """
@app.route("/")
def home():
    return render_template("index.html")

app.run(debug=True)