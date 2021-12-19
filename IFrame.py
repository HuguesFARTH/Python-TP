import tkinter as tk
import Player
import Monster
import Block


class GameMenu:
    def __init__(self,app):
        self.app = app
        self.init()

    def init(self):
        print("init")

    def update(self):
        print("Update Frame")

    def draw(self):
        print("draw")
        # self.canvas.delete("all")
        # for ent in self.entities:
        #     ent.draw()

    def unBind(self):
        self.frame.pack_forget()


class GameFrame:
    def __init__(self, app):
        self.app = app
        self.init()

    def init(self):
        # GAME
        self.entities = []
        self.score = 0

        # TKINTER
        self.frame = tk.Frame(self.app.tk, bg = 'gray')
        self.frame.pack()
        self.leftFrame = tk.Frame(self.frame)
        self.leftFrame.grid(row = 0, column = 0)
        self.topFrame = tk.Frame(self.leftFrame)
        self.topFrame.grid()


        self.canvas  = tk.Canvas(self.leftFrame, bg = 'black', width = 900, height = 550)
        self.canvas.grid(row = 1)

        self.rightFrame = tk.Frame(self.frame, bg = 'white')
        self.rightFrame.grid(row = 0, column = 1)
        self.rejouerButton = tk.Button(self.rightFrame, text = "New game", command = self.newgame)
        self.rejouerButton.grid(row = 0)
        self.quitButton = tk.Button(self.rightFrame, text = "Quitter", command = self.app.main.stop)
        self.quitButton.grid(row = 1)


        self.player = Player.Player(self.app,self.canvas)
        self.entities.append(self.player)
        stone = Block.Block(self.app, self.canvas,[500,200])
        self.entities.append(stone)
        for i in range(0,17):
            monster1 = Monster.Monster(self.app, self.canvas,[50+i*50,100])
            self.entities.append(monster1)
        self.app.tk.bind('<space>', self.player.shoot)


        self.scoreLabel = tk.Label(self.topFrame, text = "Score: " + str(self.score))
        self.scoreLabel.grid(row = 0, column = 0)
        self.invi1 = tk.Label(self.topFrame, text="")
        self.invi1.grid(row = 0, column = 2, padx = 100)
        self.lifeLabel = tk.Label(self.topFrame, text = "Lives: " + str(self.player.lives))
        self.lifeLabel.grid(row = 0, column = 3)

    def newgame(self):
        print("newgame")

    def update(self):
        # print("Update Frame")
        # self.i += 1
        for ent in self.entities:
            ent.update()

    def draw(self):
        self.canvas.delete("all")
        for ent in self.entities:
            ent.draw()

    def unBind(self):
        self.frame.pack_forget()
        self.tk.unbind("<space>")
