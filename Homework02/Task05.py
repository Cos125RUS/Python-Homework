#Реализуйте алгоритм перемешивания списка. (рандомно поменять местами элементы списка между собой)

import random

n = int(input('N = '))
list = []
sum = 0

for i in range(1, n+1):
    list.append(i)

print(list)

for j in range(0,500):
    for i in range(0,n):
        index = random.randrange(0, n-1)
        change = list[i]
        list[i] = list[index]
        list[index] = change
print(list)
