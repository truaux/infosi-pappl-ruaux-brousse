import tkinter as tk
from tkinter import messagebox
import calculateur as calc
import csv_extracter as csvex

def click():
    """When click on the button, uses the values entered by the user to calculate and display the curves"""
    s_thick = s_thick_e.get()
    s_lenght = s_length_e.get()
    s_width = s_width_e.get()
    path_csv = path_csv_e.get()
    content = csvex.readCSVFile(path_csv)
    
#def window
window = tk.Tk()
window.title("Traction Analyser")
window.geometry("400x400")

#entry of the value of the sample thickness
#def label
s_thick_l = tk.Label(window, text = "Sample thickness",
fg="black",
font=("Arial", 9),
width=20)
s_thick_l.pack()

#def frame
frame = tk.Frame(window, width=400, height=5)
frame.pack()

#def entry
s_thick_e = tk.Entry(window,
width=25)
s_thick_e.pack()

#def frame
frame = tk.Frame(window, width=400, height=5)
frame.pack()

#entry of the value of the sample length
#def label
s_length_l = tk.Label(window, text = "Sample length",
fg="black",
font=("Arial", 9),
width=20)
s_length_l.pack()

#def frame
frame = tk.Frame(window, width=400, height=5)
frame.pack()

#def entry
s_length_e = tk.Entry(window,
width=25)
s_length_e.pack()

#def frame
frame = tk.Frame(window, width=400, height=5)
frame.pack()

#entry of the value of the sample width
#def label
s_width_l = tk.Label(window, text = "Sample width",
fg="black",
font=("Arial", 9),
width=20)
s_width_l.pack()

#def frame
frame = tk.Frame(window, width=400, height=5)
frame.pack()

#def entry
s_width_e = tk.Entry(window,
width=25)
s_width_e.pack()

#def frame
frame = tk.Frame(window, width=400, height=5)
frame.pack()

#entry of the value of path to the csv file
#def label
path_csv_l = tk.Label(window, text = "Path to .csv file",
fg="black",
font=("Arial", 9),
width=20)
path_csv_l.pack()

#def frame
frame = tk.Frame(window, width=400, height=5)
frame.pack()

#def entry
path_csv_e = tk.Entry(window,
width=25)
path_csv_e.pack()

#def frame
frame = tk.Frame(window, width=400, height=5)
frame.pack()

#def button
button = tk.Button(window,
text="Entry values and file",
width=25,
height=2,
bg="red",
fg="white",
command=click)
button.pack()

window.mainloop()