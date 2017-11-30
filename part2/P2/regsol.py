# 84738 Lucia Lisboa - 77906 Antonio Sarmento - 38

import numpy as np
from sklearn import datasets, tree, linear_model
from sklearn.kernel_ridge import KernelRidge
from sklearn.model_selection import cross_val_score



def mytraining(X, Y):
	# reg = linear_model.Lasso()

	par_kernel = ['laplacian', 'polynomial', 'rbf', 'cosine']


	reg = None

	lowest_idx = 0
	lowest_acc = -1

	for idx,kernel in enumerate(par_kernel):
		reg = KernelRidge(kernel=kernel, alpha = 0.1, gamma = 0.1)
		scores = cross_val_score(reg, X, Y, cv=5,  scoring = 'neg_mean_squared_error')
		accuracy = -scores.mean()
		scores = scores.std()

		if lowest_acc == -1 or accuracy < lowest_acc:
			lowest_acc = accuracy
			lowest_idx = idx

	reg = KernelRidge(kernel = par_kernel[lowest_idx], alpha = 0.1, gamma = 0.1)
	reg.fit(X, Y)
	return reg


def myprediction(X, reg):
	Ypred = reg.predict(X)

	return Ypred
