# Grupo T005 - 77906 António Sarmento - 83391 Andreia Valente
# -*- coding: utf-8 -*-
"""
Created on Mon Oct 15 15:51:49 2018

@author: mlopes
"""

class Node():
	def __init__(self, prob, parents = []):
		self.prob = prob
		self.parents = parents
		

	def computeProb(self, evid):
		'''evid : contains list of boolean values that switch the probability
		of each Node in the network. Useful to check parents' status'''

		index = []
		for parent in self.parents:
			index += [evid[parent]]
		if index == []:
			index = [0]
		index = tuple(index)

		prob = self.prob[index]
		return [1-prob, prob] # false, true


class BN():
	def __init__(self, gra, prob):
		self.gra = gra
		self.prob = prob

	def computeJointProb(self, evid):
		jp = 1

		for node_idx in range(len(self.prob)):
			if evid[node_idx] != []:
				node = self.prob[node_idx]
				node_prob = node.computeProb(evid)[evid[node_idx]]
				jp *= node_prob
		return jp

	''' computePostProb (Inference by Enumeration)
		process: given an evid, finds the probability of the variable represented
		by '-1' in evid by adding all the joint probabilities possible for the
		unknown probabilities. 
		output: the value of the inference by enumeration
	'''
	def computePostProb(self, evid):

		result = []
		isolation = self.isolation(evid)
		for index in range(len(evid)):
			if evid[index]==-1:
				new_evid = list(evid).copy()
				new_evid[index] = 0
				result += [self.evaluation_tree(new_evid,isolation,0)]
		result += [self.evaluation_tree(list(evid),isolation,0)]

		return self.convertAlpha(result[0],result[1])



	''' convertAlpha
		input: 	falseP - probability of variable being true
				trueP - probability of variable being false
		process: assuming (falseP+trueP)=1, calculates the trueP's fraction
		output:	trueP's fraction
	'''
	def convertAlpha(self,falseP,trueP):
		return trueP/(falseP+trueP)


	'''	evaluation_tree
		input: initial - index from which recursion will be implemented
		process: the function constructs all the possible evidence tuple of the bottom 
				 of the evaluation tree and adds all the joint probabilities resulting 
				 from those evidence tuples.
		output: float with the result of adding all the joint probabilities.
	'''


	def evaluation_tree(self,evid,isolation,initial):
		if all(elem!=[] for elem in evid):
			return self.computeJointProb(evid)
		else:
			for elem in evid[initial:]:
				if elem == []:
					if evid.index(elem) in isolation:
						if initial == len(evid)-1:
							return self.computeJointProb(evid)
						return self.evaluation_tree(evid,isolation,initial+1)
					evid1 = evid.copy()
					evid1[evid.index(elem)]=1
					evid0 = evid.copy()
					evid0[evid.index(elem)]=0
					return self.evaluation_tree(evid0,isolation,initial+1) + self.evaluation_tree(evid1,isolation,initial+1)
		return 0


	def isolation(self,evid): 
		independentList=[]
		for node in self.prob: #(p1,p2,p3,p4,p5)
			if evid[self.prob.index(node)] == []:
				if all(elem == [] for elem in evid[self.prob.index(node):]):
					independentList += [self.prob.index(node)]
		return independentList