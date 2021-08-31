import turtle
from turtle import *

window = turtle.Screen()
window.bgcolor("#005c99")
window.setup(width=1920, height=1400, startx=10, starty=0.5)
plato = turtle.Turtle()  # A good mathy name for our turtle
plato.hideturtle()
plato.color("white","")

scale = 5  # This isn't a turtle module setting.  This is just for us.

fred = turtle.Turtle()  # A good mathy name for our turtle
fred.hideturtle()
fred.color("yellow","")
scale = 5  # This isn't a turtle module setting.  This is just for us.

# Move the little buddy over to the left side to give him more room to work
plato.penup()
plato.setpos(-650, 0)
plato.pendown()

fred.penup()
fred.setpos(650,0)
fred.pendown()

current = 0   # Here's how we know where we are
seen = set()  # Here's where we'll keep track of where we've been

# Step increases by 1 each time
for step_size in range(1, 200):

    backwards = current - step_size
    
    # Step backwards if its positive and we've never been there before
    if backwards > 0 and backwards not in seen:
        plato.setheading(90)  # 90 degrees is pointing straight up
        fred.setheading(270)
         # 180 degrees means "draw a semicircle"
        plato.circle(scale * step_size/2, 180)
        fred.circle(scale * step_size/2 , 180)
        current = backwards
        seen.add(current)

    # Otherwise, go forwards
    else:
        plato.setheading(270)  # 270 degrees is straight down
        fred.setheading(90)
        plato.circle(scale * step_size/2, 180)
        fred.circle(scale * step_size/2, 180)
        current += step_size
        seen.add(current)


turtle.done()