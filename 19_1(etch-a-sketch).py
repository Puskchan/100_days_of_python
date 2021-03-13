import turtle as t

ari = t.Turtle()
pg = t.Screen()


def forward():
    ari.fd(10)


def backwards():
    ari.bk(10)


def right():
    ari.right(10)


def left():
    ari.left(10)


def clear():
    pg.reset()
    game()


def game():
    pg.listen()
    pg.onkey(key="space", fun=forward)
    pg.onkey(key="d", fun=right)
    pg.onkey(key="a", fun=left)
    pg.onkey(key="s", fun=backwards)


game()
pg.onkey(key="c", fun=clear)

pg.exitonclick()
