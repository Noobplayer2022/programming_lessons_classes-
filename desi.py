import turtle as t

t.color("red")
for _ in range(3):
    t.forward(100)
    t.left(120)
    t.circle(100)

t.color("blue")
t.circle(50)
t.penup()
t.forward(150)
t.pendown()
t.circle(50)
t.penup()
t.goto(0,-150)
t.pendown()
t.circle(50)
t.penup()
t.goto(0,-125)
t.pendown()
t.circle(30)
t.done()

import turtle as t
# t.color("blue")
# num = int(input("enter num: "))
# if num > 2:
#     for _ in range(num):
#         t.forward(100)
#         t.left(360/num)
#     for test in range(num):
#         t.backward(100)
#         t.left(360/num)
# t.done()


def draw_shape():
    t.color("blue")
    num = int(input("enter num: "))
    if num > 2:
        while True:
            n = 0
            
            for _ in range(num):
                t.forward(100)
                t.left(360/num)
            for _ in range(num):
                t.backward(100)
                t.left(360/num+100)
            n +=100

    t.done()

draw_shape()





        