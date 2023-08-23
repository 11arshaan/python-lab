from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard
import math
import time

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.tracer(0)  # disables auto-update

snake = Snake()
food = Food()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

game_on = True

while game_on:
    screen.update()
    time.sleep(0.1)
    snake.move()

    # Detect collision with food
    if snake.head.distance(food) < 15:
        snake.extend()
        scoreboard.increase_score()
        food.refresh()

    # Detect collision with tail
    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 10:
            game_on = False
            scoreboard.game_over()

    # Detect collision with wall
    if abs(snake.head.xcor()) >= 290 or abs(snake.head.ycor()) >= 290:
        print(scoreboard.score)
        scoreboard.game_over()
        game_on = False

screen.exitonclick()
