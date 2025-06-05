import turtle
import random


screen = turtle.Screen()
screen.title("مثلث آشوب")
t = turtle.Turtle()
t.speed(0)
t.hideturtle()


vertices = [(-200, -200), (200, -200), (0, 200)]
t.penup()
t.goto(vertices[0])
t.pendown()
t.color("blue")
for vertex in vertices[1:]:
    t.goto(vertex)
t.goto(vertices[0])


x = random.uniform(-100, 100)
y = random.uniform(-100, 100)
t.penup()
t.color("red")
for _ in range(10000):
    target = random.choice(vertices)
    x = (x + target[0]) / 2
    y = (y + target[1]) / 2
    t.goto(x, y)
    t.dot(2)

screen.exitonclick()