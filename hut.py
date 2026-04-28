import turtle as t


def zeichne_H() -> None:
    t.right(90)
    t.forward(100)
    t.backward(50)
    t.left(90)
    t.forward(50)
    t.right(90)
    t.forward(50)
    t.backward(100)
    t.left(90)
    t.forward(30)


def zeichne_T() -> None:
    t.forward(30)
    t.right(90)
    t.forward(100)
    t.backward(100)
    t.left(90)
    t.forward(60)


def zeichne_U() -> None:
    t.right(90)
    t.forward(70)
    t.circle(30, 180)
    t.forward(70)
    t.right(90)
    t.forward(30)


t.bgcolor("black")
t.color("cyan")
t.width(3)
t.speed(7)

zeichne_H()
zeichne_U()
zeichne_T()
