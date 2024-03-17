# %%
import os
import cv2
import jsonpickle

from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.remote import webelement
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import string
from functools import reduce
from collections import Counter

from os.path import abspath
from selenium.webdriver.support.ui import Select
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.webdriver import WebDriver

# %%
import nltk

nltk.download("words")

# %%
DEFAULT_DOWNLOAD_PATH = os.getcwd()


def create_driver():
    opts = webdriver.ChromeOptions()
    prefs = {
        "download.default_directory": os.path.join(os.getcwd(), DEFAULT_DOWNLOAD_PATH)
    }
    # Seta o user-agent do navegador
    opts.add_experimental_option("prefs", prefs)
    opts.add_argument(
        "user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36"
    )

    driver = webdriver.Chrome(
        service=Service(ChromeDriverManager().install()),
        options=opts,
    )
    driver.maximize_window()
    return driver


# %%
driver = create_driver()


# %%
def find_element_with_implicit_wait(
    by, value, driver: WebDriver = driver, timeout=20
) -> webelement:
    try:
        return WebDriverWait(driver, timeout).until(
            EC.presence_of_element_located((by, value))
        )
    except Exception as e:
        print(e.__class__, e.__repr__())
        return webelement()


# %%
def open_google_images_reverse_search(
    img_path,
    driver=driver,
    google_url="https://images.google.com.br/",
):
    # Abre a página inicial
    driver.get(google_url)

    # Botão de upload
    upload_button_classname = "nDcEnd"
    find_element_with_implicit_wait(By.CLASS_NAME, upload_button_classname).click()

    # Acha o elemento de upload
    upload_element_css_ref = "input[type='file']"
    upload_element = find_element_with_implicit_wait(
        By.CSS_SELECTOR, upload_element_css_ref
    )

    # PATH = r"C:\Users\ROMILDO\Desktop\dev\cab.id\cab.id 2.0\jeans_jacket.jpg"
    # Faz o upload da imagem
    upload_element.send_keys(img_path)

    XPATH = "/html/body/c-wiz/div/div[2]/div/c-wiz/div/div[2]"
    "/c-wiz/div/div/div/div[2]/div[1]/div/div/div"
    find_element_with_implicit_wait(By.XPATH, XPATH)

    XPATH = "/html/body/c-wiz/div/div[2]/div/c-wiz/div/div[2]"
    "/c-wiz/div/div/div/div[2]/div[1]/div/div/div/div[1]/div/div"
    return find_element_with_implicit_wait(By.XPATH, XPATH)


# %%
img_path = r"C:\Users\ROMILDO\Desktop\dev\cab.id\cab.id 2.0\jeans_jacket.jpg"
html_elements = open_google_images_reverse_search(img_path)

# %%
soup = BeautifulSoup(html_elements.get_property("innerHTML"), "html.parser")

# %%
filter_relevant_image_url = lambda url: url.startswith("https") and "favicon" not in url

for img in soup.findAll("img"):
    if filter_relevant_image_url(img["src"]):
        print(img["src"])

# %%
words = list({div.text for div in soup.findAll("div") if len(div.text) > 2})

# %%


s = string.ascii_uppercase

end = reduce(lambda a, b: a + b, [Counter(words[i].split()) for i in range(len(words))])

# %%
import re


def filtrar_chaves(dicionario):
    """
    Filtra as chaves de um dicionário, encontrando apenas chaves válidas que contêm apenas letras.

    Argumentos:
      dicionario: O dicionário a ser filtrado.

    Retorna:
      Um novo dicionário com as chaves inválidas removidas.
    """
    regex = re.compile(r"^[a-zA-Z]+$")
    max_val = max(dicionario.values())
    chaves_validas = {
        chave: valor / max_val
        for chave, valor in dicionario.items()
        if regex.match(chave) and len(chave) > 2
    }
    return chaves_validas


# %%
sorted(filtrar_chaves(end).items(), key=lambda x: x[1], reverse=True)[:15]


# %%
def extract_info_from_image(path, RANKING_RET: int = 20):
    html_elements = open_google_images_reverse_search(path)
    soup = BeautifulSoup(html_elements.get_property("innerHTML"), "html.parser")
    words = list({div.text for div in soup.findAll("div") if len(div.text) > 2})
    end = reduce(
        lambda a, b: a + b, [Counter(words[i].split()) for i in range(len(words))]
    )
    return sorted(filtrar_chaves(end).items(), key=lambda x: x[1], reverse=True)[
        :RANKING_RET
    ]


# %%
extract_info_from_image(
    r"C:\Users\ROMILDO\Desktop\dev\cab.id\clothing-dataset-small\train\shorts\74222128-e39b-4787-afb2-f88a92b8e537.jpg"
)

# %%
