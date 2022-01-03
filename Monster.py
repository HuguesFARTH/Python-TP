import Projectile
import random

from PIL import Image, ImageTk
import Block
import Player
import math

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
        self.proba_tir = 1000/60
        self.collideCount = 0
        self.collideCountFake = False

    def draw(self):
        self.canvas.create_image(self.pos[0], self.pos[1], image = self.save_img, anchor = "center")

    def remove(self):
        self.app.gameFrame.entities.remove(self)
        self.app.gameFrame.score += 100
        self.app.gameFrame.scoreLabel.configure(text ="Score: " + str(self.app.gameFrame.score))

    def hit(self):
        self.remove()

    def update(self):
        if self.collideCount % 2 == 0:
            self.pos[0] = self.pos[0] + self.speed
            if self.pos[0] > int(self.canvas.cget('width')):
                self.pos[0] = int(self.canvas.cget('width'))
                self.collideCount = self.collideCount+1
                self.collideCountFake = False
        else:
            self.pos[0] = self.pos[0] - self.speed
            if self.pos[0] < 0:
                self.pos[0] = 0
                self.collideCount = self.collideCount+1
                if not self.collideCountFake:
                    self.pos[1] = self.pos[1] + self.size
                    self.collideCountFake = 0
        if random.randint(0,1000) <= self.proba_tir:
            self.shoot()

        self.collide()

    def collide(self):
        for ent in self.app.gameFrame.entities:
            if self == ent:
                continue
            if isinstance(ent, Projectile.Projectile):
                continue
            elif math.pow(self.pos[0]-ent.pos[0],2) + math.pow(self.pos[1]-ent.pos[1],2)< math.pow(self.size + ent.size/2,2):
                if isinstance(ent, Player.Player):
                    ent.hit()
                elif isinstance(ent,Block.Block):
                    self.collideCountFake = True
                    self.collideCount += 1
                    ent.hit()
                print("collide: " , ent)
                return

    def shoot(self):
        shoot = Projectile.Projectile(self.app, self.canvas, [0,1], [self.pos[0], self.pos[1]-self.size/2],False)
        self.app.gameFrame.entities.append(shoot)
