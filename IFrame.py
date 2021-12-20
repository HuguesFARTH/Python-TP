import tkinter as tk
import Player
import Monster
import Block


class GameMenu:
    def __init__(self, app):
        self.app = app
        self.gameFrame = GameFrame(self.app)
        self.gameFrame.unBind()
        self.init()

    def init(self):
        self.frame = tk.Frame(self.app.tk, bg='gray')
        self.frame.grid()

        self.quitButton = tk.Button(self.frame, text="Quitter", command=self.app.main.stop)
        self.quitButton.grid()

        self.playButton = tk.Button(self.frame, text="jouer", command=self.play)
        self.playButton.grid()

    def update(self):
        print("Update Frame")

    def draw(self):
        print("draw")
        # self.canvas.delete("all")
        # for ent in self.entities:
        #     ent.draw()

    def unBind(self):
        self.frame.grid_forget()

    def play(self):
        self.frame.grid_forget()
        self.app.gameFrame.frame.grid()
        self.app.menu = "play"
        self.app.update()
        self.app.draw()
        self.unBind()
        self.app.gameFrame.Bind()

    def settings(self):
        pass

class GameFrame:
    def __init__(self, app):
        self.app = app
        self.init()

    def init(self):
        # GAME
        self.entities = []
        self.score = 0

        # TKINTER
        self.frame = tk.Frame(self.app.tk, bg='gray')
        self.frame.grid()
        self.leftFrame = tk.Frame(self.frame)
        self.leftFrame.grid(row=0, column=0)
        self.topFrame = tk.Frame(self.leftFrame)
        self.topFrame.grid()

        self.canvas = tk.Canvas(self.leftFrame, bg='black', width=900, height=550)
        self.canvas.grid(row=1)

        self.rightFrame = tk.Frame(self.frame, bg='white')
        self.rightFrame.grid(row=0, column=1)
        self.rejouerButton = tk.Button(self.rightFrame, text="New game", command=self.newgame)
        self.rejouerButton.grid(row=0)
        self.quitButton = tk.Button(self.rightFrame, text="Quitter", command=self.app.main.stop)
        self.quitButton.grid(row=1)

        self.player = Player.Player(self.app, self.canvas)
        self.entities.append(self.player)
        stone = Block.Block(self.app, self.canvas, [500, 200])
        stone2 = Block.Block(self.app, self.canvas, [100, 200])
        self.entities.append(stone)
        self.entities.append(stone2)
        for i in range(0, 17):
            monster1 = Monster.Monster(self.app, self.canvas, [50 + i * 50, 100])
            self.entities.append(monster1)
        self.app.tk.bind('<'+self.app.config['shoot']+'>', self.player.shoot)

        self.scoreLabel = tk.Label(self.topFrame, text="Score: " + str(self.score))
        self.scoreLabel.grid(row=0, column=0)
        self.invi1 = tk.Label(self.topFrame, text="")
        self.invi1.grid(row=0, column=2, padx=100)
        self.lifeLabel = tk.Label(self.topFrame, text="Lives: " + str(self.player.lives))
        self.lifeLabel.grid(row=0, column=3)

    def newgame(self):
        self.unBind()
        self.init()

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
        self.frame.grid_forget()
        self.app.tk.unbind('<'+self.app.config['shoot']+'>')

    def Bind(self):
        self.frame.grid()
        self.app.tk.bind('<' + self.app.config['shoot'] + '>', self.player.shoot)

