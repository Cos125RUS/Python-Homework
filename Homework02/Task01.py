'''Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.
Пример:
- 6782 -> 23
- 0,56 -> 11'''

n = float(input('N = '))

string = str(n)
sum = 0

for i in range(len(string)):
    if string[i] != '.':
        sum += int(string[i])

print(sum)