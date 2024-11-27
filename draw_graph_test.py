import tkinter as tk
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib.pyplot as plt
import numpy as np

# Main Tkinter window
fenetre = tk.Tk()

def draw_figure(canvas, figure, loc=(0, 0)):
    """ Draw a matplotlib figure onto a Tk canvas using FigureCanvasTkAgg """
    figure_canvas = FigureCanvasTkAgg(figure, master=canvas)
    widget = figure_canvas.get_tk_widget()
    widget.place(x=loc[0], y=loc[1])
    figure_canvas.draw()

def test():
    # Create a canvas in the Tkinter window
    w, h = 400, 300
    canvas = tk.Canvas(fenetre, width=w, height=h)
    canvas.grid(row=0, column=1, padx=5, pady=5)

    # Generate some example data
    X = np.linspace(0, 2 * np.pi, 50)
    Y = np.sin(X)

    # Create the figure to be drawn on the canvas
    fig, ax = plt.subplots(figsize=(4, 3))
    ax.plot(X, Y)

    # Call the draw_figure function
    draw_figure(canvas, fig)

# Add a button to trigger the graph drawing
bou1 = tk.Button(fenetre, text='CALCUL', command=test)
bou1.grid(row=0, column=0, padx=5, pady=5)

# Start the Tkinter event loop
fenetre.mainloop()