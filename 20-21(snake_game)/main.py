import time
from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard


sc = Screen()
sc.setup(width=600, height=600)
sc.bgcolor("black")
sc.title("Snake baba rockstar")
sc.tracer(0)

snake = Snake()
food = Food()

sc.listen()
sc.onkey(snake.up, "Up")
sc.onkey(snake.down, "Down")
sc.onkey(snake.right, "Right")
sc.onkey(snake.left, "Left")

score = Scoreboard()
scr_cnt = 0
score.score_value(str(scr_cnt))
game_on = True

while game_on:
    sc.update()
    time.sleep(0.1)

    snake.move()

    if snake.head.distance(food) < 15:
        food.refresh()
        scr_cnt += 1
        snake.extend()

    score.score_value(str(scr_cnt))

    if snake.head.xcor() > 280 or snake.head.xcor() < -290 or snake.head.ycor() > 290 or snake.head.ycor() < -280:
        game_on = False
        score.game_over()

    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 10:
            game_on = False
            score.game_over()

sc.exitonclick()
