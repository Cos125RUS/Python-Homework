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