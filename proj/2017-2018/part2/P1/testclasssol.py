import numpy as np
from sklearn import neighbors, datasets, tree, linear_model
from sklearn.model_selection import cross_val_score
from sklearn.externals import joblib

import matplotlib.pyplot as plt
from matplotlib.colors import ListedColormap
from sklearn.model_selection import learning_curve


import classsol

#load input data
words = []
with open("words.txt") as file:
	for line in file:
		line = line.split(' ') #or some other preprocessing
		words.append(line) #storing everything in memory!

X = words[0]

for test in ["wordsclass.npy", "wordsclass2.npy"]:
	print("Testing " + test)
	#load output data
	Y=np.load(test)

	f = classsol.features(X)

	clf = classsol.mytraining(f,Y)

	Ypred = classsol.myprediction(f, clf)

	pred = np.sum(Y^Ypred)/len(X)
	print(pred)
	if pred<.05:
		print("Erro bastante baixo. PERFECT!\n")
	elif pred<.3:
		print("Erro nos Q dentro dos limites de tolerância. OK\n")
	else:
		print("Erro nos Q acima dos limites de tolerância. FAILED\n")

	# Grabbing plot figures
	plt.figure()
	train_sizes, train_scores_svr, test_scores_svr = \
		learning_curve(clf, f[:100], Y[:100], train_sizes=np.linspace(0.1, 1, 10),
		scoring="accuracy", cv=5)
	plt.plot(train_sizes, test_scores_svr.mean(1), 'o-', color="g", label='SVR')
	print(train_sizes)
	print(test_scores_svr.mean(1))
	plt.legend(loc='best')
	plt.show()
