# Use a for loop when you know how many times a loop will run
import turtle

# Square
kevin_turtle = turtle.Turtle()
kevin_turtle.speed(10)


def square():
    kevin_turtle.forward(100)
    kevin_turtle.right(90)
    kevin_turtle.forward(100)
    kevin_turtle.right(90)
    kevin_turtle.forward(100)
    kevin_turtle.right(90)
    kevin_turtle.forward(100)


for i in range(4):
    square()

turtle.done()
