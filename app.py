import numpy as np
from operations import *
from random import choice
from dotenv import load_dotenv
from flask import Flask, request, Response

load_dotenv()
app = Flask(__name__)


@app.route("/")
def hello_world():
    return "Hello World!"


@app.route("/masqueico")
def masqueico():
    return choice(["Romildo", "Mariano"])


@app.route("/api/test", methods=["POST"])
def test():
    requested_image = request
    serialized_data = np.fromstring(requested_image.data, np.uint8)
    decoded_image = cv2.imdecode(serialized_data, cv2.IMREAD_COLOR)
    response = {
        "message": "image received - [{}]x[{}]".format(
            decoded_image.shape[1], decoded_image.shape[0]
        )
    }
    pickled_response = jsonpickle.encode(response)
    return Response(response=pickled_response, status=200, mimetype="application/json")


if __name__ == "__main__":
    app.run(port=5000)
