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

        # LOADING ASSETS
        self.assets = {}
        self.initAssets()

        self.config = config.Config('config.ini').read_config()
        self.menu = "menu"

        self.gameFrame = IFrame.GameFrame(self)
        self.gameFrame.unBind()

        self.settings = IFrame.SettingsFrame(self)
        self.settings.frame.grid_forget()

        self.menuFrame = IFrame.GameMenu(self)


    def initAssets(self):
        # PLAYER
        self.assets['player'] = []
        image = Image.open("assets/player.png")
        image = image.resize((100, 100))
        self.assets['player'].append(ImageTk.PhotoImage(image))

        # MONSTER
        self.assets['monster'] = []
        image = Image.open("assets/monster_yellow.png")
        image = image.resize((30, 30))
        self.assets['monster'].append(ImageTk.PhotoImage(image))

        # BLOCKS
        self.assets['block'] = []
        image = Image.open("assets/stone.png")
        image = image.resize((30, 30))
        self.assets['block'].append(ImageTk.PhotoImage(image))

        # BLOCKS DAMAGES
        self.assets['block_damages'] = []
        for i in range(2,5):
            image = Image.open("assets/hit_"+str(4 - i)+".png")
            image = image.resize((30, 30))
            self.assets['block_damages'].append(ImageTk.PhotoImage(image))


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
