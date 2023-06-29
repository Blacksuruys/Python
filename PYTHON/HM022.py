# Задача 22: Даны два неупорядоченных набора целых чисел (может быть, с повторениями). Выдать без повторений в порядке возрастания все те числа, которые встречаются в обоих наборах.
# Пользователь вводит 2 числа. n — кол-во элементов первого множества. m — кол-во элементов второго множества. Затем пользователь вводит сами элементы множеств.

from random import randint
n=int(input('Введите длину первого набора чисел: '))
m=int(input('Введите длину второго набора чисел: '))
first=[]
second=[]
result=[]
for _ in range(n):
    first.append(randint(-10,10))
for _ in range(m):
    second.append(randint(-10,10))
first.sort()
second.sort()
print(f'Первый: {first}\nВторой: {second}')
if n<m:
    for i in range(n):
        if first[i] in second and first[i] in first:
            result.append(first[i])
else:
    for i in range(m):
        if second[i] in second and second[i] in first:
            result.append(second[i])
result=set(result)
result=list(result)
result.sort()
print(f'Ответ: {result}')