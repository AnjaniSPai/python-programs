import turtle
s=turtle.Turtle()
s.shape("turtle")
s.speed(0)
turtle.bgcolor("light blue")
s.color("white")
s.forward(100)
for i in range(400):
   s.circle(i)
   s.right(50)
turtle.mainloop()
 
