from Arkanoid.views import WINDOW_WIDTH, WINDOW_HEIGHT, GAMEMENU_ANCHORPOINT_Y, BRICKS_FIELD_ANCHORPOINT_Y
from random import randint

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
            Vx, Vy  --  projection of ball's speed (V)
            color  --  color of ball
        """

        self.x, self.y = x, y
        self.r = 3
        self.color = color
        self.Vx, self.Vy = 0, 0
        self.V = (self.Vx ** 2 + self.Vy ** 2) ** 0.5
        self.motion = False
        self.live = 1

    def move(self, platform):
        """ Change ball's coords depend of speed and contact with walls/platform """
        self.x += self.Vx
        self.y += self.Vy

        if self.x + self.Vx - self.r <= 0:
            self.x = 0 + self.r
            self.Vx = -self.Vx
        elif self.x + self.Vx + self.r >= WINDOW_WIDTH:
            self.x = WINDOW_WIDTH - self.r
            self.Vx = -self.Vx

        if self.y + self.Vy - self.r <= BRICKS_FIELD_ANCHORPOINT_Y:
            self.y = 0 + self.r
            self.Vy = -self.Vy
        elif self.y + self.Vy + self.r >= WINDOW_HEIGHT - (WINDOW_HEIGHT - GAMEMENU_ANCHORPOINT_Y):
            self.destroy_ball()

        if ((platform.x <= self.x + self.Vx <= platform.x + platform.width)
                and (platform.y + self.Vy >= self.y + self.Vy + self.r >= platform.y)):
            self.y = platform.y
            self.Vy = -randint(1, 3)
            self.Vx = randint(-3, 3)

    def hittest_brick(self, bricks):
        """ Check contact with brick and bounces ball """
        for brick in bricks:
            if ((self.y - self.r <= brick.y + brick.height) and
                    (self.y + self.r >= brick.y)):
                if brick.x <= self.x <= brick.x + brick.width:
                    self.Vy = -self.Vy
                    return brick

            if ((self.x - self.r <= brick.x + brick.width) and
                    (self.x + self.r >= brick.x)):
                if brick.y <= self.y <= brick.y + brick.height:
                    self.Vx = -self.Vx
                    return brick
        return None

    def destroy_ball(self):
        self.live = 0


class Platform:
    def __init__(self, x, y, color):
        """ Builder of Platform instance
            x, y  --  coords of the top left corner of platform on battlefield
            color  --  color of platform
            width, height  --  width, height of platform
        """

        self.x, self.y = x, y
        self.width, self.height = 40, 10
        self.color = color
        self.Vx = 0

    def move(self):
        if self.x + self.Vx < 0:
            self.x = 0
            self.Vx = 0
        elif self.x + self.Vx + self.width > WINDOW_WIDTH:
            self.x = WINDOW_WIDTH - self.width
            self.Vx = 0
        else:
            self.x += self.Vx

    def contact_walls(self):
        if self.x + self.Vx <= 0:
            return True
        elif self.x + self.Vx + self.width >= WINDOW_WIDTH:
            return True
        return False
