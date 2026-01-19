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


window.mainloop()
