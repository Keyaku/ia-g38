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


# Para isso implementar o algoritmo Q-learning que a partir de uma trajetoria
# recebida calcule os valores Q para cada accao
class myRL:

	def __init__(self, nS, nA, gamma):
		self.nS = nS
		self.nA = nA
		self.gamma = gamma
		self.Q = np.zeros((nS,nA))

	def traces2Q(self, trace):
		# TODO: implementar esta funcao
		self.Q = np.zeros((self.nS, self.nA))

		return self.Q

#J, trajlearn = fmdp.runPolicy(4, 5, Q2pol(Q))