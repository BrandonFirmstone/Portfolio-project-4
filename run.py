import os
from flask import Flask, render_template


app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html")

@app.route("/about")
def about():
    return render_template("about-us.html")

@app.route("/contact")
def contact():
    return render_template("contact-us.html")

@app.route("/policies")
def policies():
    return render_template("our-policies.html")

@app.route("/drinks")
def drinks():
    return render_template("all-drinks.html")

if __name__ == "__main__":
    app.run(
        host=os.environ.get("IP", "0.0.0.0"),
        port=int(os.environ.get("PORT", "5000")),
        debug=True)
