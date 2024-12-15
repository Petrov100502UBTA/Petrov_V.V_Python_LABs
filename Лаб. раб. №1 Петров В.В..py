import math
x = float(input("Введите значение x -> "))
y = float(input("Введите значение y -> "))
z = float(input("Введите значение z -> "))

if (10 * (x**(1/3) + x**(y + 2)))**(1/2) > 0:
    if abs(z) <= 1:
        a1 = math.sqrt(10 * (x ** (1 / 3) + x ** (y + 2)))
        a2 = math.asin(z) ** 2 - abs(x)
        s = a1 * a2
        print("Результат ", s)
    else:
        print("Значение выражения не может быть вычислено")
else:
    print("Значение выражения не может быть вычислено")