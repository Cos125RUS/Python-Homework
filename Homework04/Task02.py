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


n = int(input("Введите число N: "))
i = 2
list = []

while i <= n:
    if n % i == 0:
        list.append(i)
        n //= i
        i = 2
    else:
        i += 1
print(f"Простые множители введенного числа указаны в списке: {list}")



def PrimeFactorization(N):
    i = 2
    factor = []
    while N >= i * 2:
        if N % i == 0:
            result = PrimeFactorization(N // i)
            result.append(i)
            factor += result
            return sorted(factor)
        i += 1
    if len(factor) == 0:
        factor.append(N)
    return sorted(factor)


N = int(input("Введите число: "))

print(PrimeFactorization(N))
