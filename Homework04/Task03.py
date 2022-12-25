#Задайте последовательность чисел.
#Напишите программу, которая выведет список неповторяющихся элементов исходной последовательности.

enter = input('Nums: ')
nums = list(map(int, enter.split()))
for i in nums:
    if nums.count(i) > 1:
        count = nums.count(i)
        for j in range(count):
            nums.remove(i)
print(nums)