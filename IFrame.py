import tkinter as tk
import Player
import Monster
import Block
import keyboard

class GameMenu:
    def __init__(self, app):
        self.app = app  # on importe la classe app
        self.frame = None  # création de la variable de la frame menu
        self.quitButton = None  # création des variables des boutons
        self.playButton = None
        self.settingsButton = None

        self.init()

    def init(self):
        self.frame = tk.Frame(self.app.tk, width=self.app.main.xSize, height=self.app.main.xSize)
        self.frame.grid(ipadx=0, ipady=30, padx=390, pady=200)

        self.frame.columnconfigure(0, weight=1)
        self.frame.columnconfigure(1, weight=3)
        self.frame.columnconfigure(2, weight=1)

        self.frame.rowconfigure(0, weight=2)
        self.frame.rowconfigure(1, weight=1)
        self.frame.rowconfigure(2, weight=2)
        self.frame.rowconfigure(3, weight=1)
        self.frame.rowconfigure(4, weight=2)

        self.playButton = tk.Button(self.frame, text="Jouer", width="20", height="2", command=self.play)
        self.playButton.grid(row=0, column=1)

        self.quitButton = tk.Button(self.frame, text="Quitter", width="20", height="2", command=self.app.main.stop)
        self.quitButton.grid(row=2, column=1)

        self.settingsButton = tk.Button(self.frame, text="Paramètres", width="20", height="2", command=self.settings)
        self.settingsButton.grid(row=4, column=1)

    def unBind(self):
        self.frame.grid_forget()

    def play(self):
        self.frame.grid_forget()
        self.app.gameFrame.frame.grid()
        self.app.menu = "play"
        self.app.update()
        self.app.draw()
        self.unBind()
        self.app.gameFrame.new_game()

    def settings(self):
        self.frame.grid_forget()
        self.app.settings.init()
        self.app.menu = "settings"
        self.app.update()
        self.unBind()


class GameFrame:
    def __init__(self, app):
        self.app = app

        self.entities = None
        self.score = None
        self.frame = None
        self.leftFrame = None
        self.topFrame = None
        self.canvas = None
        self.rightFrame = None

        self.init()

    def pauseFct(self, event):
        self.pause = not self.pause

    def gameOverFct(self):
        print("game over")
        self.gameOver = True

    def init(self):
        # GAME
        self.entities = []
        self.score = 0

        self.pause = False
        self.gameOver = False

        # TKINTER
        self.frame = tk.Frame(self.app.tk, bg='gray')
        self.frame.grid()

        self.leftFrame = tk.Frame(self.frame)
        self.leftFrame.grid(row=0, column=0)

        self.topFrame = tk.Frame(self.leftFrame)
        self.topFrame.grid()

        self.canvas = tk.Canvas(self.leftFrame, bg='black', width=900, height=550)
        self.canvas.grid(row=1)

        self.rightFrame = tk.Frame(self.frame)
        self.rightFrame.grid(row=0, column=1)

        self.quitButton = tk.Button(self.rightFrame, text="Menu", command=self.retour_menu)
        self.quitButton.grid(row=1)

        self.rejouerButton = tk.Button(self.rightFrame, text="New game", command=self.new_game)
        self.rejouerButton.grid(row=0)

        self.player = Player.Player(self.app, self.canvas)
        self.entities.append(self.player)

        for i in range(0,20):
            stone = Block.Block(self.app, self.canvas, [30*i, 200])
            self.entities.append(stone)

        for i in range(0, 1):
            monster1 = Monster.Monster(self.app, self.canvas, [50 + i * 50, 100])
            self.entities.append(monster1)
        self.app.tk.bind('<' + self.app.config['shoot'] + '>', self.player.shoot)
        self.scoreLabel = tk.Label(self.topFrame, text="Score: " + str(self.score))
        self.scoreLabel.grid(row=0, column=0)

        self.invi1 = tk.Label(self.topFrame, text="")
        self.invi1.grid(row=0, column=2, padx=100)

        self.lifeLabel = tk.Label(self.topFrame, text="Lives: " + str(self.player.lives))
        self.lifeLabel.grid(row=0, column=3)

    def new_game(self):
        self.unBind()
        self.init()

    def update(self):
        # print("Update Frame")
        # self.i += 1
        if self.pause or self.gameOver:
            return
        for ent in self.entities:
            ent.update()

    def draw(self):
        self.canvas.delete("all")
        for ent in self.entities:
            ent.draw()
        if self.gameOver:
            self.drawGameOver()
        elif self.pause:
            self.drawPause()

    def drawGameOver(self):
        xp = (int(self.canvas.cget('width')) / 2)
        yp = (int(self.canvas.cget('height')) / 2)
        self.canvas.create_rectangle(0,0,int(self.canvas.cget('width'))+10,int(self.canvas.cget('height'))+10, fill="gray", stipple="gray50")
        self.canvas.create_text(xp,yp, font="bold 40",text = "Game Over" , anchor = "center")
        # self.canvas.create_rectangle(xp-13,yp+25,xp-3,yp-50, fill="blue")
        # self.canvas.create_rectangle(xp+3,yp+25,xp+13,yp-50, fill="blue")

    def drawPause(self):
        xp = (int(self.canvas.cget('width')) / 2)
        yp = (int(self.canvas.cget('height')) / 2)
        self.canvas.create_rectangle(0,0,int(self.canvas.cget('width'))+10,int(self.canvas.cget('height'))+10, fill="gray", stipple="gray50")
        self.canvas.create_rectangle(xp-13,yp+25,xp-3,yp-50, fill="blue")
        self.canvas.create_rectangle(xp+3,yp+25,xp+13,yp-50, fill="blue")

    def unBind(self):
        self.frame.grid_forget()
        self.app.tk.unbind('<' + self.app.config['shoot'] + '>')
        self.app.tk.unbind('<' + self.app.config['pause'] + '>')

    def Bind(self):
        self.frame.grid()
        self.app.tk.bind('<' + self.app.config['shoot'] + '>', self.player.shoot)
        self.app.tk.bind('<' + self.app.config['pause'] + '>', self.pauseFct)

    def retour_menu(self):
        self.frame.grid_forget()
        self.app.menu = "menu"
        self.app.menuFrame.init()

class SettingsFrame:
    def __init__(self, app):
        self.app = app

        self.frame = None
        self.back = None
        self.pref = None

        self.init()

    def init(self):
        self.frame = tk.Frame(self.app.tk, bg='gray')
        self.frame.grid(ipady=250, ipadx=100, padx=100)

        self.frame.columnconfigure(0, weight=1)
        self.frame.columnconfigure(1, weight=1)
        self.frame.columnconfigure(2, weight=1)
        self.frame.columnconfigure(3, weight=1)
        self.frame.columnconfigure(4, weight=1)

        self.pref = tk.Label(self.frame, text="Préférences clavier", font=("Arial", 25))
        self.pref.grid(columnspan=3, column=1)

        self.vide1 = tk.Label(self.frame, text="         ", font=("Arial", 25))
        self.vide1.grid(columnspan=1, column=0)

        self.vide2 = tk.Label(self.frame, text="         ", font=("Arial", 25))
        self.vide2.grid(columnspan=1, column=4)

        self.afficher_settings()
        self.back = tk.Button(self.frame, text="Retour", command=self.retour_menu, width=15, font=("Arial", 20))
        self.back.grid()

    def retour_menu(self):
        self.frame.grid_forget()
        self.app.menu = "menu"
        self.app.menuFrame.init()

    def afficher_settings(self):
        self.set = tk.Label(self.frame, text="à gauche", font=("Arial", 25))
        self.set.grid()
        pass
