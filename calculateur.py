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
    
    #Yield Stress calculation
    table["dStrength"] = table["Force"].diff(periods=-1).rolling(20).mean() / table["Temps"].diff(periods=-1).rolling(20).mean()
    table["dStrength_arranged"] = table["dStrength"]
    #We set the negative values of the derivative to Not a Number object in order to ignore the part of the graphs after the breaking of the system
    for i in range(table["dStrength"].size) :
        if table["dStrength_arranged"][i]<0 :
            table["dStrength_arranged"][i]= np.nan
    table["d2Strength"] = table["dStrength_arranged"].diff(periods=-1).rolling(20).mean() / table["Temps"].diff(periods=-1).rolling(20).mean()
    table["d2Strength_avg_1s"] = table["d2Strength"]
    #We search for the period of the experiment with the most important inflexion through time so we are doing an average of the second derivative on 1s
    for i in range(table["dStrength_arranged"].size) :
        if i<(table["dStrength_arranged"].size-10) :
            table["d2Strength_avg_1s"][i] = table["dStrength_arranged"][i+10] - table["dStrength_arranged"][i]
    index_period_min = table.loc[table["d2Strength_avg_1s"] == table["d2Strength_avg_1s"].min()].index.item()
    #When we have the period, we search for the minimum in that period
    index_min = table.loc[table["d2Strength"][index_period_min:index_period_min+10] == table["d2Strength"].min()].index.item()
    Yield_stress = table["Force"][index_min]

    #maxStress calculation
    table["Stress"] = table["Force"]/(width * thickness * 0.000001)
    units.append(("Stress", "(kPa)"))
    maxStress = round(table["Stress"].max())

    #Young's modulus calculation
    table["Strain"] = (table["Deplacement"] - table["Deplacement"][0])/(length * 0.001)
    units.append(("Strain", "(%)"))
    table["dStress"] = table["Stress"].diff(periods=-1).rolling(20).mean() / table["Strain"].diff(periods=-1).rolling(20).mean()
    table["d2Stress"] = table["dStress"].diff(periods=-1).rolling(20).mean() / table["Strain"].diff(periods=-1).rolling(20).mean()
    E = detConstante(table["dStress"], 5)

    

    return (Yield_stress, maxStress, E)


"""df = ipt.readCSV("2-SS2209_1.csv", ';')
df, units = ipt.extractUnits(df)
df = ipt.dfToFloat(df)
mxS = Calcul(df, units, 38.4, 4, 6)
print(df, units, mxS)"""

# %%
