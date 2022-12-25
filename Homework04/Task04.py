'''Задана натуральная степень k. Сформировать случайным образом список коэффициентов (значения от 0 до 100)
многочлена и записать в файл многочлен степени k.
Пример:
- k=2 => 2*x² + 4*x + 5 = 0 или x² + 5 = 0 или 10*x² = 0'''

import random
file = open('file.txt', 'w')

k = int(input('k = '))
res = ""

for i in range(k,-1, -1):
    f = ""
    a = random.randrange(0,100)
    if a > 1:
        f = str(a)
        if i > 0:
            f += '*'
    if a > 0:
        if i > 1:
            f += 'x^' + str(i) + ' + '
        elif i == 1:
            f += 'x + '
    res += f
if len(res) > 0:
    res += ' = 0'
else:
    print('No arguments')
res = res.replace('+  ', '')
res = res.replace('+  +', '+')
file.write(res)
file.close()