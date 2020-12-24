import requests
import regex
A, B = input(), input()
notFound = True
try:
    a = requests.get(A)
    links = regex.findall(r'<a.*href=\"(.*)\">?', a.text)
    for link in links:
        b = requests.get(link)
        if B in b.text:
            print('Yes')
            notFound = False
            break
    if notFound:
        print('No')
except:
    print('No')

'''
Рассмотрим два HTML-документа A и B.
Из A можно перейти в B за один переход, если в A есть ссылка на B, т. е. внутри A есть тег <a href="B">, возможно с дополнительными параметрами внутри тега.
Из A можно перейти в B за два перехода если существует такой документ C, что из A в C можно перейти за один переход и из C в B можно перейти за один переход.

Вашей программе на вход подаются две строки, содержащие url двух документов A и B.
Выведите Yes, если из A в B можно перейти за два перехода, иначе выведите No.

Обратите внимание на то, что не все ссылки внутри HTML документа могут вести на существующие HTML документы.
'''