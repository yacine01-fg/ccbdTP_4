from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return """
    <h1>Cloud Computing Lab - PaaS - Version 2.1</h1>
    <p>This application is deployed using a Platform as a Service.</p>
    """

if __name__ == "__main__":
    app.run(debug=True)
