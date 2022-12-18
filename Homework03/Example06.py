# 20. Задайте список. Напишите программу, которая определит, присутствует ли в заданном списке строк некое число.
# будем искать число 3 в одной из строк списка


listOfStrings = []
for i in range(5):
    listOfStrings.append(input("New string: "))

n = int(input("n = "))
num = str(n)

for i in listOfStrings:
    print(i.count(num))

