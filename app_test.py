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

def click():
    # Extract the data entered by the user
    try:
        s_thick = float(s_thick_e.get())
        s_length = float(s_length_e.get())
        s_width = float(s_width_e.get())
        s_fsection = float(s_fsection_e.get())
    except ValueError:
        messagebox.showerror("Input Error", "Please enter valid numerical values.")
        return

    path_csv = path_csv_e.get()

    content = ipt.readCSV(path_csv, delimiter=";")
    (readable_content, units) = ipt.extractUnits(content)
    readable_content = ipt.dfToFloat(readable_content)

    if content is not None:

        #Calculate the data
        new_readable_content = ipt.dfToFloat(readable_content)
        results = calc.Calcul(new_readable_content, units, s_length, s_width, s_thick, s_fsection)

        Yield_stress = results[0]
        Max_stress = results[1]
        Uniform_elong = 0
        Striction_coef = results[2]
        Young_modul = results[3]

        # Update graphs dynamically
        Time = pd.to_numeric(readable_content["Temps"], errors="coerce")
        Displacement = pd.to_numeric(readable_content["Deplacement"], errors="coerce")
        Deformation = pd.to_numeric(readable_content["Deformation 1"], errors="coerce")
        Strength = pd.to_numeric(readable_content["Force"], errors="coerce")
        Strain = pd.to_numeric(new_readable_content["Strain"], errors="coerce")
        Stress = pd.to_numeric(new_readable_content["Stress"], errors="coerce")

        # Add new curves with unique labels
        run_number = len(ax1.lines) + 1
        ax1.plot(Time, Deformation, label=f"Run {len(ax1.lines)+1}")
        ax2.plot(Displacement, Strength, label=f"Run {len(ax2.lines)+1}")
        ax3.plot(Strain, Strength, label=f"Run {len(ax3.lines)+1}")
        ax4.plot(Strain, Stress, label=f"Run {len(ax4.lines)+1}")

        # Set axis labels and titles for all graphs
        ax1.set_xlabel("Time (s)")
        ax1.set_ylabel("Deformation (%)")
        ax1.set_title("Deformation vs. Time")

        ax2.set_xlabel("Displacement (mm))")
        ax2.set_ylabel("Strength (kN)")
        ax2.set_title("Strength vs. Displacement")

        ax3.set_xlabel("Strain (%)")
        ax3.set_ylabel("Strength (kN)")
        ax3.set_title("Strength vs. Strain")

        ax4.set_xlabel("Strain (%)")
        ax4.set_ylabel("Stress (kPa)")
        ax4.set_title("Stress vs. Strain")

        # Update legends for all axes
        for ax in [ax1, ax2, ax3, ax4]:
            ax.legend(loc="best", fontsize="small", title="Legend")

        # Refresh the canvases
        canvas1.draw()
        canvas2.draw()
        canvas3.draw()
        canvas4.draw()

        # Update the table in tab5
        if not hasattr(click, "treeview"):
            # Create the table only the first time
            columns = ("Set of data n°","Yield Stress Re (kPa)", "Max Stress Rm (kPa)", "Uniform Elongation ()", "Striction Coefficient Z% (%)", "Young's Modulus E (kPa)")
            click.treeview = ttk.Treeview(tab5, columns=columns, show="headings")
            for col in columns:
                click.treeview.heading(col, text=col)
                click.treeview.column(col, width=150, anchor="center")
            click.treeview.pack(fill=tk.BOTH, expand=True)
            # Initialize a counter for the number of runs
            click.run_counter = 0

        # Increment the run counter
        click.run_counter += 1

        # Insert new data as a row
        click.treeview.insert("", "end", values=(click.run_counter, Yield_stress, Max_stress, Uniform_elong, Striction_coef, Young_modul))

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
          ("Sample Final Section (mm²)", "s_fsection_e"),
          ("Path to CSV File", "path_csv_e")]

entries = {}
for i, (label_text, var_name) in enumerate(fields):
    label = tk.Label(input_frame, text=label_text, font=("Arial", 10))
    label.grid(row=i, column=0, padx=5, pady=5, sticky=tk.W)
    entry = tk.Entry(input_frame, width=30)
    entry.grid(row=i, column=1, padx=5, pady=5)
    entries[var_name] = entry

s_thick_e, s_length_e, s_width_e, s_fsection_e, path_csv_e = [entries[key] for key in entries]

button = tk.Button(input_frame, text="Plot Data", command=click, bg="blue", fg="white", font=("Arial", 10))
button.grid(row=len(fields), column=0, columnspan=2, pady=10)

# Create figures and axes outside of the click function
fig1, ax1 = plt.subplots(dpi=100, constrained_layout=True)
ax1.grid()
fig2, ax2 = plt.subplots(dpi=100, constrained_layout=True)
ax2.grid()
fig3, ax3 = plt.subplots(dpi=100, constrained_layout=True)
ax3.grid()
fig4, ax4 = plt.subplots(dpi=100, constrained_layout=True)
ax4.grid()

# Tabbed Graph Display
tab_control = ttk.Notebook(window)
tab1 = ttk.Frame(tab_control)
tab2 = ttk.Frame(tab_control)
tab3 = ttk.Frame(tab_control)
tab4 = ttk.Frame(tab_control)
tab5 = ttk.Frame(tab_control)

tab_control.add(tab1, text="Deformation")
tab_control.add(tab2, text="Strength/Displacement")
tab_control.add(tab3, text="Strength/Strain")
tab_control.add(tab4, text="Stress/Strain")
tab_control.add(tab5, text="Data calculated")

tab_control.pack(expand=1, fill=tk.BOTH)

# Create Canvas for each tab
canvas1 = FigureCanvasTkAgg(fig1, master=tab1)
canvas1.get_tk_widget().pack(fill=tk.BOTH, expand=True)
canvas2 = FigureCanvasTkAgg(fig2, master=tab2)
canvas2.get_tk_widget().pack(fill=tk.BOTH, expand=True)
canvas3 = FigureCanvasTkAgg(fig3, master=tab3)
canvas3.get_tk_widget().pack(fill=tk.BOTH, expand=True)
canvas4 = FigureCanvasTkAgg(fig4, master=tab4)
canvas4.get_tk_widget().pack(fill=tk.BOTH, expand=True)

window.mainloop()