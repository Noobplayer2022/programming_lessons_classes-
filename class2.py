import turtle
import random
import math
import time

screen = turtle.Screen()
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.title("Turtle Game")

class Shape:
    def __init__(self, shape_type, color):
        self.t = turtle.Turtle()
        self.t.shape(shape_type)
        self.t.color(color)
        self.t.penup()
        self.t.speed(0)
        
        self.t.goto(random.randint(-300, 300), random.randint(-250, 250))
        self.t.setheading(random.randint(0, 360))
        self.speed = random.uniform(5, 9) 

    def move(self):
        self.t.forward(self.speed)
        x, y = self.t.pos()

        if x > 390 or x < -390:
            self.t.setheading(180 - self.t.heading())
        if y > 290 or y < -290:
            self.t.setheading(-self.t.heading())

    def is_colliding_with(self, other):
        return self.t.distance(other.t) < 25

    def destroy(self):
        self.t.hideturtle()

shape_types = ["triangle", "square", "circle"]
colors = ["red", "blue", "green", "yellow", "cyan", "magenta", "orange", "white"]

shapes = []
for _ in range(10):
    shape_type = random.choice(shape_types)
    color = random.choice(colors)
    shape = Shape(shape_type, color)
    shapes.append(shape)

while True:
    for shape in shapes:
        shape.move()

    to_remove = set()
    for i in range(len(shapes)):
        for j in range(i + 1, len(shapes)):
            if i in to_remove or j in to_remove:
                continue
            if shapes[i].is_colliding_with(shapes[j]):

                shapes[i].destroy()
                shapes[j].destroy()
                to_remove.add(i)
                to_remove.add(j)

    shapes = [s for idx, s in enumerate(shapes) if idx not in to_remove]

    if len(shapes) <= 1:
        print("ok")
        break

    time.sleep(0.01)
