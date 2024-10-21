# This module extracts data from a csv file to return it in table form

import csv # Python lybrary for csv files

DELIMITER = ";" # Delimiter in the csv file


def readFile(path: str) -> list[list]:
    """Extracts the content of the file and returns it in a string.
    
    Parameters
    ----------

    path : The file path.
        
    Returns
    -------
    
    content : The content of the file
    """

    with open(path, "r", newline='') as file:
        reader = csv.reader(file, delimiter=DELIMITER)
        content = list(reader)
        content = content[:-1] # The last element is an empty list, we remove it
    
    return content



c = readFile('2-SS2209_1.csv')
print(c)



