#Задайте натуральное число N. Напишите программу, которая составит список простых множителей числа N.

def addition(num, n, i):
    num[0] = int(n/i)
    num.append(i)
    return num

def primeFactors(num):
    if num[0] == 1:
        for j in range(1, len(num)-1):
            print(num[j], '* ', end = '')
        print(num[-1])
    else:
        for i in range(2, num[0]):
            if num[0] % i == 0:
                primeFactors(addition(num, num[0], i))

num = []
num.append(int(input('N = ')))
print(f'{num[0]} = ', end = '')
primeFactors(num)