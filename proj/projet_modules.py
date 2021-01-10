#!/usr/bin/env python3

#### IMPORT #############

import numpy as np
import pandas as pd
import sys

##### DEF DE FONCTIONS #######

    # Permet d'obtenir l'utilisateur
def obtenirUser():
    if len(sys.argv) < 2:
        print("Vous pouvez aussi passer l'utilisateur en paramètre")
        print(sys.argv[0]," < id utilisateur >\n")
        user=str(input("Veuillez donner l'id de l'user (ex : 577) : "))
    else:
        user=sys.argv[1]
    return user

    # Affiche la liste des genres
def print_list_of_genres(liste):
    colonne = ["Genres","Score"]
    myList = liste_TO_dataFrame2(liste,colonne)
    print(myList)

    # Permet d'obtenir un dataframe à partir d'un liste et ses colonnes
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

    # Ouvre un fichier et en fait une liste (le fichier doit avoir une mise en format spéciale)
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

    # obtenir la moyenne de tout les films
def obtenirMoyenneToutFilm(smtf):
    som=0
    for i in range(0,len(smtf)):
        som=som+smtf[i]
    return som/len(smtf)

    # Ce que l'utilisateur à déjà vu n'est pas à recommander
def mettreScoreZeroFilmVu(se,tfu,lfi):
    for i in range(0,len(tfu)):
        for j in range(0,len(lfi)):
            if tfu[i]==lfi[j]:
                se[j]=0
    return se

    # Mise à jour du score estimé
def mettreAjoutScoreEstime(se,lg,l):
    for i in range(0,len(l)):
        for j in lg:
            if j[0] in l[i]:
                se[i]=se[i]+j[1]
    return se

    # permet d'ajouter le score selon la note
def scoreAjouterGenre(rat, score):
    switcher = {
        1: score-1,
        2: score-0.5,
        4: score+0.5,
        5: score+1
    }
    return switcher.get(rat,score)

    # Recommande les films
def recommanderFilms(se,lfi):
    idReco=[]
    for i in range(0,5): # Ici on peut changer le nombre de film à recommander
        ind=recupIndexFilmReco(se)
        idReco.append(lfi[ind])
        se[ind]=0
    return idReco