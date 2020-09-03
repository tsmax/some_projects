class Brick:
    def __init__(self, x, y, color):
        """ Builder of Brick instance
            x, y  --  coords of brick on battlefield
            color  --  color of brick
        """

        self.x, self.y = x, y
        self.color = color



class Ball:
    def __init__(self, x, y, color):
        """ Builder of Ball instance
            x, y  --  coords of ball on battlefield
            color  --  color of ball
        """

        self.x, self.y = x, y
        self.color = color


class Platform:
    def __init__(self, x, y, color):
        """ Builder of Platform instance
            x, y  --  coords of platform on battlefield
            color  --  color of platform
        """

        self.x, self.y = x, y
        self.color = color
