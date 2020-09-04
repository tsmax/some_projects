import tkinter as tk

""" NO CHANGE """

WINDOW_HEIGHT = 600
WINDOW_WIDTH = 400

BRICKS_FIELD_WIDTH, BRICKS_FIELD_HEIGHT = WINDOW_WIDTH, 100
BRICKS_FIELD_ANCHORPOINT_X, BRICKS_FIELD_ANCHORPOINT_Y = 0, 50
""" Bricks field if rectangle with coords (0;50) --> (400;150) """

PLATFORM_LINE_ANCHORPOINT_X, PLATFORM_LINE_ANCHORPOINT_Y = 0, 440
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

    def clean(self):
        self.delete('ALL')

    def draw_platform(self, platform):
        x1, y1 = platform.x, platform.y
        x2, y2 = x1 + platform.width, y1 + platform.height
        self.create_rectangle(x1, y1, x2, y2, fill=platform.color)

    def draw_bricks(self, bricks):
        for brick in bricks:
            x1, y1 = brick.x, brick.y
            x2, y2 = x1 + brick.width, y1 + brick.height
            self.create_rectangle(x1, y1, x2, y2, fill=brick.color)





class GameMenuView(tk.Frame):
    def __init__(self, master):
        super().__init__(master)
        self.master = master
        self.pack()

        self.button_start = tk.Button(self, text='START')
        self.button_start.pack(side='left')

        self.button_stop = tk.Button(self, text='STOP')
        self.button_stop.pack(side='right')
