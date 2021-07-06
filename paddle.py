from turtle import Turtle


class Paddle(Turtle):
    """
    Creating a paddle.Input position for paddle
    """
    def __init__(self, position):
        super().__init__()
        self.shape("square")
        self.color("white")
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.penup()
        self.goto(position)

    def move_up_r(self):
        """
        Moving the right paddle up.
        :return:
        """
        new_y = self.ycor() + 20
        self.goto(self.xcor(), new_y)

    def move_down_r(self):
        """
        Moving the right paddle down.
        :return:
        """
        new_y = self.ycor() - 20
        self.goto(self.xcor(), new_y)

    def move_up_l(self):
        """
        Moving the left paddle up.
        :return:
        """
        new_y = self.ycor() + 20
        self.goto(self.xcor(), new_y)

    def move_down_l(self):
        """
        Moving the left paddle down.
        :return:
        """
        new_y = self.ycor() - 20
        self.goto(self.xcor(), new_y)
