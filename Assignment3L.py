#Roman Dattilo

#CS175L

#Stop sign




import turtle

num_sides=8
length=100
angle=45
window_width=400
window_height=400

turtle.setup(window_width,window_height)

turtle.penup()
turtle.goto(-100, 241)
turtle.pendown()

turtle.pensize(5)
turtle.color("gray", "darkred")
turtle.begin_fill()
for y in range(num_sides):
   turtle.pendown()
   turtle.forward(length)
   turtle.right(angle)
turtle.end_fill()

turtle.penup()
turtle.goto(-135,75)
turtle.color("white")
turtle.write("STOP" ,font=("Comic Sans MS", 50))


