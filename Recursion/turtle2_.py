import turtle

my_turtle = turtle.Turtle()
my_turtle.shape('turtle')
my_exit = turtle.Screen()
my_turtle.pencolor('red')
my_turtle.speed(10)

count = 0
flag = True


def draw_circle(myturtle, length):
    global count
    global flag

    if length < 30:
        flag = False

    if count > 3:
        count = 0
        change_length(length)

    if flag:
        myturtle.circle(length)
        myturtle.penup()
        myturtle.right(90)
        myturtle.pendown()
        count += 1
        print(count)
        draw_circle(myturtle, length)


def change_length(length):
    draw_circle(my_turtle, length-10)


draw_circle(my_turtle, 90)

my_exit.exitonclick()