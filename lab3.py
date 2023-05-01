def zad1 (num: int):
    return True if num % 3 == 0 else False
print ("Проверка функции деления на три")
print (zad1(9))
print (zad1(45))
def zad2(number):
    rez = None
    try:
        rez = 100 / float(number)
    except ValueError:
        print ("В эту функцию нужно передать число ")
    except ZeroDivisionError:
        print("Деление на ноль невозможно ")
    except Exception as e:
        print("Ошибка ", e)
    return rez
print("Проверка функции: деления 100 на число ")
print(zad2(10))
print(zad2("g"))
print(zad2(0))
def zad3(date: str):
    try:
        date = date.split(".")
        if int(date[0]) * int(date[1]) == int(date[2][2:]):
            return True
        else:
            return False
    except:
        print("Фунция принимает строку вида dd.mm.yyyy ")
print(zad3("22.01.2022"))
print(zad3("23.05.2004"))
def zad4(ticket: str):
    s1 = sum([int(i) for i in ticket[:int(len(ticket) / 2)]])
    s2 = sum([int(i) for i in ticket[int(len(ticket) / 2):]])
    if s1 == s2:
        return True
    else:
        return False
print(zad4("385916"))
print(zad4("231002"))