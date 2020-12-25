import requests
import sys
import json

with open('input.txt') as sr, open('output.txt', 'w') as sw:
    for line in sr:
        line = line.strip()
        req = requests.get('http://numbersapi.com/' + line + '/math?json=true')
        req = json.loads(req.text)
        if req['found']:
            sw.write('Interesting\n')
        else: sw.write('Boring\n')

'''
В этой задаче вам необходимо воспользоваться API сайта numbersapi.com

Вам дается набор чисел. Для каждого из чисел необходимо узнать, существует ли интересный математический факт об этом числе.

Для каждого числа выведите Interesting, если для числа существует интересный факт, и Boring иначе.
Выводите информацию об интересности чисел в таком же порядке, в каком следуют числа во входном файле.
'''