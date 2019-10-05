import turtle
from random import randint
t = turtle.Pen()
sc = turtle.Screen()
sc.bgcolor("black")
t.speed(0)
turtle.colormode(255)
for i in range(100):
    r = randint(0, 255)
    g = randint(0, 255)
    b = randint(0, 255)
    t.pencolor(r, g, b)
    t.circle(8*i)
    t.circle(-8*i)
    t.left(i)

turtle.mainloop()
