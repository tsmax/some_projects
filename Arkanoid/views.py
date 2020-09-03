import tkinter as tk


WINDOW_HEIGHT = 600
WINDOW_WIDTH = 400


class MainApp(tk.Tk):
    def __init__(self):
        super().__init__()

    def start_game(self):
        battlefield = BattleField(self)
        gamemenu = GameMenu(self)


class BattleField(tk.Canvas):
    def __init__(self, master):
        super().__init__(master, height=WINDOW_HEIGHT-300, width=WINDOW_WIDTH)
        self.master = master
        self.pack()


class GameMenu(tk.Frame):
    def __init__(self, master):
        super().__init__(master)
        self.master = master
        self.pack()

        self.button_start = tk.Button(self, text='START')
        self.button_start.pack(side='left')

        self.button_stop = tk.Button(self, text='STOP')
        self.button_stop.pack(side='right')


game = MainApp()
game.start_game()
game.mainloop()

