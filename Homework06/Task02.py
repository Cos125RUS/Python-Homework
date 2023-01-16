# Напишите программу, которая принимает на вход число N и выдает набор произведений чисел от 1 до N.
# Пример:
# - пусть N = 4, тогда [ 1, 2, 6, 24 ] (1, 1*2, 1*2*3, 1*2*3*4)
#

def multy(x):
    mult = 1
    while x > 1:
        mult *=x
        x -= 1
    return mult

print(list(map(multy, [i for i in range(1, int(input('n = ')) + 1)])))