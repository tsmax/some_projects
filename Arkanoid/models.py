class Brick:
    def __init__(self, x, y, color):
        """ Builder of Brick instance
            x, y  --  coords of the top left corner of brick on battlefield
            color  --  color of brick
        """

        self.x, self.y = x, y
        self.width, self.height = 40, 20
        self.color = color


class Ball:
    def __init__(self, x, y, color):
        """ Builder of Ball instance
            x, y  --  coords of ball's center on battlefield
            r -- radius of ball
            color  --  color of ball
        """

        self.x, self.y = x, y
        self.r = 3
        self.color = color


class Platform:
    def __init__(self, x, y, color):
        """ Builder of Platform instance
            x, y  --  coords of the top left corner of platform on battlefield
            color  --  color of platform
        """

        self.x, self.y = x, y
        self.width, self.height = 40, 10
        self.color = color
