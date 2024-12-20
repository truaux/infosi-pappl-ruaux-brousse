# -*- coding: utf-8 -*-
"""
Created on Fri Nov 15 12:32:27 2024
This module calculates physical quantities based on datas

@author: thomas
"""

import pandas as pd
import numpy as np
from scipy.stats import linregress


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
    UE = round(table["Force"].iloc[index_min] * length / (width * thickness * (table["Deplacement"].iloc[index_min] - table["Deplacement"].iloc[0])), 2)
    units.append(("Uniform Elongation", "(%)"))

    #Striction's coefficient calculation
    Z = round((thickness * width - finalSection) / (thickness * width) * 100)

    #Young's modulus calculation
    #We are using only the part of the curve before Re is reached
    stress_subset = table["Stress"].iloc[:index_min + 1]
    strain_subset = table["Strain"].iloc[:index_min + 1]
    
    if len(stress_subset) < 2 or len(strain_subset) < 2:
        raise ValueError("Insufficient data for linear regression.")
    #We are doing a linear regression on it
    slope, intercept, r_value, p_value, std_err = linregress(strain_subset, stress_subset)
    E = round(slope)
    
    return (Yield_stress, maxStress, Z, E, UE)
