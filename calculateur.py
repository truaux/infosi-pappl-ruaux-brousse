# -*- coding: utf-8 -*-
"""
Created on Fri Nov 15 12:32:27 2024
This module calculates physical quantities based on datas

@author: thomas
"""

import pandas as pd
import numpy as np
import input as ipt

def derivee(y, x):
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
    table["dStress"] = derivee(table["Stress"], table["Strain"])
    E = detConstante(table["dStress"], 5)

    return maxStress, E


df = ipt.readCSV("2-SS2209_1.csv", ';')
df, units = ipt.extractUnits(df)
df = ipt.dfToFloat(df)
mxS = Calcul(df, units, 38.4, 4, 6)
print(df, units, mxS)
