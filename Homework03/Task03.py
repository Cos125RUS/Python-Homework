'''Задайте список из вещественных чисел. Напишите программу, которая найдёт разницу между максимальным и минимальным значением дробной части элементов.
Пример:
- [1.1, 1.2, 3.1, 5, 10.01] => 0.19'''

list = [1.1, 1.2, 3.1, 5, 10.01]

min = round((list[0] - int(list[0])), 2)
max = round((list[0] - int(list[0])), 2)

for i in range(1, len(list)):
    if 0 < (list[i] - int(list[i])) > max:
        max = round((list[i] - int(list[i])), 2)
    if 0 < (list[i] - int(list[i])) < min:
        min = round((list[i] - int(list[i])), 2)

difference = (max - min)
print(difference) 