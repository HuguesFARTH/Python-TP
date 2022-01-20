import tkinter as tk
import math
import Monster
import Player
import Projectile
import Block

class Heart:
    def __init__(self, app, canvas, dir: list, pos: list, textureId = 0):
        self.app = app
        self.canvas = canvas
        self.dir = dir
        self.pos = pos
        self.size = 10
        self.speed = 10 * self.app.config['bulletSpeed']
        self.textureId = textureId

    def draw(self):
        self.canvas.create_image(self.pos[0], self.pos[1], image = self.app.assets['heart'][self.textureId], anchor = "center")

    def update(self):
        lastMove = [self.pos[0],self.pos[1]]
        self.pos[0] += self.dir[0] * self.speed
        self.pos[1] += self.dir[1] * self.speed
        if self.pos[0] < 0:
            self.remove()
        if self.pos[0] > int(self.canvas.cget('width')):
            self.remove()
        if self.pos[1] < 0:
            self.remove()
        if self.pos[1] > int(self.canvas.cget('height')):
            self.remove()

        if(self.collide()):
            lastMove = [lastMove[0] - self.pos[0],lastMove[1] - self.pos[1]]
            self.pos[0] = self.pos[0] + lastMove[0]
            self.pos[1] = self.pos[1] + lastMove[1]

    def remove(self):
        if self in self.app.gameFrame.entities:
            self.app.gameFrame.entities.remove(self)

    def hit(self):
        self.remove()

    def collide(self):
        for ent in self.app.gameFrame.entities:
            if not isinstance(ent,Block.Block) and not isinstance(ent,Player.Player):
                return False
            elif math.pow(self.pos[0]-ent.pos[0],2) + math.pow(self.pos[1]-ent.pos[1],2) < math.pow(self.size + ent.size/4,2):
                if isinstance(ent,Block.Block):
                    return True
                elif isinstance(ent,Player.Player):
                    self.remove()
                    ent.heal()
                    return False

# root = tk.Tk()
# root.geometry("600x600")
# parent = tk.Canvas(root, width=500, height=500, bg= 'blue')
#
# parent.pack()
# proj = Projectile(2,parent,[1.01,1.03], [200,220])
#
# btn = tk.Button(root, text='bonjour', command= lambda: proj.update())
# btn.pack()
#
#
# root.mainloop()
