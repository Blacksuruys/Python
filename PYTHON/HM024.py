# Задача 24: В фермерском хозяйстве в Карелии выращивают чернику. Она растёт на круглой грядке, причём кусты высажены только по окружности. Таким образом, у каждого куста есть ровно два соседних. Всего на грядке растёт N кустов.
# Эти кусты обладают разной урожайностью, поэтому ко времени сбора на них выросло различное число ягод — на i-ом кусте выросло ai ягод.
# В этом фермерском хозяйстве внедрена система автоматического сбора черники. Эта система состоит из управляющего модуля и нескольких собирающих модулей. Собирающий модуль за один заход, находясь непосредственно перед некоторым кустом, собирает ягоды с этого куста и с двух соседних с ним.
# Напишите программу для нахождения максимального числа ягод, которое может собрать за один заход собирающий модуль, находясь перед некоторым кустом заданной во входном файле грядки.



from random import randint

n=int(input('Введите количество кустов: '))
qu_ber = []
for _ in range(n):
    qu_ber.append(randint(1,10))
max_ber = qu_ber[0]+qu_ber[len(qu_ber)-1]+qu_ber[1]
print(qu_ber)
for i in range(len(qu_ber)-1):
    if qu_ber[len(qu_ber)-1]+qu_ber[len(qu_ber)-2]+qu_ber[0]>max_ber:
        max_ber=qu_ber[len(qu_ber)-1]+qu_ber[len(qu_ber)-2]+qu_ber[0]
    if qu_ber[i]+qu_ber[i-1]+qu_ber[i+1] > max_ber:
        max_ber = qu_ber[i]+qu_ber[i-1]+qu_ber[i+1]
print(max_ber)