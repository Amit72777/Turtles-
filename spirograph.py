import random
import turtle as t


# TODO 2 : create a function who return a random RGB color code
def random_color():
    """return r,g,b color code"""
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)

    return r, g, b

# TODO 1 : crete  a timmy object in turtle class


timmy = t.Turtle()
timmy.speed(11)
timmy.shape('turtle')
timmy.pensize(1)
t.colormode(255)
size_of_gap = 5  # for width of two line

# TODO 3 : create a for loop print a circle and move its place
for _ in range(360//size_of_gap):
    timmy.circle(100)
    timmy.color(random_color())
    timmy.seth(size_of_gap)
    size_of_gap += 5

screen = t.Screen()
screen.exitonclick()
