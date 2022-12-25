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
    if a > 0:
        f = str(a) + '*x^' + str(i) + ' + '
    res += f
if len(res) > 0:
    res += ' = 0'
else:
    print('No arguments')

res = res.replace(' 1*x', ' x').replace('x^1', 'x').replace('*x^0', '').replace('+  ', '').replace('+  +', '+')
file.write(res)
file.close()