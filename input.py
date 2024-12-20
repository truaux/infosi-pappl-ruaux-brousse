# -*- coding: utf-8 -*-
"""
Created on Thu Oct 27 16:02:27 2024
This module extracts data from a csv file to return it in a dataframework

@author: thomas
"""

import pandas as pd
import os
import chardet
import unidecode as undc
from io import StringIO


def readCSV(path: str, delimiter: str =",") -> pd.DataFrame:
    """Extracts the content of the csv file and returns it in a pd object DataFrame.
    
    Parameters
    ----------

    path : The csv file path.

    delimiter : The separator used in the csv file. ',' is used by default.
        
    Returns
    -------
    
    content : DataFrame containing datas from the csv file.
    """

    extension = os.path.splitext(path)[1]
    if extension != ".csv":
        print("Extension error : '" + extension + "' extension detected. Only csv files are supported.")
        content = pd.DataFrame()
    else :
        try:
            with open(path) as file:                
                text = file.read()
                text = undc.unidecode(text) # Remove accents
                content = pd.read_csv(StringIO(text), sep=delimiter)
        except FileNotFoundError:
            print("File not found : can't find the file " + path + ". Please check the name or the location.")
            content = pd.DataFrame()
        except UnicodeDecodeError:
            content = pd.read_csv(path, sep=delimiter, encoding='iso-8859-1')
        except pd.errors.ParserError:
            print("Parsing error : can't parse the file with the indicated delimiter '" + delimiter +"'. Please choose an other delimiter.")
            content = pd.DataFrame()
    return content


def dfToFloat(table: pd.DataFrame) -> pd.DataFrame:
    """Convert integer values of table in float type.

    Parameters
    ----------

    table : DataFrame containing datas.

    Returns
    -------

    table : DataFrame containing floats datas.
    """
    
    for column in table:
        for i in range(0, len(table[column])):
            value = str(table[column][i])
            try:
                value = value.replace(",", ".")
                value = float(value)
            except ValueError:
                print("Some values aren't float.")
            finally :
                table.loc[i, column] = value
    table = table.astype(float)
    return table


def extractUnits(table: pd.DataFrame) -> (pd.DataFrame, list[(str, str)]):
    """Extracts units from a DataFrame in a list of couples (quantity, unit).

    Parameters
    ----------

    table : The DataFrame containing datas.

    Returns
    -------

    table : The DataFrame without its first row.

    units : The list containing couples (quantity, unit).
    """

    units = []
    for column in table:
        units.append((column, table[column][0]))
    table = table.drop(table.index[[0]])
    table = table.reset_index(drop=True)
    
    return table, units

