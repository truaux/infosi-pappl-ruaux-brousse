# -*- coding: utf-8 -*-
"""
Created on Thu Oct 17 10:32:27 2024

@author: titou
"""

import csv
import numpy as np
import matplotlib.pyplot as plt

#llToArray prend en argument la liste de liste de la déformation et la transforme en tableau
#On commance par creer un tableau vide
#Puis on rempli ce tableau vide avec les valeurs voulues en enlevant les deux premieres lignes
#qui ne sont pas des valeurs
def llToArray(ll):
  tab = np.zeros((len(ll),len(ll[0])))
  for i in range(2,len(ll)) :
    for k in range(len(ll[i])) :
      ll[i][k] = ll[i][k].replace(',','.')
      tab[i-1][k] = float(ll[i][k])
  return tab

#on indique le lien vers le fichier qu'on veut ouvrir
chemin_avant = r'2-SS2209_1.csv'
# ouverture en lecture du fichier csv
with open(chemin_avant, newline='') as fichier:
    # on cree un objet reader et on indique quel est le separateur (ici ;)
    lecture = csv.reader(fichier, delimiter=';')

    # on transforme l'iterateur en liste:
    lignes_avant = list(lecture)
    
    # on retransforme cette liste en tableau
    data_avant = llToArray(lignes_avant)
    
#on recupere les differentes lignes du tableau
time = [data_avant[k][0] for k in range(len(data_avant))]  
deplacement = [data_avant[k][1] for k in range(len(data_avant))]
deformation1 = [data_avant[k][2] for k in range(len(data_avant))]
forcekN = [data_avant[k][3] for k in range(len(data_avant))]

forceN = forcekN*1000
deplacementcorrige = deplacement-deplacement[0]

print("entrer la longueur de l'echantillon")
inputString = input()
longueur = float(inputString)

print("entrer la largeur de l'echantillon")
inputString = input()
largeur = float(inputString)

print("entrer l'epaisseur' de l'echantillon")
inputString = input()
epaisseur = float(inputString)

# on cree les graphiques correspondant au differentes variables en fonction du temps
fig, ax = plt.subplots()
ax.plot(time, deplacement)
plt.ylabel("Deplacement (mm)")
plt.xlabel("Temps (s)")
plt.title("Deplacement de l'echantillon en fonction du temps")

fig, ax = plt.subplots()
ax.plot(time, deformation1)
plt.ylabel("Deformation (%)")
plt.xlabel("Temps (s)")
plt.title("Deformation de l'echantillon en fonction du temps")

fig, ax = plt.subplots()
ax.plot(time, forcekN)
plt.ylabel("Force (kN)")
plt.xlabel("Temps (s)")
plt.title("Force appliquée sur l'echantillon en fonction du temps")

plt.show()
