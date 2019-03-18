# Grupo T005 - 77906 António Sarmento - 83391 Andreia Valente
# -*- coding: utf-8 -*-
"""
Created on Mon Oct 16 20:31:54 2017

@author: mlopes
"""

from functools import wraps; import inspect
def autoassign(func):
    names, varargs, keywords, defaults = inspect.getargspec(func)
    @wraps(func)
    def wrapper(self, *args, **kargs):
        for name, arg in list(zip(names[1:], args)) + list(kargs.items()): setattr(self, name, arg)
        for name, default in zip(reversed(names), reversed(defaults)):
            if not hasattr(self, name): setattr(self, name, default)
        func(self, *args, **kargs)
    return wrapper

import numpy as np
import random

from tempfile import TemporaryFile
outfile = TemporaryFile()

class finiteMDP:

	@autoassign
	def __init__(self, nS, nA, gamma, P=[], R=[], absorv=[]):
		'''attributes:
		- nS     : number of States
		- nA     : number of Actions
		- gamma  : discount factor; 0 < gamma < 1
		- P      : structure containing the probabilities of successful actions
		- R      : structure containing the rewards of each action
		- absorv : structure containing states which have 0 rewards
		'''
		self.Q = np.zeros((self.nS,self.nA))


	def runPolicy(self, n, x0,  poltype = 'greedy', polpar=[]):
		#nao alterar
		traj = np.zeros((n,4))
		x = x0
		J = 0
		for ii in range(n):
			a = self.policy(x,poltype,polpar)
			r = self.R[x,a]
			y = np.nonzero(np.random.multinomial( 1, self.P[x,a,:]))[0][0]
			traj[ii,:] = np.array([x, a, y, r])
			J = J + r * self.gamma**ii
			if self.absorv[x]:
				y = x0
			x = y

		return J,traj


	def VI(self):
		#nao alterar
		nQ = np.zeros((self.nS,self.nA))
		while True:
			self.V = np.max(self.Q,axis=1)
			for a in range(self.nA):
				nQ[:,a] = self.R[:,a] + self.gamma * np.dot(self.P[:,a,:],self.V)
			err = np.linalg.norm(self.Q-nQ)
			self.Q = np.copy(nQ)
			if err<1e-7:
				break

		#update policy
		self.V = np.max(self.Q,axis=1)
		#correct for 2 equal actions
		self.Pol = np.argmax(self.Q, axis=1)

		return self.Q, self.Q2pol(self.Q)


	def traces2Q(self, trace):
		'''Trace is a matrix (n x 4)
		Each line = [initial_state, action, final_state, reward]
		'''
		self.Q = np.zeros((self.nS, self.nA))
		tempQ  = np.zeros((self.nS, self.nA))

		# alpha = learning rate; 0 < alpha < 1
		alpha = 0.1

		# Vai convergir para um numero
		while True:
			for elem in trace:
				state = int(elem[0])
				action = int(elem[1])
				next_state = int(elem[2])
				reward = elem[3]

				tempQ[state, action] += alpha * (reward + self.gamma * max(tempQ[next_state]) - tempQ[state, action])

			dif = np.linalg.norm(self.Q - tempQ)
			self.Q = np.copy(tempQ)

			if dif < 1e-2:
				break

		return self.Q


	def policy(self, x, poltype = 'exploration', par = []):
		if poltype == 'exploitation':
			'''Greedy, searches for the most rewarding'''
			# Get the array [ State #, Action #] from given par array with the highest probability
			a = np.array([x, *np.unravel_index(par[x].argmax(), par[x].shape)])
			a = a[1] # Get the Action #

		elif poltype == 'exploration':
			'''Random action'''
			a = self.P[x, self.P[x] > 0] # Grab only successful probabilities
			a = list(enumerate(a)) # enumerate this list to get indices
			a = random.choice([i[0] for i in a if 0 <= i[0] < self.nA]) # grab a random 0 <= index < nA

		return a

	def Q2pol(self, Q, eta=5):
		return np.exp(eta*Q)/np.dot(np.exp(eta*Q),np.array([[1,1],[1,1]]))
