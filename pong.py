# This is a sample Python script.

# Press Maiusc+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

# Simple Pong in Python 3
# By @Andrea Antonio Perrelli

import turtle
import winsound

wn = turtle.Screen()
wn.title("Pong by @Andrea Antonio Perrelli")
wn.bgcolor("black")
wn.setup(width=800, height=600)
wn.tracer(0)

# game state
game_state = True
player_winner = ""
esc_game = False

# Score
score_a = 0
score_b = 0

# speed of the ball
speed_ball = 0

# Paddle A
paddle_a = turtle.Turtle()
paddle_a.speed(0)
paddle_a.shape("triangle")
paddle_a.color("green")
paddle_a.shapesize(stretch_wid=5, stretch_len=1)
paddle_a.penup()
paddle_a.goto(-350, 0)
# Paddle B
paddle_b = turtle.Turtle()
paddle_b.speed(0)
paddle_b.shape("triangle")
paddle_b.color("green")
paddle_b.shapesize(stretch_wid=5, stretch_len=1)
paddle_b.penup()
paddle_b.goto(+350, 0)

# Ball
ball = turtle.Turtle()
ball.speed(speed_ball)
ball.shape("triangle")
ball.color("green")
ball.penup()
ball.goto(0, 0)
ball.dx = 0.1
ball.dy = -0.1

# Pen

pen = turtle.Turtle()
pen.speed(0)
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0, 260)
pen.write("Player A : 0 Player B : 0", align="center", font=("Sans", 24, "normal"))


# Function

def paddle_a_up():
    y = paddle_a.ycor()
    y += 20
    paddle_a.sety(y)


def paddle_a_down():
    y = paddle_a.ycor()
    y -= 20
    paddle_a.sety(y)


def paddle_b_up():
    y = paddle_b.ycor()
    y += 20
    paddle_b.sety(y)


def paddle_b_down():
    y = paddle_b.ycor()
    y -= 20
    paddle_b.sety(y)


def winner_screen(winner):
    pen.clear()
    ball.clear()
    paddle_a.clear()
    paddle_b.clear()
    pen.write(
        "The winner is {} , you can exit the game by pressing Esc".format(winner, align="center",
                                                                                                 font=(
                                                                                                 "Sans", 30, "normal")))
    wn.onkeypress(set_esc_game, "Escape")


def set_esc_game():
    global esc_game
    esc_game = True



# Keyboard binding
wn.listen()
wn.onkeypress(paddle_a_up, "w")
wn.onkeypress(paddle_a_down, "s")
wn.onkeypress(paddle_b_up, "Up")
wn.onkeypress(paddle_b_down, "Down")
# Main game loop
while game_state:
    wn.update()

    # Move the ball
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    # Border checking
    if ball.ycor() > 290:
        ball.sety(290)
        ball.dy *= -1
        speed_ball += 1
        ball.speed(speed_ball)
        winsound.PlaySound("bounce.wav", winsound.SND_ASYNC)

    if ball.ycor() < -290:
        ball.sety(-290)
        ball.dy *= -1
        speed_ball += 1
        ball.speed(speed_ball)
        winsound.PlaySound("bounce.wav", winsound.SND_ASYNC)

    if ball.xcor() > 390:
        ball.goto((0, 0))
        ball.dx *= -1
        score_a += 1
        speed_ball = 0
        ball.speed(speed_ball)
        pen.clear()
        pen.write("Player A : {} Player B : {}".format(score_a, score_b), align="center", font=("Sans", 24, "normal"))

    if ball.xcor() < -400:
        ball.goto((0, 0))
        ball.dx *= -1
        score_b += 1
        speed_ball = 0
        ball.speed(speed_ball)
        pen.clear()
        pen.write("Player A : {} Player B : {}".format(score_a, score_b), align="center", font=("Sans", 24, "normal"))

    # Paddle and ball collissions
    if ball.xcor() < -340 and paddle_a.ycor() + 50 > ball.ycor() > paddle_a.ycor() - 50:
        ball.dx *= -1
        speed_ball += 1
        ball.speed(speed_ball)
        winsound.PlaySound("bounce.wav", winsound.SND_ASYNC)

    elif ball.xcor() > 340 and paddle_b.ycor() + 50 > ball.ycor() > paddle_b.ycor() - 50:
        ball.dx *= -1
        speed_ball += 1
        ball.speed(speed_ball)
        winsound.PlaySound("bounce.wav", winsound.SND_ASYNC)

    if score_a == 10:
        game_state = False
        player_winner = "Player A"
    elif score_b == 10:
        game_state = False
        player_winner = "Player B"

while not game_state and not esc_game:
    wn.update()
    winner_screen(winner=player_winner)
