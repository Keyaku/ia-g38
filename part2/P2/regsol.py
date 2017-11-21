# 84738 Lucia Lisboa - 77906 Antonio Sarmento - 38

import numpy as np
from sklearn import datasets, tree, linear_model
from sklearn.kernel_ridge import KernelRidge
from sklearn.model_selection import cross_val_score
import timeit

def mytraining(X,Y):
	# TODO
	return reg

def mytrainingaux(X,Y,par):
	reg.fit(X,Y)
	# TODO

	return reg

def myprediction(X,reg):
	Ypred = reg.predict(X)
	# TODO

	return Ypred
