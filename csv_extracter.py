# This module extracts data from a csv file to return it in table form

import csv # Python lybrary for csv files

DELIMITER = ";" # Delimiter in the csv file


def readFile(path: str) -> str:
    """Extracts the content of the file and returns it in a string.
    
    Parameters
    ----------

    path : The file path.
        
    Returns
    -------
    
    content : The content of the file
    """

    with open(path, newline='') as file:
        content = csv.reader(file, DELIMITER)
    
    return content

    


