from Arkanoid.views import MainAppView, BattleFieldView
from Arkanoid.views import (WINDOW_WIDTH, PLATFORM_ANCHORPOINT_X, PLATFORM_ANCHORPOINT_Y,
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
        self.bricks, self.platform, self.ball = [], None, None
        self.right_key, self.left_key = False, False

        self.app_view = MainAppView()

        self.create_game_window()
        self.create_new_game()

        self.app_view.mainloop()

    def game_loop(self):
        """ Main loop of game """
        self.ball.move(self.platform)
        self.battlefield_view.update_ball(self.ball)

        destroyed_brick = self.ball.hittest_brick(self.bricks)
        if destroyed_brick:
            self.destroy_brick(destroyed_brick)

        self.platform.move()
        self.battlefield_view.update_platform(self.platform)

        self.app_view.after(10, self.game_loop)

    def destroy_brick(self, destroyed_brick):
        self.battlefield_view.delete_brick(destroyed_brick)
        del self.bricks[self.bricks.index(destroyed_brick)]

    def set_move_direction_platform_press(self, event):
        if event.keysym == 'Right':
            if not self.right_key:
                self.right_key = True
                if not (self.left_key and self.platform.contact_walls()):
                    self.platform.Vx += 2
        elif event.keysym == 'Left':
            if not self.left_key:
                self.left_key = True
                if not (self.right_key and self.platform.contact_walls()):
                    self.platform.Vx -= 2

    def set_move_direction_platform_release(self, event):
        if event.keysym == 'Right':
            self.right_key = False
            if not self.platform.contact_walls():
                self.platform.Vx -= 2
            elif self.platform.contact_walls() and self.left_key:
                self.platform.Vx -= 2
        if event.keysym == 'Left':
            self.left_key = False
            if not self.platform.contact_walls():
                self.platform.Vx += 2
            elif self.platform.contact_walls() and self.right_key:
                self.platform.Vx += 2


    def game_binding(self):
        """ Binds all events while game """
        self.app_view.bind('<Right>', self.set_move_direction_platform_press)
        self.app_view.bind('<Left>', self.set_move_direction_platform_press)
        self.app_view.bind('<KeyRelease>', self.set_move_direction_platform_release)

    def create_new_game(self):
        """ Function clean previous battlefield and create new one """
        self.battlefield_view.clean()
        self.game_binding()

        for x in range(0, BRICKS_FIELD_WIDTH, 40):
            for y in range(BRICKS_FIELD_ANCHORPOINT_Y, BRICKS_FIELD_ANCHORPOINT_Y + BRICKS_FIELD_HEIGHT, 20):
                brick = Brick(x, y, 'red')
                self.bricks.append(brick)

        self.platform = Platform(PLATFORM_ANCHORPOINT_X, PLATFORM_ANCHORPOINT_Y, 'black')

        self.ball = Ball(self.platform.x + self.platform.width / 2, self.platform.y - 3, 'black')

        self.battlefield_view.draw_platform(self.platform)
        self.battlefield_view.draw_bricks(self.bricks)
        self.battlefield_view.draw_ball(self.ball)

        self.game_loop()

    def create_game_window(self):
        """ Creates GUI objects for game """
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
