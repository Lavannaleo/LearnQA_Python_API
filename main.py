import requests

print('Hello from Anna Leonidova')

responce = requests.get('https://playground.learnqa.ru/api/get_text')
print(responce.text)