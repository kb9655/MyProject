import turtle
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

def grid(x,y):

    count = 0
    while(count< 6):
        moveto(x,y-100*count)
        row(500)
        count=count+1
    count = 0
    while(count< 6):
        moveto(x+100*count,y)
        col(500)
        count=count+1
    
    
grid(0,500)


turtle.exitonclick()





