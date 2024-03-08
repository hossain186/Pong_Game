from turtle import  Turtle

PADDLE_WIDTH = 1
PADDLE_HEIGHT =1
class Ball(Turtle):
    def __init__(self):
        super().__init__()

        self.create_ball()
        self.xmove  = 10
        self.ymove =10
        self.move_speed =.1

    def create_ball(self):

        self.shape("circle")
        self.color("white")
        self.shapesize(PADDLE_WIDTH, PADDLE_HEIGHT)
        self.penup()
        self.setx(0)
        self.sety(0)

    def move(self, ):

        new_x = self.xcor()+self.xmove
        new_y = self.ycor()+self.ymove

        self.goto(new_x, new_y)
    def bounce_y(self):

        self.ymove*=-1

    def bounce_x(self):
        self.xmove*=-1
        self.move_speed*=.9

    def reset_position(self):
        self.goto(0,0)
        self.move_speed = .1
        self.bounce_x()



