import turtle
import random


t = turtle.Turtle()
t.speed(0) 
turtle.bgcolor("black")  
t.color("coral") 
t.pensize(2)  


def draw_coral_branch(length, level):
    if level == 0: 
        return
    
    t.forward(length)  
    current_pos = t.position()  
    current_heading = t.heading()  
    

    t.left(45)
    draw_coral_branch(length * 0.7, level - 1)  
    

    t.penup()
    t.setposition(current_pos)
    t.setheading(current_heading)
    t.pendown()
    

    t.right(45)  
    draw_coral_branch(length * 0.7, level - 1) 
    
 
    t.penup()
    t.setposition(current_pos)
    t.setheading(current_heading + random.uniform(-10, 10))  
    t.pendown()


t.penup()
t.goto(0, -200) 
t.pendown()
t.setheading(90)  


draw_coral_branch(100, 5)  


t.hideturtle()
turtle.done()