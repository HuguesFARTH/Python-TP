import tkinter as tk


class Projectile:
    def __init__(self, app, parent, dir: list, pos: list[float]):
        self.app = app
        self.parent = parent
        self.dir = dir
        self.pos = pos
        self.draw()


    def draw(self):
        self.parent.create_oval(self.pos[0]-5, self.pos[1]-5 ,self.pos[0]+5 , self.pos[1]+5, fill = "red" )

    def update(self):
        self.parent.delete("all")
        self.pos[0] = self.pos[0]*self.dir[0]
        self.pos[1] = self.pos[1]*self.dir[1]
        self.parent.create_oval(self.pos[0]-5, self.pos[1]-5 ,self.pos[0]+5 , self.pos[1]+5, fill = "red" )

        pass

        
    

  





root = tk.Tk()
root.geometry("600x600")
parent = tk.Canvas(root, width=500, height=500, bg= 'blue')

parent.pack()
proj = Projectile(2,parent,[1.01,1.03], [200,220])

btn = tk.Button(root, text='bonjour', command= lambda: proj.update())
btn.pack()


root.mainloop()
