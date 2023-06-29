# Дана последовательность из N целых чисел и число K. Необходимо сдвинуть всю последовательность (сдвиг - циклический) на K элементов вправо, K – положительное число.



k=int(input("Введите число: "))
list_1=[1,2,3,4,5,6,7]
list_2=[]
for i in range(len(list_1)-k):
    a=list_1.pop(0)
    list_2.append(a)
for j in range(len(list_1)):
    list_2.insert(j,list_1[j])
print(list_2)