import turtle

wn = turtle.Screen()

tt1 = turtle.Turtle()
tt1.shape('turtle')
tt1.speed("slowest")
tt1.fillcolor('red')
tt1.begin_fill()


tt1.left(90)
tt1.circle(100, 180, 20)
tt1.left(45)
tt1.goto(0,-200)
tt1.left(90)
tt1.goto(200,0)
tt1.left(45)
tt1.circle(100,180,50)
tt1.end_fill()




wn.exitonclick()
