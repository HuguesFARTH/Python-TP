import tkinter as tk
from PIL import Image, ImageTk


class Block():
    def __init__(self, app, canvas, pos, life = 4):
        self.size = 30
        self.app = app
        self.canvas = canvas
        self.pos = pos
        self.life = life
        self.maxLife = self.life
        self.damageP = int(self.app.assetsSize["block_damages"])/self.maxLife #coef permettant de déterminer la texture des dégats
        pass

    def draw(self):
        self.canvas.create_image(self.pos[0], self.pos[1], image=self.app.assets['block'][0], anchor="center")
        if self.app.config['overlay'] == 1:
            self.canvas.create_text(self.pos[0], self.pos[1], fill = "blue" ,font="bold 10", text=self.life, anchor="center")
        else:
            if self.life < self.maxLife:
                self.canvas.create_image(self.pos[0], self.pos[1], image=self.app.assets['block_damages'][self.getDamage()], anchor="center")

    def getDamage(self):
        return int(self.damageP*self.life)

    def remove(self):
        self.app.gameFrame.entities.remove(self)

    def hit(self):
        self.life -= 1
        if self.life <= 0:
            self.remove()

    def update(self):
        pass
