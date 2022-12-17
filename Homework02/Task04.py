'''Задайте список из N элементов, заполненных числами из промежутка [-N, N].
Найдите произведение элементов на указанных позициях.
Позиции хранятся в отдельном списке
( пример n=4, lst1=[4,-2,1,3] - списко на основе n, а позиции элементов lst2=[3,1].'''

import random

n = int(input('N = '))
list = []
sum = 0

for i in range(n):
    list.append(random.randrange(-n, n+1))

print(list)


pos = open('file.txt', 'r')

for num in pos:
    print('x =', list[int(num)])
    sum += list[int(num)]

pos.close()

print()
print('sum =', sum)
