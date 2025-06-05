import turtle


screen = turtle.Screen()
screen.title("Sierpinski Triangle")
screen.bgcolor("white")
t = turtle.Turtle()
t.speed(0)
t.hideturtle()
t.color("red")


def draw_triangle(points):
    t.penup()
    t.goto(points[0])
    t.pendown()
    for i in range(1, 3):
        t.goto(points[i])
    t.goto(points[0])


def midpoint(p1, p2):
    return ((p1[0] + p2[0]) / 2, (p1[1] + p2[1]) / 2)

def sierpinski(points, depth):
    if depth == 0:
        draw_triangle(points)
    else:
     
        p1 = midpoint(points[0], points[1])
        p2 = midpoint(points[1], points[2])
        p3 = midpoint(points[2], points[0])

        sierpinski([points[0], p1, p3], depth - 1)
        sierpinski([p1, points[1], p2], depth - 1)
        sierpinski([p3, p2, points[2]], depth - 1)

points = [(-200, -150), (200, -150), (0, 200)]

sierpinski(points, 5)

screen.exitonclick()