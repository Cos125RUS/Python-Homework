# Задайте список из вещественных чисел. Напишите программу, которая найдёт разницу между максимальным и минимальным значением дробной части элементов.
# Пример:
# - [1.1, 1.2, 3.1, 5, 10.01] => 0.19

nums = [1.1, 1.2, 3.1, 5, 10.01]
nums = list(map(float, nums))
nums = list(zip(*(i for i in [map(float, (('0.' + i) for i in (str(i).split('.')))) for i in nums])))
nums = list(filter(lambda x: x > 0, sorted(nums[1])))
print('dif = ', nums[-1] - nums[0])
