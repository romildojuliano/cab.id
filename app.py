from flask import Flask
from models import model
from random import choice
#from dotenv import load_dotenv

#load_dotenv()
app = Flask(__name__)


@app.route("/")
def hello_world():
    return "Hello World!"


@app.route("/masqueico")
def masqueico():
    return choice(["Romildo", "Mariano"])

@app.route("/testeia")
def testeia():
    return model.run()


if __name__ == "__main__":
    app.run(port=5000)
