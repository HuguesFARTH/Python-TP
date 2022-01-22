import tkinter as tk
import Player
import Monster
import Block
import keyboard
import random
import Level


class GameMenu:
    def __init__(self, app):
        self.app = app  # on importe la classe app
        self.frame = None  # création de la variable de la frame menu
        self.quitButton = None  # création des variables des boutons
        self.playButton = None
        self.settingsButton = None

        self.init()

    def init(self):
        """

        :return:
        """
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
        """

        :return:
        """
        self.frame.grid_forget()
        self.app.gameFrame.frame.grid()
        self.app.menu = "play"
        self.app.update()
        self.app.draw()
        self.unBind()
        self.app.gameFrame.new_game()

    def settings(self):
        """

        :return:
        """
        self.frame.grid_forget()
        self.app.settings.init()
        self.app.menu = "settings"
        self.app.update()
        self.unBind()


class GameFrame:
    def __init__(self, app):
        self.app = app
        self.pause = None
        self.level = None

        self.entities = None
        self.score = None
        self.frame = None
        self.leftFrame = None
        self.topFrame = None
        self.canvas = None
        self.rightFrame = None
        self.gameOver = False
        self.init()

    def pauseFct(self, event):
        self.pause = not self.pause
        print("pause")

    def gameOverFct(self):
        print("game over")
        self.gameOver = True

    def init(self, level=Level.Level()):
        """

        :param level:
        :return:
        """

        self.level = level

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

        self.canvas = tk.Canvas(self.leftFrame, bg='black', width=self.app.main.canvasSize[0],
                                height=self.app.main.canvasSize[1])
        self.canvas.grid(row=1)

        self.rightFrame = tk.Frame(self.frame)
        self.rightFrame.grid(row=0, column=1)

        self.quitButton = tk.Button(self.rightFrame, text="Menu", command=self.retour_menu)
        self.quitButton.grid(row=1)

        self.rejouerButton = tk.Button(self.rightFrame, text="New game", command=self.new_game)
        self.rejouerButton.grid(row=0)

        # ---- SPAWN DES ENTITES -----

        # Player
        self.player = Player.Player(self.app, self.canvas)
        self.entities.append(self.player)

        # Blocks
        for info in self.level.blocksInfo:
            stone = Block.Block(self.app, self.canvas, info[0].copy(), life=info[1])
            self.entities.append(stone)

        self.app.tk.bind('<' + self.app.config['shoot'] + '>', self.player.shoot)
        self.scoreLabel = tk.Label(self.topFrame, text="Score: " + str(self.score))
        self.scoreLabel.grid(row=0, column=0)

        self.invi1 = tk.Label(self.topFrame, text="")
        self.invi1.grid(row=0, column=2, padx=100)

        self.lifeLabel = tk.Label(self.topFrame, text="Vies: " + str(self.player.life))
        self.lifeLabel.grid(row=0, column=3)

    def new_game(self):
        """

        :return:
        """
        self.unBind()
        self.init()
        self.Bind()

    def update(self):

        c = self.countMonsters()
        self.numberSpeedCount = 0 if c == 0 else 0.5 if c >= self.level.maxMonsters else 1 - (
                    0.5 * c / self.level.maxMonsters)
        if self.pause or self.gameOver:
            return
        # Update des entitées
        for ent in self.entities:
            ent.update()

        # Système de génération des monstres
        if c < self.level.maxMonsters:
            for liste in self.level.monsterSpawnPoint:
                if self.canSpawn(liste):
                    self.spawnMob(liste)
                    c += 1
                    if c >= self.level.maxMonsters:
                        return

    def getMonsters(self):
        c = []
        for entity in self.entities:
            if isinstance(entity, Monster.Monster):
                c.append(entity)
        return c

    def countMonsters(self):
        return len(self.getMonsters())


    # l correspond à une liste info de spawn des monstres dans Level
    def canSpawn(self, l):
        return random.randint(0, 1000) <= 50

    def spawnMob(self, l):
        pos = l[0].copy()
        boss = random.randint(0, 1000) <= l[1]
        shooter = random.randint(0, 1000) <= l[2]
        monster = Monster.Monster(self.app, self.canvas, pos, shooter=shooter, boss=boss)
        self.entities.append(monster)

    def draw(self):
        """
        clear le canvas puis le re-dessine en fonction de si le joueur a perdu ou met sur pause.
        :return:
        """
        self.canvas.delete("all")
        for ent in self.entities:
            ent.draw()
        if self.gameOver:
            self.drawGameOver()
        elif self.pause:
            self.drawPause()

    def drawGameOver(self):
        """
        affiche l'animation de game over.
        :return:
        """
        xp = (int(self.canvas.cget('width')) / 2)
        yp = (int(self.canvas.cget('height')) / 2)
        self.canvas.create_rectangle(0, 0, int(self.canvas.cget('width')) + 10, int(self.canvas.cget('height')) + 10,
                                     fill="gray", stipple="gray50")
        self.canvas.create_text(xp, yp, font="bold 40", text="Game Over", anchor="center")

    def drawPause(self):
        """
        affiche l'annimation de la pause.
        :return:
        """
        xp = (int(self.canvas.cget('width')) / 2)
        yp = (int(self.canvas.cget('height')) / 2)
        self.canvas.create_rectangle(0, 0, int(self.canvas.cget('width')) + 10, int(self.canvas.cget('height')) + 10,
                                     fill="gray", stipple="gray50")
        self.canvas.create_rectangle(xp - 13, yp + 25, xp - 3, yp - 50, fill="blue")
        self.canvas.create_rectangle(xp + 3, yp + 25, xp + 13, yp - 50, fill="blue")

    def unBind(self):
        """
        délie les touches de clavier (est utilisé quand on est sur le menu ou pause.
        :return:
        """
        self.frame.grid_forget()
        self.app.tk.unbind('<Key>')
        self.app.tk.unbind('<KeyRelease>')
        self.app.tk.unbind('<' + self.app.config['shoot'] + '>')
        self.app.tk.unbind('<' + self.app.config['pause'] + '>')

    def Bind(self):
        """
        lie les touches avec les actions pour pouvoir jouer
        :return:
        """
        self.frame.grid()
        self.app.tk.bind('<Key>', self.keydown)
        self.app.tk.bind('<KeyRelease>', self.keydownRelease)
        self.app.tk.bind('<' + self.app.config['shoot'] + '>', self.player.shoot)
        self.app.tk.bind('<' + self.app.config['pause'] + '>', self.pauseFct)

    def keydown(self,event):
        """
        vérifie si une touche est baissée et actionne le mouvement si c'est le cas
        :param event: paramètre qui renvoie l'evenement qu'il recoit
        :return:
        """
        if event.keysym == self.app.config['left']:
            self.player.leftMove = True
        if event.keysym == self.app.config['right']:
            self.player.rightMove = True
        pass

    def keydownRelease(self,event):
        """
        vérifie si une touche est relevée et stoppe le mouvement si c'est le cas
        :param event: paramètre qui renvoie l'evenement qu'il recoit
        :return:
        """
        if event.keysym == self.app.config['left']:
            self.player.leftMove = False
        if event.keysym == self.app.config['right']:
            self.player.rightMove = False
        pass

    def retour_menu(self):
        """
        retourne au menu : ferme la game frame et affiche la menu frame.
        :return:
        """
        self.frame.grid_forget()
        self.app.menu = "menu"
        self.app.menuFrame.init()


class SettingsFrame:
    """

    """
    def __init__(self, app):
        self.app = app

        self.frame = None
        self.back = None
        self.pref = None
        self.left = None
        self.right = None
        self.shoot = None
        self.pause = None

        self.init()

    def init(self):
        """

        :return:
        """
        self.frame = tk.Frame(self.app.tk, bg='gray')
        self.frame.grid()

        self.frame.columnconfigure(0, weight=1)
        self.frame.columnconfigure(1, weight=1)

        self.frame.rowconfigure(0)
        self.frame.rowconfigure(1)
        self.frame.rowconfigure(2)
        self.frame.rowconfigure(3)
        self.frame.rowconfigure(4)
        self.frame.rowconfigure(5)

        self.pref = tk.Label(self.frame, text="Préférences clavier", font=("Arial", 25))
        self.pref.grid(columnspan=3, column=0, padx=20, pady=20)

        self.afficher_settings()

        self.back = tk.Button(self.frame, text="Retour", command=self.retour_menu, width=15, font=("Arial", 20))
        self.back.grid(row=5, column=0, columnspan=3, pady=30)
        self.changing = False
        self.changingSection = 'left'
        self.key_pressed = None

    def retour_menu(self):
        """

        :return:
        """
        self.frame.grid_forget()
        self.app.menu = "menu"
        self.app.menuFrame.init()

    def afficher_settings(self):
        """

        :return:
        """
        self.left = tk.Label(self.frame, text="Gauche:", font=("Arial", 25))
        self.left.grid(column=0, pady=30, padx=10)

        self.right = tk.Label(self.frame, text="Droite:", font=("Arial", 25))
        self.right.grid(column=0, pady=30, padx=10)

        self.shoot = tk.Label(self.frame, text="Tirer:", font=("Arial", 25))
        self.shoot.grid(column=0, pady=30, padx=10)

        self.pause = tk.Label(self.frame, text="Pause:", font=("Arial", 25))
        self.pause.grid(column=0, pady=30, padx=10)

        self.key_used()

        self.left_button = tk.Button(self.frame, text="Modifier", command=lambda: self.change_key('left'))
        self.left_button.grid(column=2, pady=30, padx=20, row=1)

        self.right_button = tk.Button(self.frame, text="Modifier", command=lambda: self.change_key('right'))
        self.right_button.grid(column=2, pady=30, padx=40, row=2)

        self.shoot_button = tk.Button(self.frame, text="Modifier", command=lambda: self.change_key('shoot'))
        self.shoot_button.grid(column=2, pady=30, padx=20, row=3)

        self.pause_button = tk.Button(self.frame, text="Modifier", command=lambda: self.change_key('pause'))
        self.pause_button.grid(column=2, pady=30, padx=20, row=4)

    def key_used(self):
        """

        :return:
        """
        self.left_key = tk.Label(self.frame, text=self.app.config.get("left"), font=("Arial", 25))
        self.left_key.grid(column=1, pady=30, row=1)

        self.right_key = tk.Label(self.frame, text=self.app.config.get("right"), font=("Arial", 25))
        self.right_key.grid(column=1, pady=30, row=2)

        self.shoot_key = tk.Label(self.frame, text=self.app.config.get("shoot"), font=("Arial", 25))
        self.shoot_key.grid(column=1, pady=30, row=3)

        self.pause_key = tk.Label(self.frame, text=self.app.config.get("pause"), font=("Arial", 25))
        self.pause_key.grid(column=1, pady=30, row=4)

    def change_key(self, section):
        """

        :param section:
        :return:
        """
        if self.changing == True:
            return
        self.changing = True
        self.changingSection = section
        self.Bind()
        if section == "left":
            self.left_key.config(bg="red")
        if section == "right":
            self.right_key.config(bg="red")
        if section == "shoot":
            self.shoot_key.config(bg="red")
        if section == "pause":
            self.pause_key.config(bg="red")
        return

    def keydown(self, event):
        """

        :param event:
        :return:
        """
        if self.changingSection == "":
            self.unBind()
            return
        if self.changingSection == "left":
            self.left_key.config(text=event.keysym)
            self.left_key.config(bg='blue')

        if self.changingSection == "right":
            self.right_key.config(text=event.keysym)
            self.right_key.config(bg='blue')

        if self.changingSection == "shoot":
            self.shoot_key.config(text=event.keysym)
            self.shoot_key.config(bg='blue')

        if self.changingSection == "pause":
            self.pause_key.config(text=event.keysym)
            self.pause_key.config(bg='blue')

        self.app.config[self.changingSection] = event.keysym
        self.app.update_config()
        self.unBind()
        self.changing = False
        self.changingSection = ""

    def Bind(self):
        """

        :return:
        """
        self.app.tk.bind('<Key>', self.keydown)

    def unBind(self):
        """

        :return:
        """
        self.app.tk.bind('<Key>')

    def validate(self):
        """

        :return:
        """
        key_pressed = keyboard.read_key(suppress=True)  # self.app.configObject.modify_config()
