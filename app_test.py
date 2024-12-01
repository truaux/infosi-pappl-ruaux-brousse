# -*- coding: utf-8 -*-
"""
Created on Fri Nov 22 10:15:28 2024
This module displays graphs and datas

@author: titouan
"""

import tkinter as tk
from tkinter import messagebox
import calculateur as calc
import input as ipt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

def draw_figure(canvas, figure, loc=(0, 0)):
    """ Draw a matplotlib figure onto a Tk canvas using FigureCanvasTkAgg """
    figure_canvas = FigureCanvasTkAgg(figure, master=canvas)
    widget = figure_canvas.get_tk_widget()
    widget.place(x=loc[0], y=loc[1])
    figure_canvas.draw()

def click_test():
    # Création d'un graphique simple
    X = np.linspace(0, 2 * np.pi, 50)
    Y = np.sin(X)
    fig, ax = plt.subplots(figsize=(4, 3))
    ax.plot(X, Y)
    ax.set_title("Test Sinusoïde")

    # Création d'un canvas
    fig_width, fig_height = fig.get_size_inches()
    canvas_width, canvas_height = fig_width * 100, fig_height * 100
    canvas = tk.Canvas(window, width=canvas_width, height=canvas_height)
    draw_figure(canvas, fig)

def click():

    #Extract the data entered by the user
    try:
        s_thick = float(s_thick_e.get())
        s_length = float(s_length_e.get())
        s_width = float(s_width_e.get())
    except ValueError:
        messagebox.showerror("Input Error", "Please enter valid numerical values.")
        return

    path_csv = path_csv_e.get()

    content = ipt.readCSV(path_csv, delimiter=";")
    (readable_content, units) = ipt.extractUnits(content)

    # Create a canvas in the Tkinter window
    canvas = tk.Canvas(window, width=400, height=300)
    canvas.grid(row=5, column=0, columnspan=2, padx=5, pady=5)

    # Create the figure to be drawn on the canvas
    if content is not None:
        Time = pd.to_numeric(readable_content["Temps"], errors="coerce")
        Displacement = pd.to_numeric(readable_content["Deplacement"], errors="coerce")
        Deformation = pd.to_numeric(readable_content["Deformation 1"], errors="coerce")
        Strength = pd.to_numeric(readable_content["Force"], errors="coerce")
        fig, ax = plt.subplots(figsize=(4, 3))
        ax.plot(Time, Displacement, label="Force vs Temps", color='blue')

        # Ajouter des titres et légendes
        ax.set_title("Force en fonction du Temps")
        ax.set_xlabel("Temps (s)")
        ax.set_ylabel("Force (kN)")
        ax.grid(True)
        ax.legend()

        # Ajuster l'échelle des axes
        """ax.set_xlim(min(Time), max(Time))
        ax.set_ylim(min(Displacement), max(Displacement))"""

        # Afficher la figures
        draw_figure(canvas, fig)
    
#def window
window = tk.Tk()
window.title("Traction Analyser")
window.geometry("450x600")

# Labels and Entry widgets
fields = [("Sample Thickness", "s_thick_e"), 
          ("Sample Length", "s_length_e"), 
          ("Sample Width", "s_width_e"), 
          ("Path to CSV File", "path_csv_e")]

entries = {}

for i, (label_text, var_name) in enumerate(fields):
    label = tk.Label(window, text=label_text, font=("Arial", 9))
    label.grid(row=i, column=0, padx=5, pady=5)
    entry = tk.Entry(window, width=25)
    entry.grid(row=i, column=1, padx=5, pady=5)
    entries[var_name] = entry

s_thick_e, s_length_e, s_width_e, path_csv_e = [entries[key] for key in entries]

# Button to trigger plot
button1 = tk.Button(window, text="Plot Data", command=click, bg="red", fg="white")
button1.grid(row=4, column=0, columnspan=2, pady=10)

window.mainloop()