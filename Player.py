import configparser
import tkinter as tk
from PIL import Image, ImageTk
import keyboard
import Projectile
import config


class Player:
    def __init__(self, app, canvas):
        self.size = 100
        self.lives = 3
        self.app = app
        self.canvas = canvas
        self.speed = 10
        self.pos = [0,0]
        self.pos = [int(self.canvas.cget('width')) / 2, int(self.canvas.cget('height'))]
        image = Image.open("assets/player.png")
        image = image.resize((self.size, self.size))
        self.save_img = ImageTk.PhotoImage(image)
        self.config = config.Config('config.ini').read_config()
        pass

    def draw(self):
        """
        create the player
        :return:
        """
        self.canvas.create_image(self.pos[0], self.pos[1] - self.size / 2, image=self.save_img, anchor="center")

    def update(self):
        """
        verify if a key is pressed and update the position of the player
        :return:
        """
        if keyboard.is_pressed(self.config['up']):
            self.up()
        if keyboard.is_pressed(self.config['down']):
            self.down()
        if keyboard.is_pressed(self.config['left']):
            self.left()
        if keyboard.is_pressed(self.config['right']):
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

    def up(self):
        self.pos[1] -= self.speed
        if self.pos[1] < self.size / 2:
            self.pos[1] = self.size / 2

    def down(self):
        self.pos[1] += self.speed
        if self.pos[1] > int(self.canvas.cget('height')):
            self.pos[1] = int(self.canvas.cget('height'))

    def shoot(self, event):
        shoot = Projectile.Projectile(self.app, self.canvas, [0, -1], [self.pos[0], self.pos[1] - self.size / 2], True)
        self.app.gameFrame.entities.append(shoot)

    def remove(self):
        print("die")

    def hit(self):
        print("hit")
        self.lives -= 1
        self.app.gameFrame.lifeLabel.configure(text="Lives: " + str(self.lives))


# if __name__ == "__main__":
#     app = 2
#     canvas = 2
#     player = Player(app, canvas)
#     print(player.config['up'])
