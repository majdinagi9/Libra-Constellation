import turtle
from time import sleep

turtle.setup(1.0, 1.0)
turtle.speed(30)
turtle.hideturtle()


def splashPage():
    turtle.bgcolor("black")
    turtle.color("White")
    turtle.penup()
    turtle.goto(0, 100)
    turtle.write(
        "Midterm Project", font=("Arial", 24, "italic"), align="center")
    turtle.right(90)
    turtle.forward(100)
    turtle.write(
        "The Libra Constellation",
        font=("Arial", 24, "italic"),
        align="center")
    turtle.forward(100)
    turtle.write("Majdi Nagi", font=("Arial", 24, "italic"), align="center")
    sleep(5)


def libraPic():
    turtle.clearscreen()
    turtle.pu()
    turtle.setposition(0, 100)
    turtle.pd()
    turtle.bgcolor("black")
    turtle.bgpic("libra.gif")
    turtle.update()
    sleep(5)
    turtle.clearscreen()


def libraInDots():
    turtle.penup()
    turtle.hideturtle()
    turtle.goto(0, 240)
    turtle.dot(20)
    turtle.write('Zuben Elschemali')
    turtle.goto(150, 100)
    turtle.dot(20)
    turtle.write('Zuben Elgenubi')
    turtle.goto(120, -150)
    turtle.dot(15)
    turtle.write('Brachium')
    turtle.goto(-110, -170)
    turtle.dot(10)
    turtle.write('Upsilon turtlee')
    turtle.goto(-130, -210)
    turtle.dot(10)
    turtle.write('Tau turtlee')
    turtle.goto(-150, 120)
    turtle.dot(10)
    turtle.write('Zuben Elakrab')
    turtle.goto(-250, 100)
    turtle.dot(10)
    turtle.write('Theta turtlee')
    turtle.goto(100, 280)
    turtle.dot(10)
    turtle.write('Zuben Elakribi')
    #drow lines
    turtle.goto(0, 240)
    turtle.pendown()
    turtle.goto(150, 100)
    turtle.goto(120, -150)
    turtle.penup()
    turtle.goto(-110, -170)
    turtle.pendown()
    turtle.goto(-130, -210)
    turtle.goto(-110, -170)
    turtle.goto(-150, 120)
    turtle.goto(150, 100)
    turtle.goto(-150, 120)
    turtle.goto(0, 240)
    sleep(5)


def showStars(starSZ, starColor):
    turtle.color(starColor)
    turtle.pendown()
    turtle.begin_fill()
    for side in range(5):
        turtle.left(144)
        turtle.forward(starSZ)
    turtle.end_fill()
    turtle.penup()


def pageFour():
    turtle.bgcolor("black")
    turtle.color("blue")

    turtle.penup()
    turtle.hideturtle()
    turtle.goto(0, 240)
    showStars(20, "blue")
    turtle.write('Zuben Elschemali')
    turtle.goto(150, 100)
    showStars(20, "blue")
    turtle.write('Zuben Elgenubi')
    turtle.goto(120, -150)
    showStars(15, "blue")
    turtle.write('Brachium')
    turtle.goto(-110, -170)
    showStars(10, "blue")
    turtle.write('Upsilon turtlee')
    turtle.goto(-130, -210)
    showStars(10, "blue")
    turtle.write('Tau turtlee')
    turtle.goto(-150, 120)
    showStars(10, "blue")
    turtle.write('Zuben Elakrab')
    turtle.goto(-250, 100)
    showStars(5, "blue")
    turtle.write('Theta turtlee')
    turtle.goto(100, 280)
    showStars(5, "blue")
    turtle.write('Zuben Elakribi')

    turtle.speed(1000)
    turtle.update()
    turtle.goto(0, 240)
    turtle.pendown()
    turtle.goto(150, 100)
    turtle.goto(120, -150)
    turtle.penup()
    turtle.goto(-110, -170)
    turtle.pendown()
    turtle.goto(-130, -210)
    turtle.goto(-110, -170)
    turtle.goto(-150, 120)
    turtle.goto(150, 100)
    turtle.goto(-150, 120)
    turtle.goto(0, 240)
    turtle.speed(1000)
    sleep(5)


splashPage()
libraPic()
libraInDots()
pageFour()
