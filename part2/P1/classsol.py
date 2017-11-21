# 84738 Lucia Lisboa - 77906 Antonio Sarmento - 38

import numpy as np
from sklearn import neighbors, datasets, tree, linear_model

from sklearn.externals import joblib
import timeit

from sklearn.model_selection import cross_val_score

def features(X):

	F = np.zeros((len(X),5))
	for x in range(0,len(X)):
		F[x,0] = len(X[x]) # length of the word
		F[x,1] = # TODO
		F[x,2] = # TODO
		F[x,3] = # TODO
		F[x,4] = # TODO

	return F

def mytraining(f,Y):
	# TODO
	return clf

def mytrainingaux(f,Y,par):
	# TODO
	return clf

def myprediction(f, reg):
	Ypred = reg.predict(f)
	# TODO

	return Ypred
