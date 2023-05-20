import requests
import fake_useragent
from bs4 import BeautifulSoup as bs

user = fake_useragent.UserAgent().random

header = {'user-agent': user}



link = 'https://browser-info.ru/'
responce = requests.get(link, headers=header).text

soup = bs(responce, 'lxml')
block1 = soup.find('div', id='tool_padding')
check_js = block1.find('div', id='javascript_check')
result1 = check_js.find_all('span')[1].text
print(result1)


checkUserAgent = block1.find('div', id='user_agent').text
print(checkUserAgent)