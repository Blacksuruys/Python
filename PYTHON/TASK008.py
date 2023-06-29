# Дан список чисел. Определите, сколько в нем встречается различных чисел.


from random import randint
list_1=[randint(1,10) for i in range(10)]
print(list_1,end=" ")
count=1
list_1.sort()
print(list_1)
for i in range(len(list_1)-1):
    if list_1[i]!=list_1[i+1]:
        count+=1
print(count)