# 84738 Lucia Lisboa # 77906 Antonio Sarmento # Grupo 38

import numpy as np

import unicodedata


#########################
### Auxiliary content ###
#########################

# String normalization: transforms a Unicode string's characters to their closest ASCII counterparts
def normalize(string):
	return str(unicodedata.normalize('NFKD', string).encode('ascii', 'ignore'), 'utf-8')


# --------------------------------------------------------------------------------------------------------
# Removes artifacts from a string. In this case, only removes linefeed
def remove_artifacts(string):
	return string.strip('\n')


################
### Features ###
################

# Returns the length of a word.
def count_characters(word):
	return len(word)


# --------------------------------------------------------------------------------------------------------
# Returns the number of vowels in a (normalized) word.
def count_vowels(word):
	vowels = "aeiou"
	nword = normalize(word)
	count = len([c for c in nword if c in vowels])

	return count


# --------------------------------------------------------------------------------------------------------
# Returns the number of repeated characters in a word.
def count_repeated_characters(word):
	counted = []

	for c in word:
		if c not in counted and word.count(c) > 1:
			counted += [c]

	return len(counted)


# -------------------------------------------------------------------------------------------------------
# Returns the sum of all characters, where a = 0, b = 1, ..., z = 25
def sum_characters(word):
	count = 0

	for c in word:
		count += ord(c) - ord('a')

	return count


# -------------------------------------------------------------------------------------------------------
# Returns the "weight" of a word, meaning: it'll sum all the characters according to their index
# in that word.
def order(word):
	count = 0

	for i, c in enumerate(word):
		count += (ord(c) - ord('a')) * i

	return count


# -------------------------------------------------------------------------------------------------------
# Assembles all our features and executes them on each word given via the list X.
def features(X):
	feature_array = [
		count_characters,
		count_vowels,
		count_repeated_characters,
		sum_characters,
		order
	]

	F = np.zeros((len(X), len(feature_array)))

	for x in range(len(X)):
		word = remove_artifacts(X[x]).lower()

		for i in range(len(feature_array)):
			feature = feature_array[i]
			F[x, i] = feature(word)

	return F


##########################
### Training functions ###
##########################
import warnings
warnings.filterwarnings("ignore")

from sklearn import tree
from sklearn.model_selection import GridSearchCV
from sklearn import linear_model
from sklearn import neighbors

# Uses the appropriate Classifier method to process words.
def mytraining(f, Y):
	'''
	These are our DecisionTreeClassifier parameters as it stands:
		criterion='entropy',
		splitter='best',
		min_samples_split=2,
		min_samples_leaf=1,
		min_weight_fraction_leaf=0.0,
		min_impurity_decrease=0.0,
		presort=False,
	'''

	# Let's use Cross-Validation, shall we?

	'''
	# RidgeClassifier
	clf = linear_model.RidgeClassifier()
	precision = [1.0, 0.8, 0.6, 0.4, 0.2, 0.1]
	tuned_parameters = [
		{'alpha' : precision},
	]
	'''

	# DecisionTreeClassifier
	clf = tree.DecisionTreeClassifier()
	split = [2, 3, 4, 5, 6, 7, 8]
	tuned_parameters = [
		{'criterion' : ['gini', 'entropy'], 'min_samples_split' : split},
	]

	'''
	# KNeighborsClassifier
	clf = neighbors.KNeighborsClassifier()
	num_neighbors = [5]
	weights = ['uniform']
	tuned_parameters = [
		{'n_neighbors' : num_neighbors, 'weights':weights}
	]
	'''

	# Aplicacao da validacao cruzada
	cv = GridSearchCV(clf, tuned_parameters, cv = 5, scoring ='neg_mean_squared_error')
	cv.fit(f, Y)

	# Buscar o melhor estimador para a nossa regressao
	clf = cv.best_estimator_

	return clf


# -------------------------------------------------------------------------------------------------
# Simply calls the prediction logic from our training method.
def myprediction(f, clf):
	Ypred = clf.predict(f)
	return Ypred
