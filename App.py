import tkinter as tk
from PIL import Image,ImageTk
import ILib
import random
import IFrame

class App():
    def __init__(self,main):
        print("init App")
        self.main = main
        self.tk = tk.Tk()
<<<<<<< Updated upstream
        self.tk.geometry("1000x500")

if __name__ == "__main__":
    app = App()
    app.tk.title("")
    app.tk.mainloop()
=======
        self.tk.geometry(str(main.xSize)+"x"+str(main.ySize))
        self.tk.minsize(main.xSize, main.ySize)
        self.tk.maxsize(main.xSize, main.ySize)
        self.gameFrame = IFrame.GameFrame(self)

    def update(self):
        self.gameFrame.update()
        self.tk.update_idletasks()
        self.tk.update()

    def draw(self):
        self.gameFrame.draw()
>>>>>>> Stashed changes
