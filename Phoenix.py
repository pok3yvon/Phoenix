from ast import arg
import turtle
import random
turtle.screensize(canvwidth=600, canvheight=600)
t = turtle.Turtle()

def buttonclick(x,y):
    print("Clicked at the coordinate({0},{1})".format(x,y))
turtle.onscreenclick(buttonclick,1)
turtle.title("Wilder World")
colors = [ "red","purple","blue","green","orange","yellow"]
my_pen = turtle.Pen()
turtle.bgcolor("black")
for x in range(360):
   my_pen.pencolor(colors[x % 6])
   my_pen.width(x/100 + 1)
   my_pen.forward(x)
   my_pen.left(59)
   t.speed(0)

colorlist=["purple", "pink", "blue", "white", "red", "green", "yellow"]
col=random.choice(colorlist)
t.color(col)
t.shape("turtle")#Draw Wilder World Logo
t.penup()
t.speed(1)
t.setpos(-300.0,200.)
t.pendown()
t.pensize(18)
t.right(115)
t.fd(150)
t.left(55)
t.fd(350)
t.left(115)
t.fd(150)
t.right(115)
t.fd(149)
t.left(115)
t.fd(350)
t.left(55)
t.fd(150)
t.left(125)
t.fd(370)
t.right(112)
t.fd(385)
t.penup()
t.setpos(-190.0,30.0)
t.pendown()
t.color()
t.right(63)
t.fd(195)
t.right(122)
t.fd(195)
t.penup()
t.goto(-100.0,-120.0)
t.pendown()
t.color(col)
t.write("Meow", font=('Cambria',75))
    
t.pensize(8)
t.speed(0)

t.color()#Draw 50 stars for random position between x=-300~300 and y=100~300
colorlist=["purple", "pink", "blue", "white", "red", "green", "yellow", "violet", "cyan"]#Set colorlist for star
def star(size):#define star size and shape
        for x in range(22,42):
            t.forward(50)
            if x % 2 == 0:
                t.left(175)
            else:
                t.left(225)    
for i in range(75):
        t.begin_fill()
        x=random.randrange(-300,300)#Set the x,y range
        y=random.randrange(-300,300)
        t.up()
        t.goto(x,y)
        t.down()
        col=random.choice(colorlist)
        t.color(col)
        star(random.randrange(300,500))#Set star size
        t.end_fill()
        t.hideturtle()#Hide turtle

turtle.done()