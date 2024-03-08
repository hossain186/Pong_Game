from turtle import Turtle, Screen
from paddle import  Paddle
from ball import  Ball
import  time
from scoreBoard import ScoreBoard

screen = Screen()
screen.bgcolor("black")

screen.setup(800,600)

screen.title("Pong Game")
screen.tracer(0)

r_paddle = Paddle(350)
l_paddle = Paddle(-350)


screen.listen()
screen.onkeypress(r_paddle.paddle_up, "Up")
screen.onkeypress(r_paddle.paddle_down, "Down")

screen.onkeypress(l_paddle.paddle_up, "w")
screen.onkeypress(l_paddle.paddle_down, "s")

#score board

score = ScoreBoard()



# Now create ball

ball = Ball()






game_is_on = True

while game_is_on:
    time.sleep(ball.move_speed)
    screen.update()

    ball.move()

    # detect collision with wall
    if ball.ycor()>280 or ball.ycor()<-280 :

        #need to bounce
        ball.bounce_y()

    # collision with right paddle


    elif ball.distance(r_paddle)<50 and ball.xcor()>320 or ball.distance(l_paddle)<50 and ball.xcor()<-320:
        ball.bounce_x()






    # detect r paddle misses
    elif ball.xcor()>390 :
        score.increase_l_score()


        ball.reset_position()
    #detect l paddle misses
    elif ball.xcor()<-390:
        score.increase_r_score()

        ball.reset_position()



    print(ball.move_speed)




screen.exitonclick()




