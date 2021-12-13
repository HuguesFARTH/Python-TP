import tkinter as tk
from PIL import Image,ImageTk

class Block():
    def __init__(self,app,canvas,pos):
        self.size = 30
        self.app = app
        self.canvas = canvas
        self.speed = 10
        self.pos = pos
        image = Image.open("assets/stone.png")
        image = image.resize((self.size, self.size))
        self.save_img =ImageTk.PhotoImage(image)
        pass

    def draw(self):
        self.canvas.create_image(self.pos[0], self.pos[1], image = self.save_img, anchor = "center")

    def remove(self):
        self.app.gameFrame.entities.remove(self)

    def hit(self):
        pass

    def update(self):
        pass
