import numpy as np
from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello World!'

@app.route("/masqueico")
def masqueico():
    return np.random.choice(["Romildo", "Mariano"])

if __name__ == '__main__':
    app.run()