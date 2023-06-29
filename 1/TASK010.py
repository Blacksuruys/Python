# Дан массив, состоящий из целых чисел. Напишите программу, которая подсчитает количество элементов массива, больших предыдущего (элемента с предыдущим номером)



from random import randint
list_1=[randint(1,10) for i in range(10)]
count=0
print(list_1)
for i in range(len(list_1)-1):
    if (list_1[i]<list_1[i+1]):
        count+=1
print(count)