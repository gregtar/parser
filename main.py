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

for page in range(1,2): #page + 1
    url = base_url + 's-' + str(page)
    request = requests.get(url)
    soup = BeautifulSoup(request.content, 'html.parser')
    data = soup.find_all('li', {'class': 'result_'})
    for item in data:
        data = soup.find_all('ul', {'class': 'result_'})
        companyName = item.find('a', {'class': 'name_des i'}).text
        information = item.find('div', {'class': 'snipet'}).text
        city = item.find('div', {'class': 'result_right'}).text
      #  site = item.find('ul', {'class': 'l-item-features'}).contents[-2].text
      #  phone = item.find('ul', {'class': 'result_'})
      
#

     #  priceList = item.find('a',{'class':'i'}).text



        companies.append({
        'companyName':companyName,
        'information':information,
        'city': city,
        # 'site':site,
        # 'phone':phone,
       #  'priceList':priceList
        })

        # center_u > div > div > div > div > div > div.span9 > div.span7 > ol > li:nth-child(1) > div:nth-child(3)
        # center_u > div > div > div > div > div > div.span9 > div.span7 > ol > li:nth-child(3) > div:nth-child(3)


for company in companies:
     print('Название компании:', company['companyName'])
     print('Информация про компанию:', company['information'])
     print('Город:',company['city'])
   #  print('Телефон',company['phone'])


  #  print('Сайт:',company['site'])
   # print('Телефон:', company['phone'])
   # print('Ссылка на прайслит:', company['priceList'])
   # print()

with open(FILENAME, 'w',) as csv_file:
    csv_writer = csv.writer(csv_file)
    for item in companies:
        csv_writer.writerow([item])


#print(companies)
#print(phone)