import pandas as pd
import input as ipt
import matplotlib.pyplot as plt



path_csv = "2-SS2209_1.csv"
content = ipt.readCSV(path_csv, delimiter=";")
(readable_content, units) = ipt.extractUnits(content)

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
    plt.show()
