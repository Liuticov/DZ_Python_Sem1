"""
Задача №11. Решение в группах
Дано натуральное число A > 1. Определите, каким по
счету числом Фибоначчи оно является, то есть
выведите такое число n, что φ(n)=A. Если А не
является числом Фибоначчи, выведите число -1.
Input: 5
Output: 6 
"""
element_number = int(input('Enter your number: '))
count = 0
#Fn = Fn-1 + Fn-2
f1 = f2 = 1

while ((f1 + f2)< element_number):
    f1, f2 = f2, f1 + f2
    #temp = f1
    #f1 = f2
    #f2 = temp + f2
    count +=1
    if (f2 == element_number):
        print(count)
print('Ваше число неявляется числом Фибоначчи')