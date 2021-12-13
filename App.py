import tkinter as tk
from PIL import Image,ImageTk
import ILib
import random

class App():
    def __init__(self):
        print("init App")
        self.tk = tk.Tk()
        self.tk.geometry("1000x500")
