import turtle
turtle.bgcolor("black")
turtle.pensize(1)
turtle.speed(0)

for x in range(6):
    for y in ["red", "yellow", "green", "cyan", "pink", "purple"]:
        turtle.color(y)
        turtle.circle(100)
        turtle.left(10)

turtle.done()