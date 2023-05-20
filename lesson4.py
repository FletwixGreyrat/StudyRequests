import requests
import requests
import fake_useragent
from bs4 import BeautifulSoup


link = 'https://www.avito.ru/derbent?q=%D0%BF%D0%BA'
fakeUseragent = fake_useragent.UserAgent().random
head = {'user-agent': 'dolboeb'}

session = requests.Session()

responce = session.get(link, headers=head).text

soup = BeautifulSoup(responce, 'lxml')

allsales = soup.find_all('h3', itemprop='name', class_='title-root-zZCwT iva-item-title-py3i_ title-listRedesign-_rejR title-root_maxHeight-X6PsH text-text-LurtD text-size-s-BxGpL text-bold-SinUO')

allsales = [c.text for c in allsales]

allprices = soup.find_all('span', class_="price-text-_YGDY text-text-LurtD text-size-s-BxGpL")
# allprices = soup.find_all('meta', itemprop='price')
#! text.replace(u'\xa0',' ').replace(u'\u2009', '')
# print(allprices)
print(len(allprices))
for i in allprices:
    print(i.text)
# print(allsales)
# print(allprices)
