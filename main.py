import requests
from bs4 import BeautifulSoup
import csv

# http://www.truba.ua/catalog-otoplenie/

base_url = 'http://www.truba.ua/catalog-otoplenie/c-ukraine-'
companies = []
FILENAME = 'trubaUa.csv'


request = requests.get(base_url)
soup = BeautifulSoup(request.content,'html.parser')
#pages = int(soup.find_all('a', {'class': ''})[-2].text)

for page in range(1,20): #page + 1
    url = base_url + 's-' + str(page)
    request = requests.get(url)
    soup = BeautifulSoup(request.content, 'html.parser')
    data = soup.find_all('li', {'class': 'result_'})
    for item in data:
        data = soup.find_all('ul', {'class': 'result_'})
        #companyName = item.find('a', {'class': 'name_des i'}).text
        companyName = item.find('a', {'class': 'i'}).text
        activities= item.find('li', {'class': 'span3'}).text
      #  information = item.find('div', {'class': 'snipet'}).text
        city = item.find('div', {'class': 'result_right'}).text
        #phone = item.select("div:nth-of-type(2)")
        phone = item.select("div")[1].text
        price = item.select("div > div:nth-of-type(1)")




     #div:nth-child(3)

     #  priceList = item.find('a',{'class':'i'}).text



        companies.append({
        'companyName':companyName,
        'activities': activities,
        'city': city,
        #'information': information,
        'phone':phone,
       # 'price':price
        })



for company in companies:
     print('Название компании:', company['companyName'])
     print('Деятельность', company['activities'])
     print('Город:', company['city'])
     #print('Информация про компанию:', company['information'])
     print('Телефон:',company['phone'])
    # print('Прайс Лист',company['price'])
     print('-------------------------------------------------------------------')


  # print('Сайт:',company['site'])
  # print()

with open(FILENAME, 'w',) as csv_file:
    csv_writer = csv.writer(csv_file)
    for item in companies:
        csv_writer.writerow([item])


#print(companies)
#print(activities)