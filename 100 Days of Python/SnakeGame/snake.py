from turtle import Turtle

STARTING_POSITIONS = [(20, 0), (0, 0), (-20, 0)]
MOVE_DISTANCE = 20


class Snake:

    def __init__(self):
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]

    def create_snake(self):
        for position in STARTING_POSITIONS:
            self.add_segment(position)

    def add_segment(self, position):
        new_segment = Turtle("square")
        new_segment.color("white")
        new_segment.penup()
        new_segment.goto(position)
        self.segments.append(new_segment)

    def move(self):
        for segment_num in range(len(self.segments) - 1, 0, -1):
            next_position = self.segments[segment_num - 1].position()
            self.segments[segment_num].goto(next_position)
        self.segments[0].forward(MOVE_DISTANCE)

    def up(self):
        if self.head.heading() not in (90.0, 270.0):
            self.head.setheading(90)

    def down(self):
        if self.head.heading() not in (90.0, 270.0):
            self.head.setheading(270)

    def left(self):
        if self.head.heading() not in (0.0, 180.0):
            self.head.setheading(180)

    def right(self):
        if self.head.heading() not in (0.0, 180.0):
            self.head.setheading(0.0)

    def extend(self):
        self.add_segment(self.segments[-1].position())
