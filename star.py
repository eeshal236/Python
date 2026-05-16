import turtle
turtle.Screen().bgcolor("Purple")
turtle.setup(500,500)
t = turtle.Turtle()

for i in range(3):
    t.forward(100)
    t.left(120)
t.penup()
t.left(90)
t.forward(50)
t.pendown()
t.right(90)

for j in range(3):
    t.forward(100)
    t.right(120)

turtle.done()