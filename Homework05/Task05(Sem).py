# 4.Саша и Галя коллекционируют монетки.
# Каждый из них решил записать номиналы монеток из своей коллекции.
# Получилось два списка.
# Эти списки поступают на вход программы в виде двух строк из целых чисел, записанных через пробел.
# Необходимо выделить значения, присутствующие в обоих списках и оставить среди них только четные.
# Результат вывести на экран в виде строки полученных чисел в порядке их возрастания через пробел.
# При реализации программы используйте функцию filter и кое-что еще (для упрощения программы), подумайте что.
#
# Sasha = list(map(int, input("Сашины монеты: ").split()))
# Galy = list(map(int, input("Галины монеты: ").split()))
# print(*sorted(filter((lambda i: not i%2), (i for i in Sasha if Galy.count(i)))))
#
sasha = '1 5 15 20 10 50'
gala = '2 5 25 10 20'

f = lambda x: list(filter(lambda a: int(a)%2 == 0, x.split(" ")))
result = set(f(sasha)).intersection(set(f(gala)))

print(*sorted(list(result)))
