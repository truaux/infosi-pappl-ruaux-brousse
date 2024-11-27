# -*- coding: utf-8 -*-
"""
Created on Fri Nov 22 10:15:28 2024
This module displays graphs and datas

@author: titouan
"""

import tkinter as tk
from tkinter import messagebox

def click():
    name = entry.get()
    hello.config(text="Bonjour " + name)
    messagebox.showinfo("Hello", "Bonjour " + name)

#def window
window = tk.Tk()
window.title("Notre app")
window.geometry("400x400")

#def label
hello = tk.Label(window, text = "Hello World",
bg="black",
fg="green",
font=("Arial", 20),
width=20,
height=2)
hello.pack()

#def frame
frame = tk.Frame(window, width=400, height=5)
frame.pack()

#def entry
entry = tk.Entry(window, width=25)
entry.pack()

#def frame
frame = tk.Frame(window, width=400, height=5)
frame.pack()

#def button
button = tk.Button(window,
text="Entrer votre nom",
width=25,
height=2,
bg="red",
fg="white",
command=click)
button.pack()

window.mainloop()
