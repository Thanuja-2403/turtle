import turtle
screen=turtle.Screen()
screen.title("turtle drawing")
screen.bgcolor("lightblue")
screen.bgpic("kjc.png")
t=turtle.Turtle()
t.penup()
t.goto(0,-100)
t.pendown()
t.color("red")
t.begin_fill()
t.circle(100)
t.hideturtle()
t.end_fill()
t.hideturtle()
turtle.done()


