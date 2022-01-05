import Projectile
import random
import math
from PIL import Image, ImageTk
import Block
import Player
import math
import Heart

class Monster:

    # heartDropRate (0-100)
    def __init__(self,app,canvas,pos, life = None, shooter = False, boss = False, heartDropRate = 10):
        self.size = 30
        self.shooter = shooter
        self.boss = boss
        self.app = app
        self.canvas = canvas
        self.speed = 15
        self.pos = pos
        self.proba_tir = 1000/self.app.main.TICK_CAP
        self.collideCount = 0
        self.collideCountFake = False
        self.life = life if life != None else 1 if not boss else 5
        self.heartDropRate = heartDropRate if not boss else heartDropRate*7.5
        self.maxLife = self.life
        self.damageP = self.app.assetsSize["monster_damages"]/self.maxLife #coef permettant de déterminer la texture des dégats
        # self.downTimer = 100

    def draw(self):
        texture = 1 if self.shooter else 0
        texture += 2 if self.boss else 0
        self.canvas.create_image(self.pos[0], self.pos[1], image = self.app.assets['monster'][texture], anchor = "center")
        if self.app.damageDrawText:
            self.canvas.create_text(self.pos[0], self.pos[1], fill = "blue" ,font="bold 15", text=self.life, anchor="center")
        else:
            if self.life < self.maxLife:
                self.canvas.create_image(self.pos[0], self.pos[1], image=self.app.assets['monster_damages'][self.getDamage()], anchor="center")


    def getDamage(self):
        return int(self.damageP*self.life)

    def remove(self):
        if self in self.app.gameFrame.entities:
            self.app.gameFrame.entities.remove(self)
            self.app.gameFrame.score += self.getScore()
            self.app.gameFrame.scoreLabel.configure(text ="Score: " + str(self.app.gameFrame.score))

    def getScore(self):
        score = 100
        if self.shooter:
            score *= 2
        if self.boss:
            score *= 2
        return score

    def kill(self):
        self.remove()
        if random.randint(0,100) <= self.heartDropRate:
            heart = Heart.Heart(self.app, self.canvas, [0,1], [self.pos[0]+self.size/2, self.pos[1]-self.size/2],textureId = 0)
            heart.app.gameFrame.entities.append(heart)

    def hit(self):
        self.life -= 1
        if self.life <= 0:
            self.kill()

    def heal(self):
        self.life += 1

    def update(self):
        lastMove = [self.pos[0],self.pos[1]]
        if self.collideCount % 2 == 0:
            self.pos[0] = self.pos[0] + self.speed * self.app.gameFrame.numberSpeedCount
            if self.pos[0] > int(self.canvas.cget('width')):
                self.pos[0] = int(self.canvas.cget('width'))
                self.collideCount = self.collideCount+1
                self.collideCountFake = False
        else:
            self.pos[0] = self.pos[0] - self.speed * self.app.gameFrame.numberSpeedCount
            if self.pos[0] < 0:
                self.pos[0] = 0
                self.collideCount = self.collideCount+1
                if not self.collideCountFake:
                    self.pos[1] = self.pos[1] + self.size*2
                    self.collideCountFake = 0

        if self.shooter:
            if random.randint(0,1000) <= self.proba_tir:
                self.shoot()

        if self.collide():
            lastMove = [lastMove[0] - self.pos[0],lastMove[1] - self.pos[1]]
            self.pos[0] = self.pos[0] + lastMove[0]
            self.pos[1] = self.pos[1] + lastMove[1]

    def collide(self):
        for ent in self.app.gameFrame.entities:
            if self == ent:
                continue
            if isinstance(ent, Projectile.Projectile):
                continue
            if isinstance(ent, Heart.Heart):
                continue
            elif math.pow(self.pos[0]-ent.pos[0],2) + math.pow(self.pos[1]-ent.pos[1],2) < math.pow(self.size + ent.size/2,2):
                if isinstance(ent, Player.Player):
                    ent.hit()
                elif isinstance(ent,Block.Block):
                    self.collideCountFake = True
                    self.collideCount += 1
                    ent.hit()
                elif isinstance(ent,Monster):
                    if self.app.alienCollision:
                        self.collideCountFake = False
                        self.collideCount += 1
                    else:
                        return False
                return True
        return False

    def shoot(self):
        dir = [0,1]
        if self.boss:
            dir = [self.app.gameFrame.player.pos[0] - self.pos[0] if self.pos[0] != 0 else 1,self.app.gameFrame.player.pos[1] - self.pos[1] if self.pos[1] != 0 else 1]
            n = math.sqrt(dir[0]**2 + dir[1]**2)
            dir = [dir[0]/n,dir[1]/n]
            # print(dir)
        shoot = Projectile.Projectile(self.app, self.canvas, dir, [self.pos[0], self.pos[1]-self.size/2],False)
        self.app.gameFrame.entities.append(shoot)
