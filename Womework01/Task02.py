#Напишите программу для проверки истинности утверждения ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z для всех значений предикат.


x = True
y = False
z = True

print()
print('x - ', x)
print('y - ', y)
print('z - ', z)
print()
print('not x - ', not x)
print('not y - ', not y)
print('not z - ', not z)
print()
print('x or y or z - ', x or y or z)
print('not(x or y or z) - ', not(x or y or z))
print()
print('not x and not y and not z - ',not x and not y and not z)
print()

if not(x or y or z) == (not x and not y and not z):
    print('not(x or y or z) = (not x and not y and not z)\n\nEquality!')
