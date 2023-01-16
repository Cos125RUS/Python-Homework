#Задайте последовательность чисел.
#Напишите программу, которая выведет список неповторяющихся элементов исходной последовательности.

# enter = input('Nums: ')
# nums = list(map(int, enter.split()))
# for i in nums:
#     if nums.count(i) > 1:
#         count = nums.count(i)
#         for j in range(count):
#             nums.remove(i)
# print(nums)


# a= [1,2,2,2,2,3,1,4]
#
# print(set(a))

from random import randint

array_int = [randint(0, 10) for i in range(20)]
new_array = [item for item in array_int if array_int.count(item) == 1]
print(array_int)
print(new_array)



b = []
a = [6, 6, 1, 2, 3, 3, 3, 4, 5, 5]
for i in range(len(a)):
    if a.count(a[i]) == 1:
        b.append(a[i])
print(b)

