import time
from turtle import Screen
from snake import Snake

scr = Screen()
scr.setup(width=600, height=600)
scr.title(titlestring="Snake Game")
scr.bgcolor("black")
scr.tracer(0)

# tim = Turtle(shape="square")
# tim.color("white")
# print(tim.resizemode())
# print(tim.shapesize())
# tim.resizemode("user")
# tim.shapesize(0.2, 0.2, 1)
# tim.pu()
# for x in range(0, 3):
#     tim.fd(5)
#     tim.stamp()

snake = Snake()

scr.listen()
scr.onkey(snake.up, "Up")
scr.onkey(snake.down, "Down")
scr.onkey(snake.left, "Left")
scr.onkey(snake.right, "Right")


game_is_on = True
while game_is_on:
    scr.update()
    time.sleep(0.1)

    snake.move()

scr.exitonclick()
