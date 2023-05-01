def prog1():
    from PIL import Image
    name = "1.1.png"
    with Image.open(name) as img:
        img.load()

    img.show()
    width, height = img.size

    format=img.format

    mode=img.mode

    print(width)
    print(height)
    print(format)
    print(mode)
def prog2():
    from PIL import Image
    name = "1.1.png"
    with Image.open(name) as img:
        img.load()
    new_img = img.resize((img.width//3,img.height//3))
    new_img.save("c_1.png")
    c_img = img.transpose(Image.FLIP_TOP_BOTTOM)
    c_img.save("fliptop.png")
    c_img = img.transpose(Image.FLIP_LEFT_RIGHT)
    c_img.save("flip.png")
    name1 = "c_1.png"
    with Image.open(name1) as img1:
        img1.load()
    width, height=img.size
    width1, height1 = img1.size
    format = img.format
    format1 = img1.format
    mode = img.mode
    mode1 = img1.mode
    print(width, "Изменено ", width1)
    print(height, "Изменено ", height1)
    print(format, "Изменено ", format1)
    print(mode, "Изменено ", mode1)
def prog3():
    from PIL import Image,ImageFilter
    name=["1.jpg","2.jpg","3.jpg","4.jpg","5.jpg"]
    eff=[ImageFilter.BLUR]
    for i in name:
        with Image.open(i) as img:
            img.load()
            new_img = img.filter(eff[0])
            new_img.save("new_" + i)
def prog4():
    from PIL import Image
    water = "2.1.png"
    with Image.open(water) as img_water:
        img_water.load()
    img_water =Image.open(water)
    img_water=img_water.resize((img_water.width//2,img_water.height//2))
    name = "1.1.png"
    with Image.open(name) as img:
        img.load()
    img.paste(img_water,(420,10),img_water)
    img.save("watermark_1.png")
prog1()