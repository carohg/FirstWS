from selenium import webdriver
from bs4 import BeautifulSoup
import time
import pandas as pd
import requests

url = 'https://www.movistar.com.mx/productos-y-servicios/prepago'

#creating the web driver
driver = webdriver.Chrome()

driver.get(url)

#waiting for the page to load
time.sleep(3)

page = driver.page_source
soup = BeautifulSoup(page, 'html.parser')
promos_clean = soup.select('div.parrilla.slick-slide, div.parrilla.slick-slide.slick-current.slick-active, div.parrilla.slick-slide.slick-active')
#print(promos_clean)

movistar = [
    ["Compañía", "Nombre", "Vigencia", "Precio", "MB Libres", "Minutos", "SMS"]
]
for promo in promos_clean:
    item = ['MOVISTAR','Recarga']
    duration = promo.select_one('.footer-parrilla center-align p')
    print(duration)
    item.append(duration)
    price = promo.select_one('.header-parrilla center-align menor-100 p')
    print(price)
    item.append(price)
    free_data = promo.select_one('.col s6 borde-derecho borde-abajo h4')
    print(free_data)
    item.append(free_data)
    """
    social_media
    video
    """
    minute = sms = promo.select_one('.minySms').text.strip()
    item.append(minute)
    item.append(sms)
    """WA"""
    movistar.append(item)
    print("*"*30)
df = pd.DataFrame(movistar)
print(df)