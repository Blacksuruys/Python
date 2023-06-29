# Задача 6: Вы пользуетесь общественным транспортом? Вероятно, вы расплачивались за проезд и получали билет с номером. Счастливым билетом называют такой билет с шестизначным номером, где сумма первых трех цифр равна сумме последних трех. Т.е. билет с номером 385916 – счастливый, т.к. 3+8+5=9+1+6. Вам требуется написать программу, которая проверяет счастливость билета.



n = int(input('Введите шестизначный номер: '))
sum1 = 0
sum2 = 0
for i in range(3):
    sum1 += n % 10
    n //= 10
for i in range(3):
    sum2 += n % 10
    n //= 10
if sum1==sum2:
    print('Ура!Вам достался счастливый билет')
else:
    print('У Вас обычный билет.')