# 84738 Lucia Lisboa - 77906 Antonio Sarmento - 38

# -*- coding: utf-8 -*-
"""
Created on Mon Oct 16 20:31:54 2017

@author: mlopes
"""
import numpy as np

# Para calcular a trajetoria e' necessario uma politica

def Q2pol(Q, eta=5):
	# TODO
	return pol

# Action Selection Policies

# As mentioned above, there are three common policies used for action selection.
#  The aim of these policies is to balance the trade-off between exploitation and exploration,
#  by not always exploiting what has been learnt so far.
# -greedy - most of the time the action with the highest estimated reward is chosen, called the greediest action.
#  Every once in a while, say with a small probability , an action is selected at random. The action is selected uniformly,
#  independant of the action-value estimates. This method ensures that if enough trials are done,
#  each action will be tried an infinite number of times, thus ensuring optimal actions are discovered.
# -soft - very similar to  -greedy. The best action is selected with probability 1 - and the rest of the time a random action
#  is chosen uniformly.
# -softmax - one drawback of -greedy and -soft is that they select random actions uniformly.
#  The worst possible action is just as likely to be selected as the second best.
#  Softmax remedies this by assigning a rank or weight to each of the actions, according to their action-value estimate.
#  A random action is selected with regards to the weight associated with each action,
#  meaning the worst actions are unlikely to be chosen. This is a good approach to take where the worst actions are very unfavourable.


# Para isso implementar o algoritmo Q-learning que a partir de uma trajetoria
# recebida calcule os valores Q para cada
# gamma = discount factor 0 < gamma < 1
# alpha = learning rate   0 < alpha < 1
class myRL:

	def __init__(self, nS, nA, gamma):
		self.nS = nS  # numero de linhas - numero de estados
		self.nA = nA  # numero de colunas - numero de accoes
		self.gamma = gamma
		self.Q = np.zeros((nS,nA))

	# Calcular os valores de Q para cada accao
	# Trace e' uma matriz
	def traces2Q(self, trace):
		self.Q = np.zeros((self.nS, self.nA))
		tempQ  = np.zeros((self.nS, self.nA))

		alpha = 1
		#Vai convergir para um numero
		while True:
			for ele in trace:
				state  = int(ele[0])
				action = int(ele[1])
				next_state = int(ele[2])
				reward = ele[3]
				tempQ[state, action] = tempQ[state, action] + alpha * (reward + self.gamma * max(tempQ[next_state, :]) - tempQ[state, action])

			err = np.linalg.norm(self.Q-tempQ)
			self.Q = np.copy(tempQ)
			if err<1e-2:
				break

		return self.Q