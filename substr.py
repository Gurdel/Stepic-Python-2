s, t = input(), input()
ind = s.find(t)
count = 0
while(ind != -1):
    count += 1
    ind = s.find(t, ind + 1)
print(count)

'''
Вашей программе на вход подаются две строки s и t, состоящие из строчных латинских букв.

Выведите одно число – количество вхождений строки t в строку s.

Пример:
s = "abababa"
t = "aba"

3
'''