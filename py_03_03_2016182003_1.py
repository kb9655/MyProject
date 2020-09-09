import turtle
def ㄱ():
    turtle.setheading(0)
    turtle.forward(100)
    turtle.right(90)
    turtle.forward(100)

def moveto(x,y):
    turtle.penup()
    turtle.goto(x,y)
    turtle.pendown()

def row(x):
    turtle.setheading(0)
    turtle.forward(x)

def col(x):
    turtle.setheading(-90)
    turtle.forward(x)
    
	
moveto(-300,100)
ㄱ()
moveto(-250,0)
col(50)
moveto(-350,-50)
row(200)

moveto(-100,100)
ㄱ()
moveto(0,80)
row(50)
moveto(0,40)
row(50)
moveto(50,150)
col(200)
moveto(-50,-100)
turtle.circle(50)

moveto(100,100)
col(100)
moveto(200,100)
col(100)
moveto(100,50)
row(100)
moveto(100,0)
row(100)
moveto(250,150)
col(200)
moveto(120,-50)
col(100)
row(150)

turtle.exitonclick()

