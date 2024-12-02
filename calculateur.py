# %%
# -*- coding: utf-8 -*-
"""
Created on Fri Nov 15 12:32:27 2024
This module calculates physical quantities based on datas

@author: thomas
"""

import pandas as pd
import numpy as np
import input as ipt
import matplotlib.pyplot as plt

def derivee(y: list[float], x: list[float]) -> list[float]:
    """Calculates the derivative of points of y with respect to x.

    Parameters
    ----------

    y : List of points to derive.

    x : List of points relative to which the derivative is calculated.

    Returns
    -------

    d : List of derived points.
    """ 

    d = []
    for i in range(0, len(y)-1):
        dy = y[i+1]-y[i]
        dx = x[i+1]-x[i]
        d.append(dy/dx)
    d.append(0)

    return d


def detConstante(curve: list[float], margin: int) -> float:
    start = curve[0]
    interval = margin * start / 100
    i = 0
    while curve[i] < start + interval:
        i += 1
    return np.around(np.mean(curve[:i]), 2)



def Calcul(table: pd.DataFrame, units: list[(str, str)], length: float, width: float, thickness: float) -> tuple:
    table["Strain"] = (table["Deplacement"] - table["Deplacement"][0])/length
    units.append(("Strain", "(%)"))
    table["Stress"] = table["Force"]/(width * thickness)
    units.append(("Stress", "(Pa)"))
    maxStress = table["Stress"].max()
    table["dStress"] = table["Stress"].diff(periods=-1).rolling(20).mean() / table["Strain"].diff(periods=-1).rolling(20).mean()
    table["d2Stress"] = table["dStress"].diff(periods=-1).rolling(20).mean() / table["Strain"].diff(periods=-1).rolling(20).mean()
    E = detConstante(table["dStress"], 5)
    
    plt.plot(table["Strain"], table["d2Stress"])

    return maxStress, E


df = ipt.readCSV("2-SS2209_1.csv", ';')
df, units = ipt.extractUnits(df)
df = ipt.dfToFloat(df)
mxS = Calcul(df, units, 38.4, 4, 6)
print(df, units, mxS)

# %%
