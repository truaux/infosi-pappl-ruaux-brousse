# -*- coding: utf-8 -*-
"""
Created on Fri Nov 15 12:32:27 2024
This module calculates physical quantities based on datas

@author: thomas
"""


def inputSize(measure: str) -> float:
    """Returns the value entered by the user for the requested measurement.

    Parameters
    ----------

    measure : name of the resquested mesasurment

    Returns
    -------

    measurement: value of the measure entered by the user
    """

    inputString = input("Please enter the " + measure + " of the sample (in mm) : ")
    try:
        measurement = float(inputString)
    except ValueError:
        print("ValueError : Please make sure that your entry is a float.")
        inputSize(measure)
    else:
        return measurement

length = inputSize("length")
width = inputSize("width")
thickness = inputSize("thickness")