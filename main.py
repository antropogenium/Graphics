from turtle import *
from time import sleep as s
from rgbprint import Color as c
from os import system as s
from readchar import readkey as k
from tkinter import *

screen = Screen()
canvas = screen.getcanvas()
screen.setup(width=1200, height=500)
delay(0)
color('black')
ht()
teleport(-450)
title("Gr1")
speed(999^9999)

def butt1():
	color('green')
	right(280)
	forward(55)
	right(80)
	
def butt2():
	color('red')
	right(80)
	forward(55)
	right(280)

def butt3():
	undo()
	undo()
	undo()
	undo()
	ht()

button1 = Button(canvas.master, text="UP", command=butt1)
button1.pack()
button1.place(x=22, y=11)

button2 = Button(canvas.master, text="DOWN", command=butt2)
button2.pack()
button2.place(x=22, y=44)

button3 = Button(canvas.master, text="UNDO", command=butt3)
button3.pack()
button3.place(x=22, y=77)

screen.mainloop()