import turtle
t = turtle.Pen()

t.speed(0)
for i in range(100):
    t.circle(8*i)
    t.circle(-8*i)
    t.left(i)

turtle.mainloop()
