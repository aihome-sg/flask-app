from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "Hello, my first real estate website!"

if __name__ == "__main__":
    app.run(debug=True)
