import time
from turtle import Turtle, Screen
from paddles import Paddle
from ball import Ball
from scoreboard import Scoreboard


ari = Turtle()
pg = Screen()
pg.setup(height=600, width=800)
pg.bgcolor("black")
pg.title("PONG")
pg.tracer()

ball = Ball()
score = Scoreboard()

paddle_r = Paddle()
paddle_r.position_("right")

paddle_l = Paddle()
paddle_l.position_("left")


pg.listen()
pg.onkey(paddle_r.up, "Up")
pg.onkey(paddle_r.down, "Down")

pg.onkey(paddle_l.up, "w")
pg.onkey(paddle_l.down, "s")

paddle_r.showturtle()
paddle_l.showturtle()

game_on = True

while game_on:
    time.sleep(ball.move_speed)
    pg.update()
    ball.move()

    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    if ball.distance(paddle_r) < 50 and ball.xcor() > 320 or ball.distance(paddle_l) < 50 and ball.xcor() < -320:
        ball.bounce_x()

    if ball.xcor() > 390:
        ball.resetting()
        ball.bounce_x()
        score.l_point()

    if ball.xcor() < -390:
        ball.resetting()
        ball.bounce_x()
        score.r_point()


pg.exitonclick()
