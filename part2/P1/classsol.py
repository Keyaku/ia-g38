# 84738 Lucia Lisboa - 77906 Antonio Sarmento - 38

import numpy as np
from sklearn import neighbors, datasets, tree, linear_model

from sklearn.externals import joblib
import timeit

from sklearn.model_selection import cross_val_score

import re

def count_vowels(word):
	vowels = "aáàâãeéèêiíîoóõuú"
	count = 0
	for c in vowels:
		count += word.count(c)
	return count

def count_consonants(word):
	count = len(word) - count_vowels(word)
	return count

def count_accent_symbols(word):
	count = len(re.findall('^[a-zA-Z_]+$', word))
	return count

def count_repeated_characters(word):
	counted = []
	count = 0
	for c in word:
		if c not in counted:
			counted += [c]
	return len(counted)

def features(X):

	F = np.zeros((len(X),5))
	for x in range(0,len(X)):
		F[x,0] = len(X[x]) # length of the word
		F[x,1] = count_vowels(X[x])     # number of vowels
		F[x,2] = count_consonants(X[x]) # number of consonants
		F[x,3] = count_accent_symbols(X[x]) # number of accented characters
		F[x,4] = count_repeated_characters(X[x]) # number of repeated characters

	return F

def mytraining(f,Y):
	clf = neighbors.KNeighborsClassifier() # TODO: use mytrainingaux()
	clf = clf.fit(f, Y)
	return clf


def mytrainingaux(f,Y,par):
	# TODO: use different sklearn algorithms (neighbors, datasets, tree, linear_model)
	# neighbors.KNeighborsClassifier(n_neighbors, weights=weights)
	# datasets.????
	# tree.DecisionTreeClassifier(min_samples_split=min_samples_split)
	# linear_model.RidgeClassifier(alpha)
	return clf

def myprediction(f, reg):
	Ypred = reg.predict(f)
	return Ypred
