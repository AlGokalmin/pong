from turtle import Screen
import time
from paddle import Paddle
from ball import Ball
from constants import HEIGHT, WIDTH

# Creating the main screen
height = HEIGHT
width = WIDTH

screen = Screen()
screen.bgcolor("black")
screen.setup(width, height)
screen.title("Pong")
screen.tracer(0)

# Setting the paddles
r_paddle = Paddle((350, 0))
l_paddle = Paddle((-350, 0))

# Setting the ball
ball = Ball((0, 0))

# Moving the paddles
screen.listen()
screen.onkeypress(r_paddle.move_up_r, "Up")
screen.onkeypress(r_paddle.move_down_r, "Down")
screen.onkeypress(l_paddle.move_up_l, "w")
screen.onkeypress(l_paddle.move_down_l, "s")


# Loop
game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    ball.move()

screen.exitonclick()
