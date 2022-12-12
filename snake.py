from turtle import Turtle

# Create Position as Constant
STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0

class Snake:

    def __init__(self):
        """Models for Snake Game"""
        self.segments = []
        # self.heading = 0
        self.create_snake()
        self.head = self.segments[0]

    def create_snake(self):
        for position in STARTING_POSITIONS:
            self.add_segment(position)

    def add_segment(self, position):
        tim = Turtle(shape="square")
        tim.color("white")
        # tim.speed("fastest")
        tim.pu()
        tim.goto(position)
        self.segments.append(tim)

    def extend(self):
        self.add_segment(self.segments[-1].position())

    def move(self):
        """Move Snake"""
        for seg_num in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[seg_num - 1].xcor()
            new_y = self.segments[seg_num - 1].ycor()
            self.segments[seg_num].goto(new_x, new_y)

        # self.segments[0].setheading(self.heading)
        # self.segments[0].fd(MOVE_DISTANCE)
        self.head.fd(MOVE_DISTANCE)

    def up(self):
        """Set Heading to 90 degree"""
        if self.head.heading() != DOWN:
            self.head.setheading(UP)
            # self.heading = 90

    def left(self):
        """Set Heading to 180 degree"""
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def down(self):
        """Set Heading to 270 degree"""
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def right(self):
        """Set Heading to 0 degree"""
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)

