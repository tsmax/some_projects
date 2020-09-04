from Arkanoid.views import MainAppView, BattleFieldView
from Arkanoid.views import (WINDOW_WIDTH, PLATFORM_LINE_ANCHORPOINT_X, PLATFORM_LINE_ANCHORPOINT_Y,
                           BRICKS_FIELD_ANCHORPOINT_X, BRICKS_FIELD_ANCHORPOINT_Y, BRICKS_FIELD_WIDTH, BRICKS_FIELD_HEIGHT)

from Arkanoid.models import Ball, Brick, Platform


class ArkanoidApp:
    def __init__(self):
        """ Constructor of ArkanoidApp
            app_view, battlefield_view, gamemenu_view  --  GUI objects
            bricks  --  list of current Brick objects
            balls  --  list of current Ball objects
            platform  --  Platform objects

        """

        self.app_view, self.battlefield_view, self.gamemenu_view = None, None, None
        self.bricks, self.balls, self.platform = [], [], None

        self.app_view = MainAppView()

        self.start_game()

        self.app_view.mainloop()

    def create_new_game(self):
        """ Function clean previous battlefield and create new one """
        self.battlefield_view.clean()

        for x in range(0, BRICKS_FIELD_WIDTH, 40):
            for y in range(BRICKS_FIELD_ANCHORPOINT_Y, BRICKS_FIELD_ANCHORPOINT_Y + BRICKS_FIELD_HEIGHT, 20):
                brick = Brick(x, y, 'red')
                self.bricks.append(brick)

        self.platform = Platform(PLATFORM_LINE_ANCHORPOINT_X, PLATFORM_LINE_ANCHORPOINT_Y, 'black')

        self.battlefield_view.draw_platform(self.platform)
        self.battlefield_view.draw_bricks(self.bricks)

    def start_game(self):
        self.app_view.start_game()
        self.battlefield_view = self.app_view.battlefield_view
        self.gamemenu_view = self.app_view.gamemenu_view

        self.create_new_game()


def start_game(self):
        self.app_view.start_game()
        self.battlefield_view = self.app_view.battlefield_view
        self.gamemenu_view = self.app_view.gamemenu_view


def main():
    """ Main function of module.
        Create ArkanoidApp
    """
    app = ArkanoidApp()


if __name__ == '__main__':
    main()
