import matplotlib as mpl
import sys
import numpy as np
import tkinter as tk
mpl.use('TkAgg')
from matplotlib.backends.backend_agg import FigureCanvasAgg
 
fenetre = tk.Tk()
 
def draw_figure(canvas, figure, loc=(0, 0)):
    """ Draw a matplotlib figure onto a Tk canvas
 
    loc: location of top-left corner of figure on canvas in pixels.
    Inspired by matplotlib source: lib/matplotlib/backends/backend_tkagg.py
    """
    figure_canvas_agg = FigureCanvasAgg(figure)
    figure_canvas_agg.draw()
    figure_x, figure_y, figure_w, figure_h = figure.bbox.bounds
    figure_w, figure_h = int(figure_w), int(figure_h)
    photo = tk.PhotoImage(master=canvas, width=figure_w, height=figure_h)
 
    # Position: convert from top-left anchor to center anchor
    canvas.create_image(loc[0] + figure_w/2, loc[1] + figure_h/2, image=photo)
 
    # Unfortunately, there's no accessor for the pointer to the native renderer
    matplotlib.backends.tkagg.blit(photo, figure_canvas_agg.get_renderer()._renderer, colormode=2)
 
    # Return a handle which contains a reference to the photo object
    # which must be kept live or else the picture disappears
    return photo
 
def test():
    # Create a canvas
    w, h = 300, 200
    canvas = tk.Canvas(fenetre, width=w, height=h)
    canvas.grid(row=0, column=1, padx=5, pady=5)
 
    # Generate some example data
    X = np.linspace(0, 2 * np.pi, 50)
    Y = np.sin(X)
 
    # Create the figure we desire to add to an existing canvas
    fig = mpl.figure.Figure(figsize=(2, 1))
    ax = fig.add_axes([0, 0, 1, 1])
    ax.plot(X, Y)
 
    # Keep this handle alive, or else figure will disappear
    fig_x, fig_y = 100, 100
    fig_photo = draw_figure(canvas, fig, loc=(fig_x, fig_y))
    fig_w, fig_h = fig_photo.width(), fig_photo.height()
 
 
bou1 = tk.Button(fenetre, text='CALCUL',command = test)
bou1.grid(row=0, column=0, padx=5, pady=5)
 
fenetre.mainloop()