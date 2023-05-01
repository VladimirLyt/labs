def prog():
    from PIL import Image
    name = "1.1.png"
    with Image.open(name) as img:
        img.load()
    img_crop=img.crop((200, 200, 1600, 1600))
    img_crop.save('crop.png', quality=95)
def prog2():
    from PIL import Image
    ivents= {1:"Хэллоуин.png", 2:"ДеньСвятВален.png", 3:"Сантройка.png"}
    print()

    a=int(input("Мероприятие: \n"
                "1.Хэллоуин\n"
                "2.День святого валентина\n"
                "3.Сантройка\n"))
    name= ivents[a]
    with Image.open(name) as img:
        img.load()
    img.show()
prog2()
def prog3():
    from PIL import Image, ImageDraw, ImageFont
    a = input()
    image = Image.open("HappyBr.jpg")
    cons= a + ", Поздравляю"
    font = ImageFont.truetype("arial.ttf", 30)
    drawer = ImageDraw.Draw(image)
    drawer.text((250, 100), cons , font=font, fill="blue")
    image.save('new_img.jpg')
    image.show()
