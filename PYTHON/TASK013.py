# Напишите программу, которая принимает на вход строку, и отслеживает, сколько раз каждый символ уже встречался. Количество повторов добавляется к символам с помощью постфикса формата _n.




n=input('Введите строку: ')
list_1=[]

for i in n:
    if i not in list_1:
        list_1.append(i)

print(list_1,n)