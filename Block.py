import tkinter as tk
from PIL import Image, ImageTk


class Block():
    def __init__(self, app, canvas, pos):
        self.size = 30
        self.app = app
        self.canvas = canvas
        self.speed = 10
        self.pos = pos
        self.life = 4

        pass

    def draw(self):
        self.canvas.create_image(self.pos[0], self.pos[1], image=self.app.assets['block'][0], anchor="center")
        if self.life < 4:
            self.canvas.create_image(self.pos[0], self.pos[1], image=self.app.assets['block_damages'][self.life-1], anchor="center")

    def remove(self):
        self.app.gameFrame.entities.remove(self)

    def hit(self):
        self.life -= 1
        if self.life <= 0:
            self.remove()

    def update(self):
        pass
