'''Напишите программу, которая принимает на вход цифру, обозначающую день недели, и проверяет, является ли этот день выходным.

Пример:

- 6 -> да
- 7 -> да
- 1 -> нет'''

d = int(input('Enter the day '))
if 0 > d or d > 7:
    print("В неделе всего 7 дней, чувак")
elif d > 5:
    print("Выходной")
else:
    print("Унылые серые будни")