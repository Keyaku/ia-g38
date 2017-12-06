# 84738 Lucia Lisboa - 77906 Antonio Sarmento - 38

import numpy as np
from sklearn import datasets, tree, linear_model
from sklearn.kernel_ridge import KernelRidge
from sklearn.model_selection import GridSearchCV
import time
from sklearn.svm import SVR



def mytraining(X, Y):

	#Declaracao dos parametros
	range = [1.0, 0.8, 0.6, 0.4, 0.2, 0.1]

	"""tuned_parameters = [
		{'kernel': ['linear']},
		{'kernel': ['rbf'], 'alpha' :  range, 'gamma' : range},
		{'kernel' : ['polynomial'], 'alpha' : range, 'gamma' : range},
		{'kernel' : ['cosine']}
	]"""

	tuned_parameters = [
		{'kernel' : ['rbf'], 'gamma' : range, 'C': [1, 10, 100, 1000]}
	]

	if allPositive(X, Y):
		tuned_parameters += [{'kernel' : ['chi2'], 'gamma' : range }]


	Y = Y.ravel()
	reg = SVR()
	#reg = KernelRidge()
	reg.fit(X, Y)


	#clf = GridSearchCV(KernelRidge(), tuned_parameters, cv=5, scoring='neg_mean_squared_error')
	clf = GridSearchCV(SVR(), tuned_parameters, cv=5, scoring='neg_mean_squared_error')

	clf.fit(X, Y)
	reg = clf.best_estimator_

	return reg

#----------------------------------------------------------------------------------------------------------------------#

def myprediction(X, reg):
	Ypred = reg.predict(X)

	return Ypred


#----------------------------------------------------------------------------------------------------------------------#
def allPositive(X, Y):

	return not (any(x <= 0 for x in X) or any(y <= 0 for y in Y))

# ----------------------------------------------------------------------------------------------------------------------#

# Important kernel factors:

	# Chi2
	# Computes the exponential chi-squared kernel X and Y.
	# The chi-squared kernel is computed between each pair of rows in X and Y. X and Y have to be non-negative.
	# This kernel is most commonly applied to histograms.

	# Sigmoid
	# The function sigmoid_kernel computes the sigmoid kernel between two vectors.
	# The sigmoid +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++kernel is also known as hyperbolic tangent, or Multilayer Perceptron
	# (because, in the neural network field, it is often used as neuron activation function).

# Gamma:
# To "raise" the points you use the RBF kernel, gamma controls the shape of the "peaks" where you raise the points.
# A small gamma gives you a pointed bump in the higher dimensions, a large gamma gives you a softer, broader bump.
# So a small gamma will give you low bias and high variance while a large gamma will give you higher bias and low variance.
# The hyperparameter γ controls the tradeoff between error due to bias and variance in your model.
# If you have a very large value of gamma, then even if your two inputs are quite “similar”,
#  the value of the kernel function will be small - meaning that the support vector xnxn does not have much influence
#  on the classification of the training example xmxm. This allows the SVM to capture more of the complexity and shape of the data,
#  but if the value of gamma is too large, then the model can overfit and be prone to low bias/high variance. On the other hand,
#  a small value for gamma implies that the support vector has larger influence on the classification of xmxm.
#  This means that the model is less prone to overfitting, but you may risk not learning a decision boundary that captures
#  the shape and complexity of your data. This leads to a high bias, low variance model.


