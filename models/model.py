import cv2
from joblib import dump, load
import numpy as np
from pathlib import Path


def load_models(
    models_path=[
        Path(
            r"C:\Users\eliab\Documents\projetao 2\cab.id\models\modelo._gender.hdf5"
        ),
        Path(
            r"C:\Users\eliab\Documents\projetao 2\cab.id\models\modelo_articleType.hdf5"
        ),
        Path(
            r"C:\Users\eliab\Documents\projetao 2\cab.id\models\modelo_baseColour.hdf5"
        ),
        Path(
            r"C:\Users\eliab\Documents\projetao 2\cab.id\models\modelo_masterCategory.hdf5"
        ),
        Path(
            r"C:\Users\eliab\Documents\projetao 2\cab.id\models\modelo_season.hdf5"
        ),
        Path(
            r"C:\Users\eliab\Documents\projetao 2\cab.id\models\modelo_subCategory.hdf5"
        ),
        Path(
            r"C:\Users\eliab\Documents\projetao 2\cab.id\models\modelo_usage.hdf5"
        ),
        Path(
            r"C:\Users\eliab\Documents\projetao 2\cab.id\models\modelo_year.hdf5"
        ),  
    ],
    descriptions = [
        { #gender
            0: "Boys", 1: "Girls", 2: "Men", 3: "Unisex", 4: "Women", 
        },
        { #articleType
            0: "Accessory Gift Set", 1: "Backpacks", 2: "Bangle", 3: "Belts", 4: "Blazers", 5: "Boxers", 6: "Bra", 7: "Bracelet", 8: "Briefs", 9: "Capris", 10: "Caps", 11: "Casual Shoes", 12: "Churidar", 13: "Clutches", 14: "Deodorant", 15: "Dresses", 16: "Duffel Bag", 17: "Dupatta", 18: "Earrings", 19: "Flats", 20: "Flip Flops", 21: "Formal Shoes", 22: "Fragrance Gift Set", 23: "Free Gifts", 24: "Gloves", 25: "Handbags", 26: "Headband", 27: "Heels", 28: "Innerwear Vests", 29: "Jackets", 30: "Jeans", 31: "Kurta Sets", 32: "Kurtas", 33: "Kurtis", 34: "Laptop Bag", 35: "Leggings", 36: "Lounge Pants", 37: "Lounge Shorts", 38: "Messenger Bag", 39: "Mobile Pouch", 40: "Mufflers", 41: "Necklace and Chains", 42: "Patiala", 43: "Pendant", 44: "Perfume and Body Mist", 45: "Sandals", 46: "Scarves", 47: "Shirts", 48: "Shorts", 49: "Skirts", 50: "Socks", 51: "Sports Sandals", 52: "Sports Shoes", 53: "Stockings", 54: "Sunglasses", 55: "Suspenders", 56: "Sweaters", 57: "Sweatshirts", 58: "Swimwear", 59: "Ties", 60: "Tights", 61: "Tops", 62: "Track Pants", 63: "Tracksuits", 64: "Travel Accessory", 65: "Trousers", 66: "Trunk", 67: "Tshirts", 68: "Tunics", 69: "Wallets", 70: "Watches", 71: "Water Bottle"
        },
        {  #baseColour
            0: "Beige", 1: "Black", 2: "Blue", 3: "Bronze", 4: "Brown", 5: "Burgundy", 6: "Charcoal", 7: "Coffee Brown", 8: "Copper", 9: "Cream", 10: "Gold", 11: "Green", 12: "Grey", 13: "Grey Melange", 14: "Khaki", 15: "Lavender", 16: "Magenta", 17: "Maroon", 18: "Metallic", 19: "Multi", 20: "Mustard", 21: "Navy Blue", 22: "Off White", 23: "Olive", 24: "Orange", 25: "Peach", 26: "Pink", 27: "Purple", 28: "Red", 29: "Rust", 30: "Silver", 31: "Skin", 32: "Steel", 33: "Tan", 34: "Taupe", 35: "Teal", 36: "Turquoise Blue", 37: "White", 38: "Yellow"
        },
        { #masterCategory
          0: "Accessories", 1: "Apparel", 2: "Footwear", 3: "Free Items", 4: "Personal Care"
        },
        { #season
            0: "Fall", 1: "Spring", 2: "Summer", 3: "Winter"
        },
        {  #subCategory
            0: "Accessories", 1: "Apparel Set", 2: "Bags", 3: "Belts", 4: "Bottomwear", 5: "Dress", 6: "Eyewear", 7: "Flip Flops", 8: "Fragrance", 9: "Free Gifts", 10: "Gloves", 11: "Headwear", 12: "Innerwear", 13: "Jewellery", 14: "Loungewear and Nightwear", 15: "Mufflers", 16: "Sandal", 17: "Scarves", 18: "Shoes", 19: "Socks", 20: "Ties", 21: "Topwear", 22: "Wallets", 23: "Watches", 24: "Water Bottle"
        },
        {  #usage
            0: "Casual", 1: "Ethnic", 2: "Formal", 3: "NA", 4: "Smart Casual", 5: "Sports", 
        },
        {  #year
            0: "2010", 1: "2011", 2: "2012", 3: "2013", 4: "2014", 5: "2015", 6: "2016", 7: "2017", 8: "2018", 
        }
    ]
):
    models = [load(open(models_path[0], "rb")), load(open(models_path[1], "rb")), load(open(models_path[2], "rb")), load(open(models_path[3], "rb")), load(open(models_path[4], "rb")), load(open(models_path[5], "rb")), load(open(models_path[6], "rb")), load(open(models_path[7], "rb"))]
     
    return descriptions, models


descriptions, models = load_models()


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


def run(path="C:/Users/eliab/Documents/projetao 2/cab.id/1.jpg", models=models):
    img = cv2.imread(path)
    img_processed = image_to_pixels(img)
    predicted = []
    for i in range(len(models)):
        num = models[i].predict(img_processed)
        print(num)
        print(descriptions[i])
        predicted.append(descriptions[i][num] )
    
    predicted = f"Labels for image {predicted}"
    return predicted


def main():
    run()


if __name__ == "__main__":
    main()
