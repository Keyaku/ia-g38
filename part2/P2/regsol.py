# 84738 Lucia Lisboa # 77906 Antonio Sarmento # Grupo 38

from sklearn.kernel_ridge import KernelRidge
from sklearn.model_selection import GridSearchCV
import time
from sklearn.svm import SVR
import warnings

warnings.filterwarnings("ignore")

def mytraining(X, Y):

	# Declaracao dos parametros
	range = [1.0, 0.8, 0.6, 0.4, 0.2, 0.1]

	tuned_parameters = [
		{'kernel': ['linear']},
		{'kernel': ['rbf'], 'alpha': range, 'gamma': range},
		{'kernel': ['polynomial'], 'alpha': range, 'gamma': range},
		{'kernel': ['cosine']}
	]

	"""tuned_parameters = [
		{'kernel' : ['rbf'], 'gamma' : range, 'C': [1, 10, 100, 1000]}
	]"""

	# Metodos a serem utilizados
	#reg = SVR()
	reg = KernelRidge()

	# Fit do metodo
	reg.fit(X, Y)

	# Aplicacao da validacao cruzada
	clf = GridSearchCV(KernelRidge(), tuned_parameters, cv = 5, scoring ='neg_mean_squared_error')
	#clf = GridSearchCV(SVR(), tuned_parameters, cv=5, scoring='neg_mean_squared_error')
	clf.fit(X, Y)

	# Buscar o melhor estimador para a nossa regressao
	reg = clf.best_estimator_

	return reg

#----------------------------------------------------------------------------------------------------------------------#

def myprediction(X, reg):
	Ypred = reg.predict(X)

	return Ypred

# ----------------------------------------------------------------------------------------------------------------------#
