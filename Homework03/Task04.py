'''Напишите программу, которая будет преобразовывать десятичное число в двоичное.
Пример:
- 45 -> 101101
- 3 -> 11
- 2 -> 10'''

n = int(input("N = "))

list = []
while n > 1:
    list.insert(0,n%2)
    n = int(n/2)

list.insert(0,n)

s = ""
for i in list:
    s += str(i)

print(s)

a = int(input('введите число для перевода = '))
b = ''
while a != 0:
    b = str(a % 2) + b
    a = a // 2
print(b)

num10 = 45
print(f'Двоичное число через функцию bin: {bin(num10)}')

def toBinary(num):
    if num == 0:
        return '0'
    if num == 1:
        return '1'
    else:
        return toBinary(num // 2) + str(num % 2)
