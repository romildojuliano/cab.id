from flask import Flask, request
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

@app.route("/image_to_labels", methods=['POST'])
def image_to_labels():
    image = request.files['image']
    print("1")
    #image.save('src/cab.id/buscas/' + image.filename)
    print("2")
    #path = "src/cab.id/buscas/" + image.filename
   
    print("entrando na chamada")
    return model.run(image, descriptions, models)


@app.route("/image_to_images", methods=['POST'])
def image_to_images():
    image = request.files['image']
    image.save('https://cab-id-it6v.onrender.com/cab.id/buscas/' + image.filename)
    print("salvo")
    path = "https://cab-id-it6v.onrender.com/cab.id/buscas/" + image.filename
    return model.image_to_images(cluster, path, descriptions, models)


if __name__ == "__main__":
    cluster = model.load_cluster()
    descriptions, models = model.load_models()
    app.run(port=5000)
