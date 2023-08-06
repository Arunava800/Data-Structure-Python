import turtle

my_turtle = turtle.Turtle()
my_win = turtle.Screen()
my_turtle.shape('turtle')
counter = 0


def draw_circle(myturtle, length):
    global counter
    if counter > 3:
        return
    if length > 0:
        myturtle.circle(length)
        draw_circle(myturtle, length-10)
    change_state(myturtle)


def change_state(myturtle):
    global counter
    myturtle .penup()
    myturtle.right(90)
    myturtle.pendown()
    counter += 1
    draw_circle(myturtle, 100)





draw_circle(my_turtle, 100)
my_win.exitonclick()


