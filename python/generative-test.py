import turtle
from turtle import *

window = turtle.Screen()
window.bgcolor("#242424")
window.setup(width=2920, height=2920, startx=0.5, starty=0.5)
plato = turtle.Turtle()  # A good mathy name for our turtle
plato.hideturtle()
plato.color("white","")

scale = 5  # This isn't a turtle module setting.  This is just for us.

fred = turtle.Turtle()  
fred.hideturtle()
fred.color("white","")

leo = turtle.Turtle()  
leo.hideturtle()
leo.color("red","")

tom = turtle.Turtle()  
tom.hideturtle()
tom.color("red","")



# Move the little buddy over to the left side to give him more room to work
plato.penup()
plato.setpos(-250, 0)
plato.pendown()

fred.penup()
fred.setpos(250,0)
fred.pendown()

leo.penup()
leo.setpos(0,250)
leo.pendown()

tom.penup()
tom.setpos(0,-250)
tom.pendown()

current = 0   # Here's how we know where we are
seen = set()  # Here's where we'll keep track of where we've been

# Step increases by 1 each time
for step_size in range(1, 200):

    backwards = current - step_size
    
    # Step backwards if its positive and we've never been there before
    if backwards > 0 and backwards not in seen:
        plato.setheading(90)  # 90 degrees is pointing straight up
        fred.setheading(270)
        leo.setheading(0)
        tom.setheading(180)
         # 180 degrees means "draw a semicircle"
        plato.circle(scale * step_size/4, 150)
        fred.circle(scale * step_size/4 , 150)
        leo.circle(scale * step_size/4, 150)
        tom.circle(scale * step_size/4, 150)
        current = backwards
        seen.add(current)

    # Otherwise, go forwards
    else:
        plato.setheading(270)  # 270 degrees is straight down
        fred.setheading(90)
        leo.setheading(180)
        tom.setheading(0)
        plato.circle(scale * step_size/4, 150)
        fred.circle(scale * step_size/4, 150)
        leo.circle(scale * step_size/4, 150)
        tom.circle(scale * step_size/4, 150)
        current += step_size
        seen.add(current)


turtle.done()