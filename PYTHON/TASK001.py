# За день машина проезжает n километров. Сколько дней нужно, чтобы проехать маршрут длиной m километров?
# При решении этой задачи нельзя пользоваться условной инструкцией if и циклами.

n = int(input())
m = int(input())
day = m//n+(m % n != 0)
print(day)