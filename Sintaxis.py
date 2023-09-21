import turtle

def dibujar_flor():
    window = turtle.Screen()
    window.bgcolor("white")

    flor = turtle.Turtle()
    flor.shape("turtle")
    flor.speed(10)

    flor.color("yellow")

    for _ in range(36):
        dibujar_petalos(flor)
        flor.right(10)

    flor.color("green")
    flor.right(90)
    flor.forward(300)

    window.exitonclick()

def dibujar_petalos(t):
    t.forward(100)
    t.right(45)
    t.forward(100)
    t.right(135)
    t.forward(100)
    t.right(45)
    t.forward(100)
    t.right(135)

dibujar_flor()
