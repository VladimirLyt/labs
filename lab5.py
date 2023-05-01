def prog1():
    from random import randint
    a = []
    k = 0
    for i in range(5):
        m = randint(1, 15)
        a.append(m)
    p = int(input('Введите число: '))
    for i in range(5):
        if p == a[i]:
            k += 1
    if k > 0:
        print(a)
        print("Поздравляю, Вы угадали число!")
    else:
        print("Нет такого числа!")
def prog2():
    from random import randint
    a = []
    for i in range(6):
        m = randint(1, 10)
        a.append(m)
    b = a.copy()
    for i in range(0, 6):
        for j in range(i + 1, 6):
            if a[i] == b[j]:
                print(a[i])
            else:
                j += 1
        i += 1
def prog3():
    a = ("Пн", "Вт", "Ср", "Чт", "Пт", "Сб", "Вс")
    v = int(input("Cколько выходных на неделе Вы хотите иметь? "))
    print("Ваши рабочие дни: ", a[:-v])
    print("Ваши выходные дни: ", a[-v:])
def prog4():
    from random import randint
    a = ["Тарнаева", "Лыткин", "Гусев", "Сидорова", "Иванов", "Фатькин", "Ившина", "Рахимов", "Васильев", "Жарко"]
    b = ["Киркоров", "Пугачева", "Лазарев", "Гагарина", "Басков", "Леонтьев", "Бузова", "Ваенга", "Агутин", "Воробьев"]
    c = [] * 10
    k = 0
    tmp = 0
    cnt = 0
    while tmp < 10:
        if tmp < 5:
            ch = randint(0, 9)
            if a[ch] in c:
                k += 1
            else:
                c.append(a[ch])
                tmp += 1
        elif tmp < 10:
            ch = randint(0, 9)
            if b[ch] in c:
                k += 1
            else:
                c.append(b[ch])
                tmp += 1
    if "Иванов" in c:
        cnt += 1
    c = tuple(sorted(c))
    print(a)
    print(b)
    print(c, len(c))
    print("Людей с фамилией Иванов в команде: ", cnt)