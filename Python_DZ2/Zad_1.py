"""
Задача 10: На столе лежат n монеток. Некоторые из них
 лежат вверх решкой,а некоторые – гербом.
Определите минимальное число монеток, которые нужно перевернуть, 
чтобы все монетки были повернуты
вверх одной и той же стороной. Выведите минимальное количество монет,
 которые нужно перевернуть.
5 -> 1 0 1 1 0
2
"""

N = int(input("Введите количество монет "))
gerb = reshka = 0
for i in range(N):
    x = int(input("герб(1) или решка(0)? "))
    if x == 1:
        gerb += 1
    else:
        reshka += 1
if gerb < reshka:
    print (f" {gerb} ")
elif gerb == reshka:
    print (f" {gerb} ")
else:
    print (f" {reshka} ")