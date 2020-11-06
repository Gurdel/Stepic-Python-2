parents = {'global':'None'}
local_vars = {'global':[]}

def create(namespace, parent):
    parents[namespace] = parent
    local_vars[namespace] = []

def add(namespace, var):
    local_vars[namespace].append(var)

def get(namespace, var):
    if namespace == 'None':
        return namespace
    if var in local_vars[namespace]:
        return namespace
    return get(parents[namespace], var)

for i in range(int(input())):
    command, namespace, var = input().split()
    if command == 'create':
        create(namespace, var)
    elif command == 'add':
        add(namespace, var)
    else:
        print(get(namespace, var))

'''
Реализуйте программу, которая будет эмулировать работу с пространствами
имен. Необходимо реализовать поддержку создания пространств имен и
добавление в них переменных.

В данной задаче у каждого пространства имен есть уникальный текстовый 
идентификатор – его имя.

Вашей программе на вход подаются следующие запросы:

create <namespace> <parent> –  создать новое пространство имен с именем 
<namespace> внутри пространства <parent>
add <namespace> <var> – добавить в пространство <namespace> переменную <var>
get <namespace> <var> – получить имя пространства, из которого будет взята 
переменная <var> при запросе из пространства <namespace>, или None, если 
такого пространства не существует
'''