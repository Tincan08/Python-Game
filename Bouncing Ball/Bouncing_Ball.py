from tkinter import *
from Classes.Ball import Ball
import time

tk = Tk()
tk.title("Game")
tk.resizable(0, 0)
tk.wm_attributes("-topmost", 1)
canvas = Canvas(tk, width=500,height=400,bd=0,highlightthickness=0)
canvas.pack()
tk.update()

ball=Ball(canvas, 'red')

while 1:
    ball.draw()
    tk.update_idletasks()
    tk.update()
    time.sleep(0.01)