# Даны два файла, в каждом из которых находится запись многочлена.
# Задача - сформировать файл, содержащий сумму многочленов.

with open('file1.txt', 'r') as file:
    arg = file.read().replace(' = 0', '').replace(' ', '').split('+')
with open('file2.txt', 'r') as file:
    arg += file.read().replace(' = 0', '').replace(' ', '').split('+')
dic = {}
for degree in arg:
    q = (degree + ' ').replace('*x^', ' ').replace('x^', '1 ').replace('*x', ' 1').replace('x', '1 1').split()
    print(q)
    if len(q) == 1:
        q.append('0')
    if q[1] not in dic.keys():
        dic[q[1]] = [q[0]]
    else:
        dic[q[1]] += [q[0]]
dic = dict(sorted(dic.items(), reverse=True))
formula = ""
for i in dic.keys():
    sum = 0
    for j in dic[i]:
        sum += int(j)
    formula += str(sum) + '*x^' + str(i) + ' + '
formula += ' = 0'
formula = formula.replace('x^1', 'x').replace('*x^0', '').replace(' 1*', ' ').replace('+  +', '+').replace('+  ', '')
with open('res.txt', 'w') as file:
    file.write(formula)
