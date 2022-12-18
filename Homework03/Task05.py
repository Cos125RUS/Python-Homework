'''Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.
Пример:
- для k = 8 список будет выглядеть так: [-21 ,13, -8, 5, −3, 2, −1, 1, 0, 1, 1, 2, 3, 5, 8, 13, 21]'''


def fi(n):
    if n == 1 or n == -1:
        return 1
    elif n == 0:
        return 0
    elif n == -2:
        return -1
    else:
        if n > 0:
            return fi(n-1) + fi(n-2)
        else:
            return fi(n+2) - fi(n+1)


n = int(input("n = "))
numbers = []

for i in range(-n, n+1):
    numbers.append(fi(i))

print(numbers)