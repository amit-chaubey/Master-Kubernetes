from flask import Flask
import os

app = Flask(__name__)

@app.route('/')
def home():
    message = os.getenv("MESSAGE_APP", "Hello, K8s!")
    return message

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
