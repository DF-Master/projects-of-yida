import turtle

wn=turtle.Screen()

tt1 = turtle.Turtle()
tt1.shape('turtle')
tt1.speed("fast")

tt1.penup()
tt1.goto(-30,30)
tt1.pendown()
tt1.goto(-80,80)
tt1.goto(-130,30)
tt1.penup()
tt1.goto(30,30)
tt1.pendown()
tt1.goto(80,80)
tt1.goto(130,30)
tt1.penup()
tt1.goto(200,0)
tt1.pendown()
tt1.setheading(90)
tt1.circle(200,360,100)
tt1.penup()

tt1.goto(130,-30)

tt1.pendown()
tt1.fillcolor('red')
tt1.begin_fill()
tt1.setheading(225)
tt1.circle(-130*1.414,90,50)
tt1.setheading(270)
tt1.circle(130,180,100)
tt1.goto(130,-30)
tt1.end_fill()

wn.exitonclick()

