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
        image = Image.open("assets/stone.png")
        image = image.resize((self.size, self.size))
        self.save_img = ImageTk.PhotoImage(image)
        self.imageHit = []
        for i in range(2,self.life+1):
            imageB = Image.open("assets/hit_"+str(self.life - i)+".png")
            imageB = imageB.resize((self.size, self.size))
            self.imageHit.append(ImageTk.PhotoImage(imageB))
        pass

    def draw(self):
        self.canvas.create_image(self.pos[0], self.pos[1], image=self.save_img, anchor="center")
        if self.life < 4:
            self.canvas.create_image(self.pos[0], self.pos[1], image=self.imageHit[self.life-1], anchor="center")

    def remove(self):
        self.app.gameFrame.entities.remove(self)

    def hit(self):
        self.life -= 1
        if self.life <= 0:
            self.remove()

    def update(self):
        pass
