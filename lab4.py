def prog1():
    m = []
    while (n := str(input())) != "stop":
        m.append(n)
    print(" ".join(m))

def prog2():
    while (m := str(input())) != "stop":
        if "ф" in m or "Ф" in m:
            print("Ого! Это редкое слово!")
        else:
            print("Эх, это не очень редкое слово...")
def prog3():
    from random import randint
    mist = 0
    right = 0
    while mist != 3:
        m = randint(1, 10)
        n = randint(1, 10)
        summ = m + n
        print(m, "+", n)
        f = int(input())
        if f == summ:
            print("Правильно!")
            right += 1
        else:
            mist += 1
            print("Ответ неверный")
    print("Игра окончена.", "Правильных ответов:", right)