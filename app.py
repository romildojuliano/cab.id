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

@app.route("/image_to_labels")
def image_to_labels():
    #para o futuro
    #image = request.files['image']
    #image.save('buscas/' + image.filename)
    #path = "buscas/" + image.filename
    print("entrando na chamada")
    return model.run("C:/Users/eliab/Documents/projetao 2/cab.id/1.jpg", descriptions, models)


@app.route("/image_to_images", methods=['POST'])
def image_to_images():
    return 

if __name__ == "__main__":
    #cluster = model.load_cluster()
    descriptions, models = model.load_models()
    app.run(port=5000)
