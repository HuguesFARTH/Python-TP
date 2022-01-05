import tkinter as tk
import math
import Monster
import Player

class Projectile:
    def __init__(self, app, canvas, dir: list, pos: list, isplayer):
        self.app = app
        self.canvas = canvas
        self.dir = dir
        self.pos = pos
        self.rayon = 5
        self.isplayer = isplayer
        self.speed = 20


    def draw(self):
        self.canvas.create_oval(self.pos[0]-self.rayon, self.pos[1]-self.rayon ,self.pos[0]+self.rayon , self.pos[1]+self.rayon, fill = "green" if self.isplayer else "red" )

    def update(self):
        self.pos[0] += self.dir[0] * self.speed
        self.pos[1] += self.dir[1] * self.speed
        self.checkCollisions()
        if self.pos[0] < 0:
            self.remove()
        if self.pos[0] > int(self.canvas.cget('width')):
            self.remove()
        if self.pos[1] < 0:
            self.remove()
        if self.pos[1] > int(self.canvas.cget('height')):
            self.remove()


    def remove(self):
        if self in self.app.gameFrame.entities:
            self.app.gameFrame.entities.remove(self)

    def checkCollisions(self):
        for ent in self.app.gameFrame.entities:
            if isinstance(ent, Projectile):
                continue
            elif not self.isplayer and isinstance(ent,Monster.Monster):
                continue
            elif self.isplayer and isinstance(ent,Player.Player):
                continue
            elif math.pow(self.pos[0]-ent.pos[0],2) + math.pow(self.pos[1]-ent.pos[1],2)< math.pow(self.rayon + ent.size/2,2):
                self.remove()
                ent.hit()
                return
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
