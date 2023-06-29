# Иван Васильевич пришел на рынок и решил купить два арбуза: один для себя, а другой для тещи. Понятно, что для себя нужно выбрать арбуз потяжелей, а для тещи полегче. Но вот незадача: арбузов слишком много и он не знает как же выбрать самый легкий и самый тяжелый арбуз? Помогите ему!


from random import randint

n=int(input('Введите число: '))
weight=0
max_=1
min_=20
for i in range(n):
    weight=randint(1,20)
    if weight>max_:
        max_=weight
    if weight<min_:
         min_=weight
    print(weight,end=" ")
print(f'min = {min_}, max= {max_}')