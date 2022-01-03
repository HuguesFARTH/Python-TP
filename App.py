import tkinter as tk
from PIL import Image, ImageTk
import ILib
import random
import IFrame
import config


class App:
    def __init__(self, main):
        print("init App")
        self.main = main

        self.tk = tk.Tk()
        self.tk.geometry(str(main.xSize) + "x" + str(main.ySize))
        self.tk.minsize(main.xSize, main.ySize)
        self.tk.maxsize(main.xSize, main.ySize)

        self.config = config.Config('config.ini').read_config()
        self.config["pause"] = "p"
        self.menu = "menu"

        self.gameFrame = IFrame.GameFrame(self)
        self.gameFrame.unBind()

        self.settings = IFrame.SettingsFrame(self)
        self.settings.frame.grid_forget()

        self.menuFrame = IFrame.GameMenu(self)

    def update(self):
        if self.menu == "play":
            self.gameFrame.update()
            self.tk.update_idletasks()
            self.tk.update()

        elif self.menu == "menu":
            self.tk.update_idletasks()
            self.tk.update()

        elif self.menu == "settings":
            self.tk.update_idletasks()
            self.tk.update()

    def draw(self):
        self.gameFrame.draw()
