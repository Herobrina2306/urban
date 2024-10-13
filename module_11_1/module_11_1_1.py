import requests
from pprint import pprint

s = 'https://yandex.ru/images/search'

r1 = requests.get(s, {'text': 'kitten', 'from': 'tabbar'})

print(r1.url, '\n')
print(requests.options(s), '\n')
# ссылка на котиков)

w = 'https://i.ytimg.com/vi/bF84zFYeU9U/maxresdefault.jpg'
w1 = requests.get(w).content
with open('kitten.jpg', 'wb') as file:
    file.write(w1)





