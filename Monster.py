import tkinter as tk
from PIL import Image,ImageTk
import random
import Projectile

class Monster:
    def __init__(self,app,canvas,pos):
        self.size = 30
        self.app = app
        self.canvas = canvas
        self.speed = 10
        self.pos = pos
        image = Image.open("assets/monster_yellow.png")
        image = image.resize((self.size, self.size))
        self.save_img =ImageTk.PhotoImage(image)
        self.proba_tir = 1000/120

    def draw(self):
        self.canvas.create_image(self.pos[0], self.pos[1], image = self.save_img, anchor = "center")

    def remove(self):
        self.app.gameFrame.entities.remove(self)
        self.app.gameFrame.score += 100
        self.app.gameFrame.scoreLabel.configure(text = "Lives: " + str(self.app.gameFrame.score))

    def hit(self):
        self.remove()

    def update(self):
        if random.randint(0,1000) <= self.proba_tir:
            self.shoot()

    def shoot(self):
        shoot = Projectile.Projectile(self.app, self.canvas, [0,1], [self.pos[0], self.pos[1]-self.size/2],False)
        self.app.gameFrame.entities.append(shoot)
