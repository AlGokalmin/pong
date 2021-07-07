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
        self.x_move = 10
        self.y_move = 10

    def move(self):
        """
        Moving the ball upper right corner.
        :return:
        """
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(new_x, new_y)

    def bounce(self):
        self.y_move *= -1
