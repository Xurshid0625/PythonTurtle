from turtle import Turtle, Screen

window = Screen()
window.title("Mening Oynam")

line = Turtle()
line.color("Blue")
line.pensize(5)
line.speed(0)
line.up()
line.goto(300, 300)
line.down()
line.goto(300, -300)
line.goto(-300, -300)
line.goto(-300, 300)
line.goto(300, 300)
line.hideturtle()

ball = Turtle()
ball.color("Yellow")
ball.shape("circle")
ball.up()
ball.goto(0, 0)

step_x = 3
step_y = 2

while True:

    x, y = ball.position()

    if x + step_x >= 300 or x + step_x <= -300:
        step_x = -step_y
    if y + step_y >= 300 or y + step_y <= -300:
        step_y = -step_y

    ball.goto(x + step_x, y + step_y)


window.mainloop()
