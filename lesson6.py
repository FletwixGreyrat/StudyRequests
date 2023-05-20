import requests
import bs4
import fake_useragent

storageNum = 1
link = f'https://zastavok.net'

header = {'user-agent': fake_useragent.UserAgent().random}

response = requests.get(link + f'/{storageNum}/', headers=header)

soup = bs4.BeautifulSoup(response.text, 'lxml')

block = soup.find('div', class_='block-photo')

allImages = soup.find_all('div', class_='short_full')
allImageLinks = [image.find('a').get('href') for image in allImages]
print(allImageLinks)

num = 1
for i in allImageLinks:
    req = requests.get(link + i, headers=header)
    soup = bs4.BeautifulSoup(req.text, 'lxml')
    block = soup.find('a', id='orig_size').get('href')
    # print(block)

    image_bytes = requests.get(f'{link}{block}').content
    with open(f'images/{num}.jpg', 'wb') as file:
        file.write(image_bytes)
    num += 1