#Дан список чисел. Определите, сколько в нем
#встречается различных чисел.
#Input: [1, 1, 2, 0, -1, 3, 4, 4]
#Output: 6

my_list = [1, 1, 2, 0, -1, 3, 4, 4]
my_list2 = []
for elem in my_list:
    if elem not in my_list2:
        my_list2.append(elem)
        print(len(my_list2))