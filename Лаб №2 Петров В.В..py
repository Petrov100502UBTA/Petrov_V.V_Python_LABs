import math

def get_float_input(prompt):
  """Запрашивает ввод числа с клавиатуры и проверяет его корректность."""
  while True:
    try:
      return float(input(prompt))
    except ValueError:
      print("Ошибка: Введите корректное число.")

def sh(x):
    """Вычисляет гиперболический синус."""
    return (math.exp(x) - math.exp(-x)) / 2

def f_x(choice, x, y):
    if choice == 1:
        print("Выбрана функция sh(x)")
        return sh(x)
    elif choice == 2:
        print("Выбрана функция x^2")
        return x ** 2
    elif choice == 3:
        print("Выбрана функция e^x")
        return math.exp(x)
    elif choice == 4:
        print("Выбрана функция cos(0.5x)")
        return math.cos(0.5 * x)
    elif choice == 5:
         print("Выбрана функция e^y")
         return math.exp(y)
    elif choice == 6:
        if y == 0:
          print("Ошибка: деление на ноль в ln(x/y)")
          return None
        print("Выбрана функция ln(x/y)")
        return math.log(x/y)
    else:
        print("Неверный выбор функции.")
        return None


def calculate_b(x, y, choice):

    xy = x * y

    if 0.5 <= xy < 10:
        fx = f_x(choice, x, y)
        if fx is None:
          return None
        print("Вычисляем по первой ветви")
        return (math.exp(fx) - abs(y))
    elif 0.1 < xy < 0.5:
        fx = f_x(choice, x,y)
        if fx is None:
            return None
        print("Вычисляем по второй ветви")
        return (abs(fx + y))**(1/3)
    else:
        fx = f_x(choice, x,y)
        if fx is None:
            return None
        print("Вычисляем по третьей ветви")
        return 2 * fx**2

if __name__ == "__main__":
    print("Выберите вид функции f(x):")
    print("1. sh(x)")
    print("2. x^2")
    print("3. e^x")
    print("4. cos(0.5x)")
    print("5. e^y")
    print("6. ln(x/y)")

    while True:
      try:
        choice = int(input("Введите номер выбранной функции: "))
        if 1 <= choice <= 6:
          break
        else:
            print("Неверный выбор, введите число от 1 до 6.")
      except ValueError:
          print("Неверный выбор, введите целое число")


    x = get_float_input("Введите значение x: ")
    y = get_float_input("Введите значение y: ")

    b = calculate_b(x, y, choice)
    if b is not None:
      print(f"Результат вычисления b: {b}")
