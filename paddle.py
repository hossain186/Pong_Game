from turtle import Turtle
class Paddle(Turtle):

    def __init__(self,position):
        super().__init__()
        self.position = position
        self.create_paddle()


    def create_paddle(self):

        self.shape("square")
        self.color("white")
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.penup()
        self.goto(self.position, 0)

    def paddle_up(self):
        new_y = self.ycor() + 20
        if self.ycor() <280:
            self.goto(self.xcor(), new_y)

    def paddle_down(self):
        new_y = self.ycor() - 20
        self.goto(self.xcor(), new_y)

