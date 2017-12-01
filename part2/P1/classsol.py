# 84738 Lucia Lisboa - 77906 Antonio Sarmento - 38

import numpy as np
from sklearn import neighbors, datasets, tree, linear_model

from sklearn.externals import joblib
import timeit

from sklearn.model_selection import cross_val_score

import unicodedata


# Auxiliary content
vowels = "aeiouy"
def normalize(word):
	return str(unicodedata.normalize('NFKD', word).encode('ascii', 'ignore'), 'utf-8').strip('\n')


# Features
def count_characters(word):
	return len(normalize(word))


def count_vowels(word):
	nword = normalize(word)
	count = len([c for c in nword if c in vowels])

	return count


def count_character_occurrences(word):
	counted = []
	nword = normalize(word)

	for c in nword:
		if c not in counted and nword.count(c) > 1:
			counted += [c]

	return len(counted)


def sum_characters(word):
	nword = normalize(word)
	count = 0

	for c in nword:
		count += ord(c) - ord('a')

	return count


def features(X):
	feature_array = [
		count_characters,
		count_vowels,
		count_character_occurrences,
		sum_characters,
	]

	F = np.zeros((len(X),len(feature_array)))

	for x in range(len(X)):
		for i in range(len(feature_array)):
			feature = feature_array[i]
			F[x,i] = feature(X[x])

	return F


# Training functions
def mytraining(f,Y):
	clf = tree.DecisionTreeClassifier(min_samples_split=8, criterion='entropy', splitter='best')
	#clf = neighbors.KNeighborsClassifier(n_neighbors = 2, weights='distance')
	#clf = neighbors.KNeighborsClassifier(n_neighbors = 2, weights='uniform')
	#clf = neighbors.KNeighborsClassifier(n_neighbors = 3, weights='distance')
	#clf = neighbors.KNeighborsClassifier(n_neighbors = 3, weights='uniform')
	#clf = linear_model.RidgeClassifier(alpha = 0.1)
	clf = clf.fit(f, Y)
	return clf


# Prediction function
def myprediction(f, clf):
	Ypred = clf.predict(f)
	return Ypred
