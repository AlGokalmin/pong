from turtle import Turtle


class Ball(Turtle):
    """
    Creating a ball, setting is shape, color and position
    """

    def __init__(self, position):
        super().__init__()
        self.penup()
        self.shape("circle")
        self.color("white")
        self.goto(position)

    def move(self):
        """
        Moving the ball upper right corner.
        :return:
        """
        new_x = self.xcor() + 10
        new_y = self.ycor() + 10
        self.goto(new_x, new_y)
