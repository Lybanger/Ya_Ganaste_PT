import os
import time
import selenium.common.exceptions
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec


def driver():
    prefs = {
        "download.default_directory": r"C:\Users\chiefs\Downloads\Prueba tecnica\files",  # Directorio de descarga
        "download.directory_upgrade": True,  # Directorio predeterminado de descarga si el anterior no existe
    }
    chrome_options = Options()
    chrome_options.add_argument("--headless")  # Deshabilita la pantalla del navegador
    chrome_options.add_experimental_option('prefs', prefs)
    chrome_service = Service(
        executable_path=r"C:\Users\chiefs\Downloads\Prueba tecnica\CHROME\chromedriver.exe",
        service_args=['--disable-build-check']  # No toma en cuenta la versión del driver
    )

    drive = webdriver.Chrome(service=chrome_service, options=chrome_options)

    return drive


def downloads():
    d = driver()
    urls = [
        "https://github.com/AseguramientoYG/Prueba_tecnica/blob/main/CL_TRANSACCIONES_2022-02-26.csv",
        "https://github.com/AseguramientoYG/Prueba_tecnica/blob/main/SENCILLITO-20220226.xls",
        "https://github.com/AseguramientoYG/Prueba_tecnica/blob/main/Transbank%2026%20feb.csv"
    ]

    for url in urls:
        d.get(url)
        # Espera un máximo de 20 s hasta que aparece el texto "Prueba_tecnica" en la página
        WebDriverWait(d, 20).until(ec.presence_of_element_located((By.LINK_TEXT, "Prueba_tecnica")))
        try:
            d.find_element(By.XPATH, "//a[contains(.,'View raw')]").click()
        except selenium.common.NoSuchElementException:  # Transbank se descarga de otra forma
            d.find_element(By.XPATH, "//span[@data-component='text'][contains(.,'Raw')]").click()
        name = url.split('/')
        name_file = name[-1]  # Nos quedamos solo con el nombre del archivo
        if name_file == "Transbank%2026%20feb.csv":
            name_file = "Transbank 26 feb.csv"
        file = "C:\\Users\\chiefs\\Downloads\\Prueba tecnica\\FILES\\" + name_file
        WebDriverWait(d, 10).until(lambda x: os.path.exists(file))  # Esperamos a que el archivo se descargue


def conciliation():
    d = driver()

    d.get("https://github.com/AseguramientoYG/Prueba_tecnica/tree/main")
    # Espera un máximo de 20 s hasta que aparece el texto "Prueba_tecnica" en la página
    WebDriverWait(d, 20).until(ec.presence_of_element_located((By.LINK_TEXT, "Prueba_tecnica")))
    i = 1
    while i < 4:
        name_file = "(//td[contains(@colspan,'1')])[" + str(i) + "]"
        name = d.find_element(By.XPATH, name_file)
        if "CL_TRANSACCIONES" in name.text:
            url = "https://github.com/AseguramientoYG/Prueba_tecnica/blob/main/" + str(name.text)
            d.get(url)
            WebDriverWait(d, 20).until(ec.presence_of_element_located((By.LINK_TEXT, "Prueba_tecnica")))
            d.find_element(By.XPATH, "//a[contains(.,'View raw')]").click()
        elif "Transbank" in name.text:
            url = "https://github.com/AseguramientoYG/Prueba_tecnica/blob/main/" + str(name.text)
            d.get(url)
            WebDriverWait(d, 20).until(ec.presence_of_element_located((By.LINK_TEXT, "Prueba_tecnica")))
            d.find_element(By.XPATH, "//span[@data-component='text'][contains(.,'Raw')]").click()
        elif "SENCILLITO" in name.text:
            url = "https://github.com/AseguramientoYG/Prueba_tecnica/blob/main/" + str(name.text)
            d.get(url)
            WebDriverWait(d, 20).until(ec.presence_of_element_located((By.LINK_TEXT, "Prueba_tecnica")))
            d.find_element(By.XPATH, "//a[contains(.,'View raw')]").click()
        time.sleep(5)
        if i == 3:
            break
        d.get("https://github.com/AseguramientoYG/Prueba_tecnica/tree/main")
        time.sleep(5)
        WebDriverWait(d, 20).until(ec.presence_of_element_located((By.LINK_TEXT, "Prueba_tecnica")))
        i += 1
