import requests

link = 'https://icanhazip.com/'
responce1 = requests.get(link).text #* html страница
responce2 = requests.get(link).content #* Байты
print(responce1, responce2) 
responce = requests.get(link)
print(responce.status_code) #* статус код. 200 - заебись

