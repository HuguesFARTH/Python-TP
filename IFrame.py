import tkinter as tk

class GameFrame:
    def __init__(self, app):
        self.app = app
        self.init()

    def init(self):
        # GAME
        self.entities = []
        self.score = 0
        self.lives = 3

        # TKINTER
        self.frame = tk.Frame(self.app.tk, bg = 'gray')
        self.frame.pack()
        self.leftFrame = tk.Frame(self.frame)
        self.leftFrame.grid(row = 0, column = 0)
        self.topFrame = tk.Frame(self.leftFrame)
        self.topFrame.grid()
        self.scoreLabel = tk.Label(self.topFrame, text = "Score: " + str(self.score))
        self.scoreLabel.grid(row = 0, column = 0)
        self.invi1 = tk.Label(self.topFrame, text="")
        self.invi1.grid(row = 0, column = 2, padx = 100)
        self.lifeLabel = tk.Label(self.topFrame, text = "Lives: " + str(self.lives))
        self.lifeLabel.grid(row = 0, column = 3)

        self.canvas  = tk.Canvas(self.leftFrame, bg = 'black', width = 900, height = 550)
        self.canvas.grid(row = 1)

        self.rightFrame = tk.Frame(self.frame, bg = 'white')
        self.rightFrame.grid(row = 0, column = 1)
        self.rejouerButton = tk.Button(self.rightFrame, text = "New game", command = self.newgame)
        self.rejouerButton.grid(row = 0)
        self.quitButton = tk.Button(self.rightFrame, text = "New game", command = self.app.main.stop)
        self.quitButton.grid(row = 1)

    def newgame(self):
        print("newgame")

    def update(self):
        # print("Update Frame")
        # self.i += 1
        for ent in self.entities:
            ent.update()

    def draw(self):
        self.canvas.delete("all")
        self.canvas.create_oval(100,100,200,200,fill = "white")

    def unBind(self):
        self.frame.pack_forget()
