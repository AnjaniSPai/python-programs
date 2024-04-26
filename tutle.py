import turtle
import colorsys
s=turtle.Turtle()
turtle.bgcolor("Black")
s.color("white")
h=0.0
s.speed(0)
for i in range(200):
    s.color(colorsys.hsv_to_rgb(h,1,1))
    for j in range(4):
        s.forward(i)
        s.right(90)
    s.right(4)
    h+=0.002
turtle.mainloop()