#!/usr/bin/env python3

#### IMPORT #############

import numpy as np
import pandas as pd
import sys

import projet_modules

pathToRoot = "../"

#### DATA #####

	###### Pour les ratings 

lRatings = projet_modules.obtenirListe(pathToRoot+'Data/ratings.dat')
colRatings = ['UserID','MovieID','Rating','Timestamp']

dfRatings = projet_modules.liste_TO_dataFrame2(lRatings,colRatings)
#print(dfRatings)

	####### Pour les movies

lMovies = projet_modules.obtenirListe(pathToRoot+'Data/movies.dat')
colMovies = ['MovieID','Title','Genres']

dfMovies = projet_modules.liste_TO_dataFrame2(lMovies,colMovies)
#print(dfMovies)

	######## Pour les users

lMovies = projet_modules.obtenirListe(pathToRoot+'Data/users.dat')
colMovies = ['UserID','Gender','Age','Occupation','Zip-code']

dfUser = projet_modules.liste_TO_dataFrame2(lMovies,colMovies)
#print(dfUser)