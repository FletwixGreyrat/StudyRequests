import requests
import fake_useragent
from bs4 import BeautifulSoup
import lxml

session = requests.Session()

User = fake_useragent.UserAgent().random

header = {'user-agent': User}

data = {}

link = 'https://stepik.org/catalog?auth=login'

# search = input('Введите поисковый запрос:')

search = 'python'

response = session.post(f'{link}', headers=header, data=data)

courses = session.get(f'https://stepik.org/catalog/search?q={search}', headers=header)

print(courses.text)

soup = BeautifulSoup(courses.text, 'html.parser')

block  = soup.find('div', class_='catalog')

cookiesList = [{'domain': key.domain, 'name': key.name, 'path': key.path, 'value': key.value} for key in session.cookies]

session2 = requests.Session()

for i in cookiesList:
    session2.cookies.set(**i)


print(block)

# allTitiles = soup.find_all('li')

# print(allTitiles)

# allData = {}