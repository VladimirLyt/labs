#Этолаба3
def prog1():
    a=[]
    while (b:=str(input()))!="stop":
        a.append(b)
    print(" ".join(a))
prog1()
def prog2():
    while (b:=str(input()))!="stop":
        if "ф" in b or "Ф" in b:
            print("Ого это редкое слово")
        else:
            print("Эх, это не очень редкое слово")
prog2()
def prog3():
    from random import randint
    mi=0
    rh=0
    while mi!=3:
        a = randint(1, 10)
        b = randint(1, 10)
        summ=a+b
        print(a,"+",b)
        f=int(input())
        if f == summ:
            print("Правильно")
            rh+=1
        else:
            mi+=1
            print("Ответ неправильный")
    print("Игра окончена", "Правильных ответов", rh)
prog3()