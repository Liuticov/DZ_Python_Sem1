"""
for i in range(3, 5, 2):
    print("heloo")

Задача №9. Решение в группах
По данному целому неотрицательному n вычислите
значение n!. N! = 1 * 2 * 3 * … * N (произведение всех
чисел от 1 до N) 0! = 1 Решить задачу используя цикл
while
Input: 5
Output: 120
"""
number = int(input('Введите число: '))
factorial = number

for i in range(1, number):
    factorial = factorial * i

print(factorial)