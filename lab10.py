def prog1():
    import json
    with open("1.json", encoding='utf-8' ) as f:
        data = json.load(f)
    prod=data['products']
    for i in prod:
        print('Название: '+ i["name"])
        print('Цена: ' + str(i["price"]))
        print('Вес: ' + str(i["weight"]))
        if i['available']==True:
            print('В наличии', "\n")
        else:
            print('Нет в наличии' , "\n")
def prog2():
    import json
    name=input("Название: ")
    price=input("Цена: ")
    aval= input("Есть в наличии: ")
    weight=input("Вес: ")
    def change(data):
        with open("2.json","r+",encoding='utf-8') as file:
            file_data = json.load(file)
            file_data['products'].append(data)
            file.seek(0)
            json.dump(file_data, file, indent=4)
    if aval == "Да":
        aval=True
    else:
        aval=False
    y = {
        "name": name,
        "price": price,
        "available": aval,
        "weight": weight
        }
    change(y)
    with open("2.json", encoding='utf-8') as f:
        data = json.load(f)
    prod = data['products']
    for i in prod:
        print('Название: ' + i["name"])
        print('Цена: ' + str(i["price"]))
        print('Вес: ' + str(i["weight"]))
        if i['available'] == True:
            print('В наличии', "\n")
        else:
            print('Нет в наличии', "\n")
def prog3():
    import json
    with open("en-rus.json","r", encoding='utf-8') as f:
        data = json.load(f)
    g=data['words']
prog3()