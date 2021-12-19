import tkinter as tk
from PIL import Image,ImageTk
import ILib
import random
import IFrame


class App():
    def __init__(self, main):
        print("init App")
        self.main = main
        self.tk = tk.Tk()
        self.tk.geometry(str(main.xSize)+"x"+str(main.ySize))
        self.tk.minsize(main.xSize, main.ySize)
        self.tk.maxsize(main.xSize, main.ySize)
        self.menu = "menu"
        self.gameFrame = IFrame.GameFrame(self)
        self.gameFrame.unBind()
        self.menuFrame = IFrame.GameMenu(self)
        self.tk.mainloop()

    def update(self):
        if self.menu == "play":
            self.gameFrame.update()
            self.tk.update_idletasks()
            self.tk.update()

    # def menu(self):
    #

    # def play(self):
        # self.gameFrame.init()

    def draw(self):
        self.gameFrame.draw()
