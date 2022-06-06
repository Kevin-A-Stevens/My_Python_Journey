import turtle

# Square
kevin_turtle = turtle.Turtle()


def square():
    kevin_turtle.forward(100)
    kevin_turtle.right(90)
    kevin_turtle.forward(100)
    kevin_turtle.right(90)
    kevin_turtle.forward(100)
    kevin_turtle.right(90)
    kevin_turtle.forward(100)


# square()
# kevin_turtle.forward(100)
# square()


elephant_weight = 3000
ant_weight = 0.1

if elephant_weight < ant_weight:
    square()
else:
    kevin_turtle.forward(100)

turtle.done()
