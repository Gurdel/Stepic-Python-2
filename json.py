import json

inp = '[{"name": "B", "parents": ["A", "C"]}, {"name": "C", "parents": ["A"]}, {"name": "A", "parents": []}, {"name": "D", "parents":["C", "F"]}, {"name": "E", "parents":["D"]}, {"name": "F", "parents":[]}]'
data = json.loads(inp)
dic = {line['name']:0 for line in data}

classes = {}
for line in data:
    if(line['parents']):
        classes[line['name']] = line['parents']
    else:
        classes[line['name']] = ['obj']

def isparent(son, par):
    if son not in classes.keys():
        return False
    if son == par:
        return True
    if son == 'obj':
        return False
    if par in classes[son]:
        return True
    for cl in classes[son]:
        if isparent(cl, par):
            return True
    return False

for son in dic:
    for par in dic:
        if isparent(par, son):
            dic[son] += 1

[print(i + ' : ' + str(dic[i])) for i in sorted(dic.keys())]

'''
Вам дано описание наследования классов в формате JSON.
Описание представляет из себя массив JSON-объектов, которые соответствуют классам. У каждого JSON-объекта есть поле name, которое содержит имя класса, и поле parents, которое содержит список имен прямых предков.

Пример:
[{"name": "A", "parents": []}, {"name": "B", "parents": ["A", "C"]}, {"name": "C", "parents": ["A"]}]

Эквивалент на Python:

class A:
    pass

class B(A, C):
    pass

class C(A):
    pass

Гарантируется, что никакой класс не наследуется от себя явно или косвенно, и что никакой класс не наследуется явно от одного класса более одного раза.

Для каждого класса вычислите предком скольких классов он является и выведите эту информацию в следующем формате.

<имя класса> : <количество потомков>

Выводить классы следует в лексикографическом порядке.

Sample Input:

[{"name": "A", "parents": []}, {"name": "B", "parents": ["A", "C"]}, {"name": "C", "parents": ["A"]}]
Sample Output:

A : 3
B : 1
C : 2
'''