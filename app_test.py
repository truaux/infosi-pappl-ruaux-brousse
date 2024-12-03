# -*- coding: utf-8 -*-
"""
Created on Fri Nov 22 10:15:28 2024
This module displays graphs and datas

@author: titouan
"""

import tkinter as tk
from tkinter import messagebox, ttk
import calculateur as calc
import input as ipt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd


def draw_figure(canvas, figure):
    """Draw a matplotlib figure onto a Tk canvas using FigureCanvasTkAgg."""
    figure_canvas = FigureCanvasTkAgg(figure, master=canvas)
    figure_canvas.get_tk_widget().pack(fill=tk.BOTH, expand=True)
    figure_canvas.draw()

def click():
    # Extract the data entered by the user
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

    if content is not None:
        Time = pd.to_numeric(readable_content["Temps"], errors="coerce")
        Displacement = pd.to_numeric(readable_content["Deplacement"], errors="coerce")
        Deformation = pd.to_numeric(readable_content["Deformation 1"], errors="coerce")
        Strength = pd.to_numeric(readable_content["Force"], errors="coerce")

        # Graph of displacement
        fig1, ax1 = plt.subplots(dpi=100, constrained_layout=True)
        ax1.plot(Time, Displacement, label="Displacement vs Time", color='blue')
        ax1.set_ylabel("Displacement (mm)")
        ax1.set_xlabel("Time (s)")
        ax1.set_title("Displacement of the Sample")
        ax1.legend()

        # Graph of deformation
        fig2, ax2 = plt.subplots(dpi=100, constrained_layout=True)
        ax2.plot(Time, Deformation, label="Deformation vs Time", color='green')
        ax2.set_ylabel("Deformation (%)")
        ax2.set_xlabel("Time (s)")
        ax2.set_title("Deformation of the Sample")
        ax2.legend()

        # Graph of strength
        fig3, ax3 = plt.subplots(dpi=100, constrained_layout=True)
        ax3.plot(Time, Strength, label="Strength vs Time", color='red')
        ax3.set_ylabel("Strength (kN)")
        ax3.set_xlabel("Time (s)")
        ax3.set_title("Strength Applied on the Sample")
        ax3.legend()

        # Display graphs in tabs
        for tab, fig in zip([tab1, tab2, tab3], [fig1, fig2, fig3]):
            canvas = tk.Canvas(tab)
            canvas.pack(fill=tk.BOTH, expand=True)
            draw_figure(canvas, fig)


# Create the main window
window = tk.Tk()
window.title("Traction Analyzer")
window.geometry("800x600")

# Input Frame
input_frame = tk.Frame(window, padx=10, pady=10)
input_frame.pack(side=tk.TOP, fill=tk.X)

fields = [("Sample Thickness (mm)", "s_thick_e"),
          ("Sample Length (mm)", "s_length_e"),
          ("Sample Width (mm)", "s_width_e"),
          ("Path to CSV File", "path_csv_e")]

entries = {}
for i, (label_text, var_name) in enumerate(fields):
    label = tk.Label(input_frame, text=label_text, font=("Arial", 10))
    label.grid(row=i, column=0, padx=5, pady=5, sticky=tk.W)
    entry = tk.Entry(input_frame, width=30)
    entry.grid(row=i, column=1, padx=5, pady=5)
    entries[var_name] = entry

s_thick_e, s_length_e, s_width_e, path_csv_e = [entries[key] for key in entries]

button = tk.Button(input_frame, text="Plot Data", command=click, bg="blue", fg="white", font=("Arial", 10))
button.grid(row=len(fields), column=0, columnspan=2, pady=10)

# Tabbed Graph Display
tab_control = ttk.Notebook(window)
tab1 = ttk.Frame(tab_control)
tab2 = ttk.Frame(tab_control)
tab3 = ttk.Frame(tab_control)

tab_control.add(tab1, text="Displacement")
tab_control.add(tab2, text="Deformation")
tab_control.add(tab3, text="Strength")

tab_control.pack(expand=1, fill=tk.BOTH)

window.mainloop()