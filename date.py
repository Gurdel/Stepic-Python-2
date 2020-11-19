from datetime import date, timedelta

lst = list(map(int, input().split()))
cur_date = date(*lst)
td = timedelta(days=int(input()))
cur_date += td
print(cur_date.year, cur_date.month, cur_date.day)

'''
В первой строке дано три числа, соответствующие некоторой дате date -- год, месяц и день.
Во второй строке дано одно число days -- число дней.

Вычислите и выведите год, месяц и день даты, которая наступит, когда с момента исходной даты date пройдет число дней, равное days.
'''