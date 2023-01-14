# Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных.
# Входные и выходные данные хранятся в отдельных текстовых файлах.

with open('Source.txt','r') as file:
    file = file.read() + ' '

with open('RLE.txt', 'w') as rle:
    while len(file) > 1:
        i = 1
        while file[0] == file[i]:
            i += 1
        rle.write(f'{ord(file[0])} {i}\n')
        file = file[i:]
