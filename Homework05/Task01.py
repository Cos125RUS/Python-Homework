# 1.Напишите программу, удаляющую из текста все слова, содержащие "абв".

print(*list(filter(lambda t: not t.count('абв'), input('Enter the text: ').split())))
