import csv
import mysql.connector
import requests
from bs4 import BeautifulSoup
import pandas as pd

url = 'https://www.promociones-att.com.mx/mas/?utm_campaign_dom=0101020304&gad=1&gclid=CjwKCAjwuqiiBhBtEiwATgvixCQJzuAniyG28Bk9yPFy9vj-4-cu_h7pWPXIapTEBYOD9b6Y8oqWLxoChC0QAvD_BwE'

response = requests.get(url)
soup = BeautifulSoup(response.content, 'html.parser')
promos = soup.find_all('div', class_='swiper-slide')
total_promos = [
    #["Compañía", "Nombre", "Vigencia", "Precio", "MB Libres", "Minutos", "SMS"]
]


for promo in promos:
    insert_promo = ["ATNT"]
    name = promo.select_one('.title').text.strip()
    price = promo.select_one('.price b').text.strip()
    free_data = promo.select_one('.promo1 b').text.strip()#promo.find('div', class_='promo1').find('b').text
    video = promo.select_one('.promo2 b').text.strip()
    social_media = wa = promo.select_one('.promo3 b').text.strip()
    sms = minute = promo.select_one('.mobileQuantity').text.strip()
    duration = promo.select_one('.promoDuration').text.strip()

    insert_promo.append(name)
    insert_promo.append(duration)
    insert_promo.append(price)
    insert_promo.append(free_data)
    #insert_promo.append(social_media)
    #insert_promo.append(video)
    insert_promo.append(minute)
    insert_promo.append(sms)
    #insert_promo.append(wa)
    total_promos.append(insert_promo)

#df = pd.DataFrame(total_promos)


"""
sql = "INSERT INTO public.oferta_comercial
(empresa, nombre_producto, vigencia, precio, megas, minutos, mensajes)
values(%s, %s, %s, %s, %s, %s, %s); "--query 

values = (,,,)
mycursor.execute(sql, values)

#commit the changes to the db
mydb.commit()
"""