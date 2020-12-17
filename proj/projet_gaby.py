#!/usr/bin/env python3

#### IMPORT #############

import numpy as np
import pandas as pd
import sys

#### UTILS ###########

import projet_data as data
# data.dfRatings
# data.dfMovies
# data.dfUser

import projet_modules as mod
# les fonctions n'utilisant pas les data sont dans ce module

###### FUNCTION #########

def obtenirScoreMoyUser(user):
    sul=[]
    for i in data.dfRatings.loc[data.dfRatings['UserID'] == str(user)].index.values:
        sul.append(data.dfRatings.loc[i,'Rating'])
    somme=sum((int(i) for i in sul))
    long=len(sul)
    return somme/long

def obtenirScoreMoyToutFilm(tab):
	tab2=[]
	for i in tab:
		somme=0
		nb=0
		for j in data.dfRatings.loc[data.dfRatings['MovieID'] == str(i)].index.values:
			somme=somme+int(data.dfRatings.loc[j,'Rating'])
			nb=nb+1
		if nb!=0:
			tab2.append(somme/nb)
		else:
			tab2.append(0)
	return tab2

def obtenirListeFilmUser(user):
	tab=[]
	for i in data.dfRatings.loc[data.dfRatings['UserID'] == str(user)].index.values:
		tab.append(data.dfRatings.loc[i,'MovieID'])
	return tab

########## SCRIPT ##########

score = obtenirScoreMoyUser(1)
print(score)