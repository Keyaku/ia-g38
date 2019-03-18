import numpy as np
from sklearn import datasets, tree, linear_model
from sklearn.kernel_ridge import KernelRidge
from sklearn.model_selection import cross_val_score
from sklearn.externals import joblib
import timeit
import matplotlib.pyplot as plt
from matplotlib.colors import ListedColormap
from sklearn.model_selection import learning_curve

import regsol

tres = [.3, 800]
for ii,test in enumerate(["regress.npy","regress2.npy"]):
	print("Testing " + test)

	X,Y,Xp,Yp = np.load(test)

	reg = regsol.mytraining(X,Y)

	Ypred = regsol.myprediction(Xp,reg)

	if -cross_val_score( reg, X, Y, cv = 5, scoring = 'neg_mean_squared_error').mean() < tres[ii]:
		print("Erro dentro dos limites de tolerância. OK\n")
	else:
		print("Erro acima dos limites de tolerância. FAILED\n")
	plt.figure()
	train_sizes, train_scores_svr, test_scores_svr = \
		learning_curve(reg, X[:100], Y[:100], train_sizes=np.linspace(0.1, 1, 10),
		scoring="neg_mean_squared_error", cv=10)
	plt.plot(train_sizes, -test_scores_svr.mean(1), 'o-', color="g", label='SVR')
	print(train_sizes)
	print(-test_scores_svr.mean(1))
	plt.xlabel("Train size")
	plt.ylabel("Mean Squared Error")
	plt.title('Learning curves')
	plt.legend(loc='best')
	#plt.plot(Xp,Yp,'g.',label='datatesting')
	#plt.plot(X,Y,'k+',label='datatrain')
	#plt.plot(Xp,Ypred,'m',label='KRR', color = 'r')
	#plt.legend( loc = 1 )
	plt.savefig('hm' + str(ii) + '.svg', transparent = True)
	plt.show()


