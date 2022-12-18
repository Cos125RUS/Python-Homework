# 21. Напишите программу, которая определит позицию второго вхождения строки в списке либо сообщит, что её нет.

list = []
for i in range(5):
    list.append(input("New string: "))

find = input('So what? ')
count = 0

for i in range(len(list)):
    if list[i].count(find):
        count += 1
    if count == 2:
        print(i)
        break

if count < 2:
    print('No')