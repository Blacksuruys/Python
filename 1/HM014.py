# Задача 14: Требуется вывести все целые степени двойки (т.е. числа вида 2k), не превосходящие числа N.




n=int(input('Введите число: '))
degree=1
for i in range(n):
    degree*=2
    if degree>n:
        break
    print(degree)