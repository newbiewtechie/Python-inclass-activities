import turtle
turtle.Screen().bgcolor("pink")
turtle.Screen().setup(300, 400)
polygon = turtle.Turtle()
numsides = 6
sidelength = 70
angle = 360.0 / numsides
for i in range(numsides):
    polygon.forward(sidelength)
    polygon.right(angle)
turtle.done()