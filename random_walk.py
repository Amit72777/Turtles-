import random
import turtle as t


def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)

    return r, g, b


t.colormode(255)
timmy = t.Turtle()
timmy.shape('turtle')
timmy.pensize(5)
timmy.speed(10)

direction = (0, 90, 180, 270)

for _ in range(200):
    angle = random.choice(range(5, 360))
    # timmy.pencolor(random.choice(color))
    timmy.color(random_color())
    timmy.forward(20)
    timmy.setheading(random.choice(direction))

screen = t.Screen()
screen.exitonclick()
