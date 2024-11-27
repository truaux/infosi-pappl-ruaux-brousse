# -*- coding: utf-8 -*-
"""
Created on Thu Oct 27 16:02:27 2024
This module extracts data from a csv file to return it in a dataframework

@author: thomas
"""

import pandas as pd
import os
import chardet


def readCSV(path: str, delimiter: str =",") -> pd.DataFrame:
    """Extracts the content of the csv file and returns it in a pd object DataFrame.
    
    Parameters
    ----------

    path : The csv file path.

    delimiter : The separator used in the csv file. ',' is used by default.
        
    Returns
    -------
    
    content : DataFrame containing datas from the csv file
    """

    extension = os.path.splitext(path)[1]
    if extension != ".csv":
        print("Extension error : '" + extension + "' extension detected. Only csv files are supported.")
        content = pd.DataFrame()
    else :
        try:
            content = pd.read_csv(path, sep=delimiter)
        except FileNotFoundError:
            print("File not found : can't find the file " + path + ". Please check the name or the location.")
            content = pd.DataFrame()
        except UnicodeDecodeError:
            with open(path) as file:
                text = file.read()
                encoding = chardet.detect(text)
                content = pd.read_csv(path, sep=delimiter, encoding=encoding)
        except pd.errors.ParserError:
            print("Parsing error : can't parse the file with the indicated delimiter '" + delimiter +"'. Please choose an other delimiter.")
            content = pd.DataFrame()
        finally:
            print(content)

    return content


readCSV("2-SS2209_1.csv", ";")
