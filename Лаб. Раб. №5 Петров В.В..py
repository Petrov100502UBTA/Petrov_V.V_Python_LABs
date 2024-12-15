def compare_with_max():
    """Вводит список чисел, находит максимум и сравнивает с остальными."""

    try:
        n = int(input("Введите количество элементов в списке: "))
        if n <= 0:
            print("Количество элементов должно быть положительным.")
            return

        numbers = []
        for i in range(n):
          while True:
            try:
              num = int(input(f"Введите элемент {i+1}: "))
              numbers.append(num)
              break
            except ValueError:
               print("Ошибка: Введите целое число")


        if not numbers:
            print("Список пуст.")
            return

        max_number = max(numbers)
        less_count = 0
        greater_count = 0

        for number in numbers:
            if number < max_number:
                less_count += 1
            elif number > max_number:
                greater_count += 1


        print(f"Максимальный элемент: {max_number}")
        print(f"Количество чисел меньше максимального: {less_count}")
        print(f"Количество чисел больше максимального: {greater_count}")


    except ValueError:
        print("Ошибка: Введите целое число для количества элементов.")

if __name__ == "__main__":
    compare_with_max()

def sum_greater_than_5():
    """Вводит список чисел и вычисляет сумму тех, что больше 5."""

    try:
        n = int(input("Введите количество элементов в списке: "))
        if n <= 0:
           print("Количество элементов должно быть положительным.")
           return

        numbers = []
        for i in range(n):
            while True:
              try:
                num = int(input(f"Введите элемент {i+1}: "))
                numbers.append(num)
                break
              except ValueError:
                 print("Ошибка: Введите целое число")

        if not numbers:
            print("Список пуст.")
            return

        sum_of_greater = 0
        for number in numbers:
            if number > 5:
                sum_of_greater += number

        print(f"Сумма чисел больше 5: {sum_of_greater}")

    except ValueError:
        print("Ошибка: Введите целое число для количества элементов.")

if __name__ == "__main__":
   sum_greater_than_5()
