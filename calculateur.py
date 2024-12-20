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
from scipy.stats import linregress

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

def Calcul(table: pd.DataFrame, units: list[(str, str)], length: float, width: float, thickness: float, finalSection: float) -> tuple:
    
    table["Strain"] = (table["Deplacement"] - table["Deplacement"][0])/length
    units.append(("Strain", "(%)"))

    #Yield Stress calculation
    table["dStrength/Strain"] = table["Force"].diff(periods=-1).rolling(20).mean() / table["Strain"].diff(periods=-1).rolling(20).mean()
    table["dStrength/Strain_arranged"] = table["dStrength/Strain"]
    #We set the negative values of the derivative to Not a Number object in order to ignore the part of the graphs after the breaking of the system
    for i in range(table["dStrength/Strain"].size) :
        if table["dStrength/Strain_arranged"][i]<0 :
            table.loc[i, "dStrength/Strain_arranged"]= np.nan
    table["d2Strength/Strain"] = table["dStrength/Strain_arranged"].diff(periods=-1).rolling(20).mean() / table["Strain"].diff(periods=-1).rolling(20).mean()
    #We know that the inflexion point we are searching for is located after we pass half of the overall maximum Strength
    table["d2Strength/Strain_arranged"] = table["d2Strength/Strain"]
    maxStrength = table["Force"].max()
    for i in range(table["d2Strength/Strain"].size) :
        if table["Force"][i]< maxStrength/2:
            table.loc[i, "d2Strength/Strain_arranged"]= np.nan
    index_min = table["d2Strength/Strain_arranged"].idxmin()
    Yield_stress = round(table["Force"][index_min]/(width * thickness * 0.000001))

    #Maximum Stress calculation
    table["Stress"] = table["Force"]/(width * thickness * 0.000001)
    units.append(("Stress", "(kPa)"))
    maxStress = round(table["Stress"].max())

    #Uniform Elongation calculation
    #For this part we should use the formula on the website https://www.rocdacier.com/essai-de-traction-2/ :
    #Module d’élasticité longitudinale (%) : E =F0xL0/S0xDeltaL (avec DeltaL = L-L0)

    #Striction's coefficient calculation
    Z = round((thickness * width - finalSection) / (thickness * width) * 100)

    #Young's modulus calculation
    #We are using only the part of the curve before Re is reached
    stress_subset = table["Stress"].iloc[:index_min + 1]
    strain_subset = table["Strain"].iloc[:index_min + 1]
    
    print("Stress subset:", stress_subset.tolist())
    print("Strain subset:", strain_subset.tolist())

    if len(stress_subset) < 2 or len(strain_subset) < 2:
        raise ValueError("Insufficient data for linear regression.")
    #We are doing a linear regression on it
    slope, intercept, r_value, p_value, std_err = linregress(strain_subset, stress_subset)
    E = round(slope)
    
    return (Yield_stress, maxStress, Z, E)


"""df = ipt.readCSV("2-SS2209_1.csv", ';')
df, units = ipt.extractUnits(df)
df = ipt.dfToFloat(df)
mxS = Calcul(df, units, 38.4, 4, 6)
print(df, units, mxS)"""
