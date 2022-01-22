import configparser
import tkinter as tk
from PIL import Image, ImageTk
import keyboard
import Projectile
import config
import Level

class Player:
    """

    """
    def __init__(self, app, canvas, level = Level.Level()):
        self.app = app
        self.size = 45
        self.life = level.playerLife
        self.canvas = canvas
        self.speed = 20 * self.app.config['playerSpeed']
        self.pos = [0,0]
        self.lastShoot = 0
        self.shootRate = 1000 #TODO
        self.pos = [int(self.canvas.cget('width')) / 2, int(self.canvas.cget('height'))]
        self.maxBullet = 10
        self.bullet = self.maxBullet
        self.bulletTick = 0
        self.rightMove = False
        self.leftMove = False
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
        self.bulletTick += 1
        if self.bulletTick > self.app.main.TICK_CAP*0.5:
            self.bulletTick = 0
            self.bullet = self.bullet + 1 if self.bullet < self.maxBullet else self.maxBullet
        if self.leftMove:
            self.left()
        if self.rightMove:
            self.right()
        pass

    def left(self):
        """

        :return:
        """
        self.pos[0] -= self.speed
        if self.pos[0] < 0:
            self.pos[0] = 0

    def right(self):
        """

        :return:
        """
        self.pos[0] += self.speed
        if self.pos[0] > int(self.canvas.cget('width')):
            self.pos[0] = int(self.canvas.cget('width'))

    def shoot(self, event):
        """

        :param event:
        :return:
        """
        if self.bullet > 0:
            # print(self.bullet)
            self.bullet -= 1
            shoot = Projectile.Projectile(self.app, self.canvas, [0, -1], [self.pos[0], self.pos[1] - self.size / 2], True)
            self.app.gameFrame.entities.append(shoot)

    def remove(self):
        """

        :return:
        """
        if self in self.app.gameFrame.entities:
            self.app.gameFrame.entities.remove(self)

    def kill(self):
        """

        :return:
        """
        self.life = 0
        self.app.gameFrame.lifeLabel.configure(text="Vies: " + str(self.life))
        self.remove()
        self.app.gameFrame.gameOverFct()

    def heal(self):
        """

        :return:
        """
        self.life += 1
        self.app.gameFrame.lifeLabel.configure(text="Vies: " + str(self.life))

    def hit(self):
        """

        :return:
        """
        self.life -= 1
        if self.life <= 0:
            self.kill()
        else:
            self.app.gameFrame.lifeLabel.configure(text="Vies: " + str(self.life))
