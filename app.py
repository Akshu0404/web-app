from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "Jenkins CI/CD Project Running!"

if __name__ == "__main__":
    app.run(port=5000)