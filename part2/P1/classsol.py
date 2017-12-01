# 84738 Lucia Lisboa - 77906 Antonio Sarmento - 38

import numpy as np
from sklearn import neighbors, datasets, tree, linear_model

from sklearn.externals import joblib
import timeit

from sklearn.model_selection import cross_val_score

import re
import unicodedata


# Auxiliary functions
def normalize(word):
	return str(unicodedata.normalize('NFKD', word).encode('ascii', 'ignore'), 'utf-8')


# Features
def count_characters(word):
	return len(normalize(word))


def count_vowels(word):
	vowels = "aeiouy"
	nword = normalize(word)
	count = len([c for c in nword if c in vowels])

	return count


def count_accent_symbols(word):
	symbols = re.findall('[^\w]', word, re.A)

	while '\n' in symbols:
		symbols.remove('\n')

	return len(symbols)


def count_character_occurrences(word):
	counted = []
	nword = normalize(word)

	for c in nword:
		if c not in counted and nword.count(c) > 1:
			counted += [c]

	return len(counted)


def count_alpha(word):
	count = len(word)
	digits = re.findall(r'\d+', word)
	if len(digits) > 0:
		count -= len(digits[0])
	return count


def features(X):

	F = np.zeros((len(X),5))
	for x in range(0,len(X)):
		F[x,0] = count_characters(X[x]) # length of the word, lowers by ~0.04 in wordsclass.npy, ~0.01 in wordsclass2.npy
		F[x,1] = count_accent_symbols(X[x]) # accented words, lowers by ~0.032
		F[x,2] = count_vowels(X[x]) # vowels, lowers ~0.002
		F[x,3] = count_character_occurrences(X[x]) # repeated characters, lowers by ~0.015
		F[x,4] = count_alpha(X[x])

	return F


# Training functions
def mytraining(f,Y):
	clf = tree.DecisionTreeClassifier(min_samples_split=8) # TODO: use mytrainingaux()
	clf = clf.fit(f, Y)
	return clf


def mytrainingaux(f,Y,par):
	# TODO: use different sklearn algorithms (neighbors, datasets, tree, linear_model)
	# neighbors.KNeighborsClassifier(n_neighbors, weights=weights)
	# n_neighbors= 2 or 3
	# weights = 'distance'
	# weights = 'uniform'

	# datasets.????

	# tree.DecisionTreeClassifier(min_samples_split=min_samples_split)
	# min_samples_split= 8

	# linear_model.RidgeClassifier(alpha)
	return clf

# Prediction function
def myprediction(f, reg):
	Ypred = reg.predict(f)
	return Ypred
