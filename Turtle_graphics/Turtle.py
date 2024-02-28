import turtle

screen = turtle.Screen()
screen.setup(width=400, height=400)

t = turtle.Turtle()
t.speed(5)

def heart(r, color):
    t.fillcolor(color)
    t.begin_fill()
    t.left(140)
    t.forward(113)

    for i in range(200):
        t.right(1)
        t.forward(1)

    t.left(120)

    for i in range(200):
        t.right(1)
        t.forward(1)

    t.forward(112)
    t.end_fill()
    t.left(135)


heart(1,"red")
#heart(0.5, "blue")
#t.ht()
canvas = turtle.getcanvas()
canvas.postscript(file="output_image.png", colormode="color")
screen.exitonclick()