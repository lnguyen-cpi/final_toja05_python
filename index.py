import os

from flask import Flask
app = Flask(__name__)

APP_VERSION = os.environ.get("APP_VERSION", default="None")
APP_HOST = os.environ.get("APP_HOST", default="None")

@app.route("/")
def hello():
    return f"http://{APP_HOST}:5000 -> Hello Python - {APP_VERSION} - {APP_HOST}, build Python"
  
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int("5000"), debug=True)
