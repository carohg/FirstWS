import psycopg2
import requests
from bs4 import BeautifulSoup

url = 'https://www.promociones-att.com.mx/mas/?utm_campaign_dom=0101020304&gad=1&gclid=CjwKCAjwuqiiBhBtEiwATgvixCQJzuAniyG28Bk9yPFy9vj-4-cu_h7pWPXIapTEBYOD9b6Y8oqWLxoChC0QAvD_BwE'
conn = psycopg2.connect(database = 'vmm_esb', user = 'postgres', password = 'tangananica', host = '172.31.19.104', port = '5432')
cur = conn.cursor()
insert_query = "INSERT INTO public.referencia_oferta_comercial(empresa, nombre_producto, vigencia, precio, megas, minutos, mensajes) VALUES (%s, %s, %s, %s, %s, %s, %s)"

response = requests.get(url)
soup = BeautifulSoup(response.content, 'html.parser')
promoss = soup.find_all('div', class_='swiper-slide')


for promo in promoss:
    company = "ATT"
    name = promo.select_one('.title').text.strip()
    price = promo.select_one('.price b').text.strip()
    free_data = promo.select_one('.promo1 b').text.strip()
    # video = promo.select_one('.promo2 b').text.strip()
    # social_media = wa = promo.select_one('.promo3 b').text.strip()
    sms = minute = promo.select_one('.mobileQuantity').text.strip()
    duration = promo.select_one('.promoDuration').text.strip()
    v = (company, name, duration, price, free_data, minute, sms)
    cur.execute(insert_query, v)
    conn.commit()

cur.close()
conn.close()

