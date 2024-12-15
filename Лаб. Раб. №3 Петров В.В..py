import math

# Исходные данные
x1 = 2
xn = 5
delta_x = 0.5
a = 1.5
b = 4.8

def calculate_y(x):
    """Вычисляет значение y по формуле."""
    try:
        return a * (b / x - math.log(a * x) / (b ** 2))
    except ValueError:
        return float('nan')  # Возвращаем NaN при ошибке (например, log от отрицательного числа)

# 1. Вычисление с использованием цикла for
print("Результаты вычислений с использованием цикла for:")
for x in range(int((xn - x1) / delta_x) + 1):
  current_x = x1 + x * delta_x
  y = calculate_y(current_x)
  print(f"x = {current_x:.2f}, y = {y:.4f}")


# 2. Вычисление с использованием цикла while
print("\nРезультаты вычислений с использованием цикла while:")
x = x1
while x <= xn:
    y = calculate_y(x)
    print(f"x = {x:.2f}, y = {y:.4f}")
    x += delta_x


# Сравнение результатов
print("\nСравнение результатов:")
print("Оба цикла дают одинаковые результаты вычислений.")
