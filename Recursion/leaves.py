import turtle


def leaf(length, t):
    if length > 5:
        t.forward(length)
        t.right(20)
        leaf(length - 15, t)
        t.left(40)
        leaf(length - 15, t)
        t.right(20)
        t.backward(length)


def main():
    t = turtle.Turtle()
    my_win = turtle.Screen()
    t.left(90)
    t.up()
    t.backward(100)
    t.down()
    t.color('green')
    leaf(75, t)
    my_win.exitonclick()


main()
