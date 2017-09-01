from tkinter import *
from colormap import rgb2hex
import requests, json

class Color():
    def __init__(self, name="", red=0, green=0, blue=0):
        self.name = name
        self.red = str(red)
        self.green = str(green)
        self.blue = str(blue)

    def hex(self):
        return rgb2hex(self.red, self.green, self.blue)



root = Tk()

f = Frame(width=400, height=400, bg="red")
f.pack()

while True:
    r = requests.get("http://127.0.0.1:5000/color")
    print(r.content)
    data = json.loads(r.content.decode())
    red = data['color']['Red']
    green = data['color']['Green']
    blue = data['color']['Blue']
    f.config(bg=rgb2hex(int(red), int(green), int(blue)))
    root.update()
    root.update_idletasks()