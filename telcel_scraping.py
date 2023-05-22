from bs4 import BeautifulSoup
from selenium import webdriver
import time
import requests

url = "https://www.telcel.com/personas/telefonia/amigo/paquetes-end/paquetes-amigo-sin-limite"
driver = webdriver.Chrome()
driver.get(url)
#waiting for the page to load
time.sleep(3)

page = driver.page_source
soup = BeautifulSoup(page, 'html.parser')
promos = soup.find_all('div', class_="telcel-tabla-dinamica-contenedor")

telcel_offer = []
for promo in promos:
    offer = promo.find_all('div', class_= "telcel-tabla-dinamica-item")
    option = []
    for o in offer:
        info = o.find('div', class_="telcel-tabla-dinamica-item-oferta")
        option.append(info.text)
    del option[1:3]
    print(option)
    print("*"*30)
    """    
        
    name = promo.select('p', class_="telcel-tabla-dinamica-titulo h1 mt-30")
    option.append(name[0].text)
    data = promo.find_next('div', class_="telcel-tabla-dinamica-item-oferta")
    option.append(data.text)
    sms = promo.find_next('div', class_="telcel-tabla-dinamica-item-oferta")
    minute = sms
    option.append(sms)
    days = promo.find_next('div', class_="telcel-tabla-dinamica-item gluo-item-completa")
    option.append(days.text)
    price = promo.find_next('div', class_="telcel-tabla-dinamica-item gluo-item-completa")
    option.append(price.text)
    print(option)
    """
