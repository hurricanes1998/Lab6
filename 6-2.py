def del100():
    try:
        ch = float(input("введите число: "))
        d = 100 / ch
        print(f"результат: {d}")
    except ValueError:
        print("ошибка: введите корректное число.")
    except ZeroDivisionError:
        print("ошибка: деление на ноль невозможно.")

del100()