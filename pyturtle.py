import turtle

screen = turtle.Screen()
screen.bgcolor("White")
screen.setup(width=1000, height=1000)

p = turtle.Turtle()

s = 6
x = 100
angle = 360 / s

for i in range(s):
    p.forward(x)
    p.right(angle)

p.penup()
p.goto(-200, 100)
p.pendown()

for i in range(5):
    p.forward(100)
    p.right(144)

turtle.Screen().exitonclick()