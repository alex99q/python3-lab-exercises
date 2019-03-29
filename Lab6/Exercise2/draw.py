import turtle


class Draw(turtle.Turtle):
    def __init__(self):
        turtle.Turtle.__init__(self)
        self.color("blue")
        self.hideturtle()

    def draw_pixel(self, set_color):
        current_color = self.pencolor()

        self.color(set_color)
        self.forward(1)

        self.color(current_color)

    def draw_centered_line(self, length):
        x_to_change = (length / 2) * -1

        self.penup()
        self.goto(x_to_change, 0)
        self.pendown()
        self.forward(length)

    def draw_triangle(self):
        for x in range(3):
            if x == 0:
                self.forward(100)
            else:
                self.forward(200)

            self.left(120)

        self.forward(100)

    def draw_rectangle(self):
        for x in range(5):
            if x == 2:
                self.forward(400)
            else:
                self.forward(200)

            if x < 4:
                self.left(90)

    def draw_centered_circle(self, radius):
        y_to_change = radius * -1

        self.penup()
        self.goto(0, y_to_change)
        self.pendown()

        self.circle(radius)