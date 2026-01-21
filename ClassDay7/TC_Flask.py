from flask import Flask
app = Flask(__name__)

@app.route("/")
def home():
    return "welcome to Flask API"


if __name__ == "__main__":

    app.run(debug=True)
