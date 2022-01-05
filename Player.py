import configparser
import tkinter as tk
from PIL import Image, ImageTk
import keyboard
import Projectile
import config


class Player:
    def __init__(self, app, canvas):
        self.size = 90
        self.life = 3
        self.app = app
        self.canvas = canvas
        self.speed = 20
        self.pos = [0,0]
        self.lastShoot = 0
        self.shootRate = 1000 #TODO
        self.pos = [int(self.canvas.cget('width')) / 2, int(self.canvas.cget('height'))]
        # self.config = config.Config('config.ini').read_config()
        pass

    def draw(self):
        """
        draw the player
        :return:
        """
        self.canvas.create_image(self.pos[0], self.pos[1] - self.size / 2, image=self.app.assets['player'][0], anchor="center")

    def update(self):
        """
        verify if a key is pressed and update the position of the player
        :return:
        """
        # if keyboard.is_pressed(self.app.config['up']):
        #     self.up()
        # if keyboard.is_pressed(self.app.config['down']):
        #     self.down()
        if keyboard.is_pressed(self.app.config['left']):
            self.left()
        if keyboard.is_pressed(self.app.config['right']):
            self.right()
        pass

    def left(self):
        self.pos[0] -= self.speed
        if self.pos[0] < 0:
            self.pos[0] = 0

    def right(self):
        self.pos[0] += self.speed
        if self.pos[0] > int(self.canvas.cget('width')):
            self.pos[0] = int(self.canvas.cget('width'))

    # def up(self):
    #     self.pos[1] -= self.speed
    #     if self.pos[1] < self.size / 2:
    #         self.pos[1] = self.size / 2
    #
    # def down(self):
    #     self.pos[1] += self.speed
    #     if self.pos[1] > int(self.canvas.cget('height')):
    #         self.pos[1] = int(self.canvas.cget('height'))

    def shoot(self, event):
        shoot = Projectile.Projectile(self.app, self.canvas, [0, -1], [self.pos[0], self.pos[1] - self.size / 2], True)
        self.app.gameFrame.entities.append(shoot)

    def remove(self):
        if self in self.app.gameFrame.entities:
            self.app.gameFrame.entities.remove(self)

    def kill(self):
        self.life = 0
        self.app.gameFrame.lifeLabel.configure(text="Vies: " + str(self.life))
        self.remove()
        self.app.gameFrame.gameOverFct()

    def heal(self):
        self.life += 1
        self.app.gameFrame.lifeLabel.configure(text="Vies: " + str(self.life))

    def hit(self):
        self.life -= 1
        if self.life <= 0:
            self.kill()
        else:
            self.app.gameFrame.lifeLabel.configure(text="Vies: " + str(self.life))
