# This module extracts data from a csv file to return it in table form

import csv # Python lybrary for csv files
import numpy as np

DELIMITER = ";" # Delimiter in the csv file


class WrongFileExtensionError(Error):
    """Exception raised for error in the extension of a file.

    Attributes
    ----------
    
    file : name of the file whose extension is not supported
    message : explanation of the error
    """

    def _init_(self, file, message):
        self.file = file
        self.message = message

def readFile(path: str) -> list[list]:
    """Extracts the content of the file and returns it in a list of lists.
    
    Parameters
    ----------

    path : The file path.
        
    Returns
    -------
    
    content : The content of the file
    """

    try:
        with open(path, "r", newline='') as file:
            reader = csv.reader(file, delimiter=DELIMITER)
    except FileNotFoundError:
        print("FileNotFoundError : can't find the file " + path + ". Please check the name or the location.")
        content = [[]]
    else:
        if not path[-4:] == ".csv":
            print("Wrong")
        content = list(reader) # cout de cette operation, et impacte pour un grand nombre de donnees ?
        content = content[:-1] # The last element is an empty list, we remove it
        

    return content


# J'ai choisi un dictionnaire, mais on pourrait aussi prendre une liste de tuples (la 'transposee' de celle en entree)
# ou chaque tuple est de la forme ('grandeur', 'unite', [donnee1, donnee2,...])
def listToDict(lst: list[list]) -> dict[(str, np.array)]:
    """Let n be the length of lst. Creates n array containing each time the i-th element of lists in lst (except the first 2).
    Values of the first list in lst are used as dictionnary keys and are associated with the couple (value of the second list, array).

    Parameters
    ----------

    lst :
        List of lists containing digital datas except for the first 2 : in the first one, values are names of physical quantities and 
        in the second one, values are units of measurment.
    
    Returns
    -------

    dic :
        Dictionnary where keys are values of the first list in lst, and values are the couples (unit of measurment, list of datas).
    """

    dic = {}
    for i in range(0, len(lst[0])):
        key = lst[0][i] # String for physical quantity
        unit = lst[1][i] # String for unit of measurment
        tab = np.zeros(len(lst)-2) # Array for digital datas
        
        for j in range(0, len(tab)):
            num = lst[j+2][i]
            num = num.replace(",", ".") # Replace ',' with '.' because Python uses '.' for floats
            tab[j] = num

        dic[key] = (unit, tab)
    
    return dic


print(readFile("2-SS2209.csv"))