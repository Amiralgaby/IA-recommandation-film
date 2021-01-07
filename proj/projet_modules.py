#!/usr/bin/env python3

#### IMPORT #############

import numpy as np
import pandas as pd
import sys

##### DEF DE FONCTIONS #######

def print_list_of_list(liste):
    colonne = ["Genres","Score"]
    myList = liste_TO_dataFrame2(liste,colonne)
    print(myList)

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

def obtenirMoyenneToutFilm(smtf):
    som=0
    for i in range(0,len(smtf)):
        som=som+smtf[i]
    return som/len(smtf)

def mettreScoreZeroFilmVu(se,tfu,lfi):
    for i in range(0,len(tfu)):
        for j in range(0,len(lfi)):
            if tfu[i]==lfi[j]:
                se[j]=0
    return se

def mettreAjoutScoreEstime(se,lg,l):
    for i in range(0,len(l)):
        for j in lg:
            if j[0] in l[i]:
                se[i]=se[i]+j[1]
    return se

def scoreAjouterGenre(rat, score):
    switcher = {
        1: score-1,
        2: score-0.5,
        4: score+0.5,
        5: score+1
    }
    return switcher.get(rat,score)

def recupIndexFilmReco(tabse):
    maxi=0
    index=0
    for i in range(0,len(tabse)):
        if tabse[i]>maxi:
            maxi=tabse[i]
            index=i
    return index

def recommanderFilms(se,lfi):
    idReco=[]
    for i in range(0,5):
        ind=recupIndexFilmReco(se)
        idReco.append(lfi[ind])
        se[ind]=0
    return idReco