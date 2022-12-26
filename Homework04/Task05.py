# Даны два файла, в каждом из которых находится запись многочлена.
# Задача - сформировать файл, содержащий сумму многочленов.

with open('file1.txt', 'r') as file:
    arg = file.read().replace(' = 0', '').replace(' ', '').split('+')
with open('file2.txt', 'r') as file:
    arg += file.read().replace(' = 0', '').replace(' ', '').split('+')
dic = {}
for degree in arg:
    if degree.count('^'):
        key = degree[-1:]
    elif degree.count('x'):
        key = '1'
    else:
        key = '0'
    if key not in dic.keys():
        dic[key] = [degree.replace('*x','').replace('^','').replace(key,'')]
    else:
        dic[key] += [degree.replace('*x','').replace('^','').replace(key,'')]
formula = ""
for i in dic.keys():
    sum = 0
    for j in dic[i]:
        sum += int(j)
    formula += str(sum) + '*x^' + i + ' + '
formula += ' = 0'
formula = formula.replace('x^1', 'x').replace('*x^0', '').replace(' 1*', ' ').replace('+  +', '+').replace('+  ', '')
with open('res.txt', 'w') as file:
    file.write(formula)
