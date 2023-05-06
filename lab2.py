def prog1():
    parol = input("Your password is:  ")
    parol2 = input("repeat password:  ")
    if len(parol) < 4:
        print("Your password too short")
    elif 3 < len(parol) and len(parol) < 6:
        print("weak password")
    else:
        print("OK.")
        is_numeric = False
        is_upper = False
        is_lower = False
        is_spec = False
        for char in parol:
            if char.isnumeric():
                is_numeric = True
            elif char.isupper():
                is_upper = True
            elif char.islower():
                is_lower = True
            elif char in "#@!*&%^":
                is_spec = True
        if is_numeric and is_upper and is_lower and is_spec:
            print("Password accepted")
            if parol == parol2:
                print("Registration is over")
            else:
                print("passwords mismatch")
def prog2():
    nom = int(input("Введите номер Вашего места от 1 до 54 :  "))
    if nom in range(37, 55):
        print("У Вас боковое место")
    elif nom % 2 == 0:
        print("У Вас верхнее место")
    else:
        print("У Вас нижнее место")
def prog3():
    g = int(input("Введите интересующий Вас год:  "))
    if (g % 4 == 0) and (g % 100 != 0) or (g % 400 == 0):
        print("это високосный год")
    else:
        print("это НЕ високосный год")
def prog4():
    colors = ("Синий", "Желтый", "Красный")
    col1 = input("Введите первый цвет: ")
    col2 = input("Введите второй цвет: ")
    if col1 in colors and col2 in colors:
        if col1 != col2:
            if (col1 in ("Синий", "Красный")) and (col2 in ("Синий", "Красный")):
                print("Фиолетовый")
            if (col1 in ("Желтый", "Красный")) and (col2 in ("Желтый", "Красный")):
                print("Оранжевый")
            if (col1 in ("Синий", "Желтый")) and (col2 in ("Синий", "Желтый")):
                print("Зеленый")
        else:
            print(col1)
    else:
        print("Ошибка")