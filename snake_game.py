import turtle
import time
from random import randint

# moving to left
def left():
    if snake[0].heading() == 90:
        snake[0].left(90)
    elif snake[0].heading() == 270:
        snake[0].right(90)

# moving to right
def right():
    if snake[0].heading() == 270:
        snake[0].left(90)
    elif snake[0].heading() == 90:
        snake[0].right(90)

# moving to up
def up():
    if snake[0].heading() == 0:
        snake[0].left(90)
    elif snake[0].heading() == 180:
        snake[0].right(90)

# moving to down
def down():
    if snake[0].heading() == 180:
        snake[0].left(90)
    elif snake[0].heading() == 0:
        snake[0].right(90)


def add():  # adding a new part to the snake
    add_body = turtle.Turtle(shape="square")
    add_body.color("white")
    add_body.penup()
    add_body.goto(snake[i - 1].xcor() + 20, snake[i - 1].ycor())
    add_body.speed(0)
    snake.append(add_body)


window = turtle.Screen()
window.bgcolor("black")
window.setup(height=600, width=600)
window.tracer(0)

# moving
window.listen()
window.onkey(key="Left", fun=left)
window.onkey(key="Right", fun=right)
window.onkey(key="Up", fun=up)
window.onkey(key="Down", fun=down)

food = turtle.Turtle(shape="circle")
food.color("blue")
food.penup()
food.shapesize(0.5)
food.goto(randint(-250, 250), randint(-250, 250))

score = 0
score_board = turtle.Turtle()
score_board.color("white")
score_board.penup()
score_board.hideturtle()

# creating the snake
snake = []
for i in range(3):
    
    # snake's head
    if i == 0:
        head = turtle.Turtle(shape="square")
        head.color("red")
        head.penup()
        head.goto(0, 0)
        snake.append(head)
    
    # snake's body
    else:
        body = turtle.Turtle(shape="square")
        body.color("white")
        body.penup()
        body.goto(snake[i - 1].xcor() + 20, snake[i - 1].ycor())
        snake.append(body)
live = True
while live:
    
    for i in range(len(snake) - 1, 0, -1):
        new_x = snake[i - 1].xcor()
        new_y = snake[i - 1].ycor()
        snake[i].goto(new_x, new_y)
    
    snake[0].forward(20)
    # Detect collision with tail
    for i in range(4, len(snake)):
        if snake[0].xcor() == snake[i].xcor() and snake[0].ycor() == snake[i].ycor():
            live = False
    
    # Detect collision with food
    if snake[0].distance(food) <= 20:
        score += 1
        add()
        food.goto(randint(-250, 250), randint(-250, 250))
        i = 0
        # food and snake being in different places
        while i < len(snake):
            if snake[i].distance(food) < 15:
                food.goto(randint(-250, 250), randint(-250, 250))
                i = 0
            i += 1
    score_board.clear()
    score_board.goto(0, 270)
    score_board.write(f"SCORE : {score}", align="center", font=("arial", 20, "normal"))
    
    # Detect collision with wall
    if snake[0].ycor() < -270 or snake[0].ycor() > 270 or snake[0].xcor() < -270 or snake[0].xcor() > 270:
        live = False
    
    window.update()
    time.sleep(0.15 - (score * .005))

game_over = turtle.Turtle()
game_over.color("white")
game_over.penup()
game_over.hideturtle()
game_over.write("GAME OVER", align="center", font=("arial", 25, "normal"))
window.exitonclick()
