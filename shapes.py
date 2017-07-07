from turtle import *
import math

# Name your Turtle.
t = Turtle()

# Set Up your screen and starting position.
t.penup()
setup(1500,1500)
x_pos = -200
y_pos = -200
x= -500
y= -500
t.setposition(x_pos, y_pos)

### Write your code below:
def square (steps, angle, speed):
    begin_fill()
    t.pendown()
    t.speed(speed)

    t.setposition(x_pos, y_pos)
    t.forward(steps)
    t.right(angle)
    t.forward(steps)
    t.right(angle)
    t.forward(steps)
    t.right(angle)
    t.forward(steps)
    t.penup()
    end_fill()

    print("this is the square")

square(140, 90, 30)


answer = input("How many sides")
question= int(answer)
angle= 360//question
color3= input("What color")



begin_fill()
t.pendown()
fillcolor (color3)
for hops in range(question):
    right(angle)
    forward(90)
t.penup()
end_fill()

begin_fill()
t.pendown()
color ('green', 'aqua')
for hops in range(3):
    left(120)
    forward(200)
t.penup()
end_fill()

begin_fill()
t.pendown()
color ( 'purple', 'silver')
for hops in range(6):
    forward(200)
    left(60)
t.penup()
t.setposition(x, y)
end_fill()

begin_fill()
while True:
    color ( 'black', 'pink')
    t.pendown()
    forward(200)
    left(200)
    if abs(pos()) < 1:
        break

end_fill()
done()





# Close window on click.
exitonclick()
