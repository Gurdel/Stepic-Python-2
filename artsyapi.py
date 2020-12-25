import requests
import sys
import json

client_id = '2c9e72d4086344024e9f'
client_secret = '37bba6572bac895f7bb9f1096275b4dc'

# инициируем запрос на получение токена
r = requests.post("https://api.artsy.net/api/tokens/xapp_token",
                  data={
                      "client_id": client_id,
                      "client_secret": client_secret
                  })

# разбираем ответ сервера
j = json.loads(r.text)

# достаем токен
token = j["token"]
res = []
# создаем заголовок, содержащий наш токен
headers = {"X-Xapp-Token" : token}
with open('input.txt') as sr:
    for line in sr:
        line = line.strip()
        r = requests.get('https://api.artsy.net/api/artists/' + line, headers=headers)
        r.encoding = 'utf-8'
        # разбираем ответ сервера
        j = json.loads(r.text)
        res.append(j['birthday']+' '+j['sortable_name'])
[print(i[5:]) for i in sorted(res)]

'''
Вам даны идентификаторы художников в базе Artsy.
Для каждого идентификатора получите информацию о имени художника и годе рождения.
Выведите имена художников в порядке неубывания года рождения. В случае если у художников одинаковый год рождения, выведите их имена в лексикографическом порядке.
'''