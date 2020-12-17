#!/usr/bin/env python3

#### IMPORT #############

import numpy as np
import pandas as pd
import sys

##### DEF DE FONCTIONS #######

def print_list(liste):
	for i in liste:
		print(i)


def print_list_of_list(liste):
	for i in liste:
		print_list(i)

def liste_TO_dataFrame(liste,columms):
	return liste_TO_dataFrame2(liste,columms)

def liste_TO_dataFrame2(liste,columms):
    assert len(columms) == len(liste[0])
    colList = [ [] for _ in columms]
    for i in liste:
        for j in range(0,len(columms)):
            colList[j].append(i[j])
    d = {}
    for i in range(0,len(colList)):
        d[columms[i]] = pd.Series(colList[i])
    df = pd.DataFrame(d)
    return df

def obtenirListe(fichierAOuvrir):
    try:
        print("[INFO]Ouverture du fichier",fichierAOuvrir,end='\n')
        f = open(fichierAOuvrir, 'r')
        # là ça fait une liste de liste
        l = [ list(line.strip('\n').split('::')) for line in f ]
    except Exception as e:
        print("le problème vient du fichier : ",fichierAOuvrir)
        raise e
    else:
        print("[INFO]Réussi",end='\n')
    return l

def recupIndexFilmReco(tabse):
	maxi=0
	index=0
	for i in range(0,len(tabse)):
		if tabse[i]>maxi:
			maxi=tabse[i]
			index=i
	return index
