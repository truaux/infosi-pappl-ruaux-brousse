import tkinter as tk
from tkinter import messagebox

"""def click():
    name = entry.get()
    hello.config(text="Bonjour " + name)
    messagebox.showinfo("Hello", "Bonjour " + name)"""

#def window
window = tk.Tk()
window.title("Traction Analyser")
window.geometry("400x400")

#entry of the value of the sample thickness
#def label
s_thick = tk.Label(window, text = "Sample thickness",
bg="white",
fg="black",
font=("Arial", 11),
width=11)
s_thick.pack()

#def frame
frame = tk.Frame(window, width=400, height=5)
frame.pack()

#def entry
s_thick_e = tk.Entry(window,
width=25)
s_thick_e.pack()

frame.pack()

#entry of the value of the sample length
#def label
s_length = tk.Label(window, text = "Sample length",
bg="white",
fg="black",
font=("Arial", 11),
width=11)
s_length.pack()

frame.pack()

#def entry
s_length_e = tk.Entry(window,
width=25)
s_length_e.pack()

frame.pack()

#entry of the value of the sample width
#def label
s_length = tk.Label(window, text = "Sample width",
bg="white",
fg="black",
font=("Arial", 11),
width=11)
s_length.pack()

frame.pack()

#def entry
s_width_e = tk.Entry(window,
width=25)
s_width_e.pack()

frame.pack()

#entry of the value of path to the csv file
#def label
path_csv = tk.Label(window, text = "Path to .csv file",
bg="white",
fg="black",
font=("Arial", 11),
width=11)
path_csv.pack()

frame.pack()

#def entry
path_csv_e = tk.Entry(window,
width=25)
path_csv_e.pack()

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