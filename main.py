import turtle

board = turtle.Screen()
board.bgcolor("light blue")
board.title("Board")

cursor = turtle.Turtle()

def turtle_forward():
    cursor.forward(100)


def turtle_right():
    cursor.right(5)

def turtle_left():
    cursor.left(5)

def clear_screen():
    cursor.clear()


def home():
    cursor.penup()
    cursor.home()
    cursor.pendown()

def penup():
    cursor.penup()


def pendown():
    cursor.pendown()











board.listen()
board.onkey(fun=turtle_forward , key="space")
board.onkey(turtle_right, key="Right")
board.onkey(turtle_left,key="Left")
board.onkey(fun=clear_screen,key="Up")
board.onkey(fun=home,key="h")
board.onkey(fun=penup,key="w")
board.onkey(fun=pendown,key="s")

turtle.mainloop()
board.done()