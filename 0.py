"""
За день машина произжает n километров. Сколько надо дней
надо чтобы машина проехала m километров?
n = 700
m = 750
Output:
2
""" 
n = int(input('Введите количество километров в день:'))
m = int(input('Длина маршрута: '))

res=int (bool(n % m ))
days = m // n + res

print (n, m, days)