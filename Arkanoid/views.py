import tkinter as tk

""" NO CHANGE """

WINDOW_HEIGHT = 600
WINDOW_WIDTH = 400

BRICKS_FIELD_WIDTH, BRICKS_FIELD_HEIGHT = WINDOW_WIDTH, 100
BRICKS_FIELD_ANCHORPOINT_X, BRICKS_FIELD_ANCHORPOINT_Y = 0, 50
""" Bricks field if rectangle with coords (0;50) --> (400;150) """

PLATFORM_ANCHORPOINT_X, PLATFORM_ANCHORPOINT_Y = WINDOW_WIDTH//2 - 20, 440
""" Platform line's anchor point """

GAMEMENU_WIDTH, GAMEMENU_HEIGHT = WINDOW_WIDTH, 100
GAMEMENU_ANCHORPOINT_X, GAMEMENU_ANCHORPOINT_Y = 0, 500
""" Game menu field if rectangle with coords (0;500) --> (400;600) """


class MainAppView(tk.Tk):
    def __init__(self):
        super().__init__()
        self.geometry('{}x{}'.format(WINDOW_WIDTH, WINDOW_HEIGHT))
        self.resizable(width=False, height=False)

    def start_game(self):
        self.battlefield_view = BattleFieldView(self)
        self.gamemenu_view = GameMenuView(self)

    def play(self):
        pass

    def pause(self):
        pass


class BattleFieldView(tk.Canvas):
    def __init__(self, master):
        super().__init__(master, height=WINDOW_HEIGHT - (WINDOW_HEIGHT - GAMEMENU_ANCHORPOINT_Y), width=WINDOW_WIDTH,
                         bg='grey')
        self.master = master
        self.pack()

        self.platform, self.ball, self.bricks = None, None, {}
        self.lives_count = None

    def clean(self):
        self.delete('ALL')

    def draw_lives_count(self, lives):
        self.lives_count = self.create_text(WINDOW_WIDTH // 2, 25, text='lives: {}'.format(lives), font=15)

    def update_lives_count(self, lives):
        self.itemconfigure(self.lives_count, text='lives: {}'.format(lives))
        self.update()

    def draw_platform(self, platform):
        x1, y1 = platform.x, platform.y
        x2, y2 = x1 + platform.width, y1 + platform.height
        self.platform = self.create_rectangle(x1, y1, x2, y2, fill=platform.color)

    def draw_bricks(self, bricks):
        for brick in bricks:
            x1, y1 = brick.x, brick.y
            x2, y2 = x1 + brick.width, y1 + brick.height
            brick_id = self.create_rectangle(x1, y1, x2, y2, fill=brick.color)
            self.bricks[brick] = brick_id

    def draw_ball(self, ball):
        x1, y1 = ball.x - ball.r, ball.y - ball.r
        x2, y2 = ball.x + ball.r, ball.y + ball.r
        self.ball = self.create_oval(x1, y1, x2, y2, fill=ball.color)

    def update_platform(self, platform):
        x1, y1 = platform.x, platform.y
        x2, y2 = x1 + platform.width, y1 + platform.height
        self.coords(self.platform, x1, y1, x2, y2)
        self.update()

    def delete_brick(self, brick):
        self.delete(self.bricks[brick])

    def update_ball(self, ball):
        x1, y1 = ball.x - ball.r, ball.y - ball.r
        x2, y2 = ball.x + ball.r, ball.y + ball.r
        self.coords(self.ball, x1, y1, x2, y2)
        self.update()

    def delete_ball(self):
        self.delete(self.ball)

    def delete_platform(self):
        self.delete(self.platform)


class GameMenuView(tk.Frame):
    def __init__(self, master):
        super().__init__(master)
        self.master = master
        self.pack()

        self.button_start = tk.Button(self, text='START')
        self.button_start.pack(side='left')

        self.button_pause = tk.Button(self, text='PAUSE')
        self.button_pause.pack(side='right')
