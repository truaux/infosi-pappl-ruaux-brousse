# -*- coding: utf-8 -*-
"""
Created on Fri Nov 15 12:32:27 2024
This module calculates physical quantities based on datas

@author: thomas
"""

import pandas as pd
import input as ipt

def Calcul(table: pd.DataFrame, length: float, width: float, thickness: float) :
    table["Strain"] = (table["Deplacement"] - table["Deplacement"][2])/longueur
    table["Stress"] = table["Force"]/(width * thickness)
    maxStress = table["Stress"].max()


"""df = ipt.readCSV("2-SS2209_1.csv", ';')
print(df)
print(df.dtypes)
Calcul(df, 38.4, 4, 6)
print(df)"""
