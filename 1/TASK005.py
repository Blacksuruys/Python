# Дано натуральное число A > 1. Определите, каким по счету числом Фибоначчи оно является, то есть выведите такое число n, что φ(n)=A. Если А не является числом Фибоначчи, выведите число -1.

n = int(input('Введите число: '))
i = 2
fubonacci = 1
fub1 = 0
fub2 = 1
while fubonacci < n:
    i += 1
    fub1 = fubonacci-fub1
    fub2 = fubonacci
    fubonacci = fub1+fub2
if fubonacci == n:
   print(i)
elif fubonacci > n:
   print("-1")