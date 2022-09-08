from turtle import *

speed(30)
width(7)
color("purple")

forward(200)
left (90)

forward(200)
left(90)

forward(200)
left(90)

forward(200)
left(90)


forward(70)
left(90)

begin_fill()
color("yellow")
forward(120)
right(90)
forward(60)
right(90)
forward(120)
end_fill()


penup()
goto(200, 200)
pendown()

color("red")
begin_fill()
right(150)
forward(200)
left(120)
forward(200)
end_fill()

penup()
goto(0, 0)
right(150)

goto(30, 0)
forward(150)
pendown()

color("Black")
begin_fill()

forward(25)
right(90)
forward(25)
right(90)
forward(25)
right(90)
forward(25)
end_fill()




exitonclick()