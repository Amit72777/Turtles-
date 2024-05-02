from turtle import Turtle, Screen
tom = Turtle()

''' Hints: 
    1: press 'w' for move forward
    2: press 's' for move backward
    3: press 'a' for move Clockwise
    4: press 'd' for move Anti-Clockwise
    5: press 'c' for Clear Screen 
'''


def move_forward():
    tom.forward(30)


def move_backward():
    tom.bk(30)


def clear_screen():
    tom.clear()
    tom.up()
    tom.home()
    tom.down()


def turn_left():
    tom.left(10)


def turn_right():
    tom.right(10)


screen = Screen()

screen.listen()
screen.onkey(key='w', fun=move_forward)
screen.onkey(key='s', fun=move_backward)
screen.onkey(key='c', fun=clear_screen)
screen.onkey(key='a', fun=turn_left)
screen.onkey(key='d', fun=turn_right)


screen.exitonclick()
