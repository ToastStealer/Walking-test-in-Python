import turtle as t
t.bgcolor('lime')
t.title("Cube Guy")

player = t.Turtle()
player.shape('square')
player.color('red')
player.shapesize(1,1)
player.speed(0)
player.penup()

def up():
    player.setheading(90)
    player.forward(20)

def down():
    player.setheading(270)
    player.forward(20)

def left():
    player.setheading(180)
    player.forward(20)

def right():
    player.setheading(0)
    player.forward(20)

t.listen()
t.onkey(up, 'Up')
t.onkey(down, 'Down')
t.onkey(left, 'Left')
t.onkey(right, 'Right')
