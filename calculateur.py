# -*- coding: utf-8 -*-
"""
Created on Fri Nov 15 12:32:27 2024
This module calculates physical quantities based on datas

@author: thomas
"""

import pandas as pd

def strainCalcul(table: pd.DataFrame, longueur: float) :
    table["Strain"] = (table["Deplacement"] - table["Deplacement"][0])/longueur
