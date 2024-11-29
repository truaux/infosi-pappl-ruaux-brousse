# -*- coding: utf-8 -*-
"""
Created on Fri Nov 15 12:32:27 2024
This module calculates physical quantities based on datas

@author: thomas
"""

import pandas as pd

def Calcul(table: pd.DataFrame, length: float, width: float, thickness: float) :
    table["Strain"] = (table[1] - table[1][0])/longueur
    table["Stress"] = table[3]/(width * thickness)
    
