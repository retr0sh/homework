#Номер 1
start = int(input("Введите начало отрезка: "))
end = int(input("Введите конец отрезка: "))
step = int(input("Введите шаг: "))

if step > 0:
    step = -step

if start > end:
    start, end = end, start

def f(x):
    return x**2 + 2*x + 1
x = end
while x >= start:
    y = f(x)
    print(f'x = {x} y = {y}')
    x += step
print()
print('-------------------------------------------')
print()
#Номер 2
n = int(input('Введите число: '))
n2 = 0
for i in range(n):
    n2 += 1
    print((-1)**n2 * 1/(2**n2))
