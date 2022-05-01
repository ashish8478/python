import random
import turtle as t

def drawimage(mypen, tscreen):
    gifs = ['yum1.gif', 'yum2.gif', 'yum3.gif']
    
    mypen.showturtle()

    tscreen.addshape('yum1.gif')
    mypen.shape('yum1.gif')
    mypen.penup()
    mypen.goto(-200,-255)
    mypen.stamp()
    mypen.pendown()

    tscreen.addshape('yum2.gif')
    mypen.shape('yum2.gif')
    mypen.penup()
    mypen.goto(0,-255)
    mypen.stamp()
    mypen.pendown()

    tscreen.addshape('yum3.gif')
    mypen.shape('yum3.gif')
    mypen.penup()
    mypen.goto(170,-255)
    mypen.stamp()
    mypen.pendown()

mypen = t.Turtle()
tscreen = mypen.getscreen()
tscreen.colormode(255)
mypen.speed(0)
mypen.hideturtle()

numfireworks = random.randint(10, 15)

for fw in range(0, numfireworks):
    x = random.randint(-200, 200)
    y = random.randint(-200, 200)

    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    mypen.color(r, g, b)

    mypen.penup()
    mypen.goto(x, y)
    mypen.pendown()

    flaresize = random.randint(20, 100)

    for flare in range(0, 18):
        mypen.forward(flaresize)
        mypen.backward(flaresize)
        mypen.left(20)


mypen.penup()
mypen.goto(-225, 150)
mypen.color('black')
mypen.pendown()
mypen.write('  Thank you Harshad Kaka!! \n                 And \n   have a Happy Diwali !!', font = ('Arial', 36, 'italic'))

drawimage(mypen, tscreen)

t.done()