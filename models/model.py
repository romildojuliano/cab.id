import cv2
from joblib import dump, load
import numpy as np
from pathlib import Path


def load_models(
    models=[
        Path(
            r"C:\Users\eliab\Documents\projetao 2\cab.id\models\modelo._gender.hdf5"
        )
    ],
):
    new_gender_model = load(open(models[0], "rb"))
    return new_gender_model


gender_model = load_models()


def image_to_pixels(image):

    # Redimensionar a imagem
    image = cv2.resize(image, (165, 165))

    # Converter para um array numpy
    pixels = image.flatten()
    pixels_array = np.array(pixels)

    # normalizando os pixels para um intervalo (-1,1)
    normalized_pixels = cv2.normalize(
        np.array([pixels_array]), None, 0, 1.0, cv2.NORM_MINMAX, dtype=cv2.CV_32F
    )

    return normalized_pixels[0]


def run(path="C:/Users/eliab/Documents/projetao 2/cab.id/1.jpg", model=gender_model):
    img = cv2.imread(path)
    img_processed = image_to_pixels(img)
    predicted = model.predict([img_processed])
    predicted = f"O output foi: {predicted}"
    return predicted


def main():
    run()


if __name__ == "__main__":
    main()
