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
        self.game_running = False
        self.lives = 3

        self.app_view = MainAppView()

        self.create_game_window()
        self.create_new_game()

        self.app_view.mainloop()

    def game_loop(self):
        """ Main loop of game """
        if self.game_running:
            self.ball.move(self.platform)
            self.battlefield_view.update_ball(self.ball)

            destroyed_brick = self.ball.hittest_brick(self.bricks)
            if destroyed_brick:
                self.destroy_brick(destroyed_brick)

            self.platform.move()
            self.battlefield_view.update_platform(self.platform)
        if self.ball.live == 1:
            self.app_view.after(10, self.game_loop)
        elif self.lives > 0:
            self.lives -= 1
            self.pause(None)
            self.battlefield_view.delete_ball()
            self.battlefield_view.delete_platform()
            self.set_start_position()
        else:
            self.end_game()

    def destroy_brick(self, destroyed_brick):
        self.battlefield_view.delete_brick(destroyed_brick)
        del self.bricks[self.bricks.index(destroyed_brick)]

    def set_move_direction_platform_press(self, event):
        if event.keysym == 'Right':
            if not self.right_key:
                self.right_key = True
                if not (self.left_key and self.platform.contact_walls()):
                    self.platform.Vx = 2
        elif event.keysym == 'Left':
            if not self.left_key:
                self.left_key = True
                if not (self.right_key and self.platform.contact_walls()):
                    self.platform.Vx = -2

    def set_move_direction_platform_release(self, event):
        if event.keysym == 'Right':
            self.right_key = False
            if self.left_key:
                self.platform.Vx = -2
            else:
                self.platform.Vx = 0
        if event.keysym == 'Left':
            self.left_key = False
            if self.right_key:
                self.platform.Vx = 2
            else:
                self.platform.Vx = 0

    def game_binding(self):
        """ Binds all events while game """
        self.app_view.bind('<Right>', self.set_move_direction_platform_press)
        self.app_view.bind('<Left>', self.set_move_direction_platform_press)
        self.app_view.bind('<KeyRelease>', self.set_move_direction_platform_release)

    def create_new_game(self):
        """ Function clean previous battlefield and create new one """
        self.battlefield_view.clean()
        self.game_binding()
        self.lives = 3

        for x in range(0, BRICKS_FIELD_WIDTH, 40):
            for y in range(BRICKS_FIELD_ANCHORPOINT_Y, BRICKS_FIELD_ANCHORPOINT_Y + BRICKS_FIELD_HEIGHT, 20):
                brick = Brick(x, y, 'red')
                self.bricks.append(brick)

        self.battlefield_view.draw_bricks(self.bricks)
        self.set_start_position()

    def set_start_position(self):
        self.platform = Platform(PLATFORM_ANCHORPOINT_X, PLATFORM_ANCHORPOINT_Y, 'black')

        self.ball = Ball(self.platform.x + self.platform.width / 2, self.platform.y - 3, 'black')

        self.battlefield_view.draw_platform(self.platform)
        self.battlefield_view.draw_ball(self.ball)

        self.game_loop()

    def create_game_window(self):
        """ Creates GUI objects for game """
        self.app_view.start_game()
        self.battlefield_view = self.app_view.battlefield_view
        self.gamemenu_view = self.app_view.gamemenu_view

        self.gamemenu_view.button_start.bind('<Button-1>', self.start)
        self.gamemenu_view.button_pause.bind('<Button-1>', self.pause)

    def end_game(self):
        pass

    def start(self, event):
        self.game_running = True
        if self.ball.Vy == 0:
            self.ball.Vx, self.ball.Vy = -1, -1

    def pause(self, event):
        self.game_running = False

    def empty_event(self, event):
        pass


def main():
    """ Main function of module.
        Create ArkanoidApp
    """
    app = ArkanoidApp()


if __name__ == '__main__':
    main()
