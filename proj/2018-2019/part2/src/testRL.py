# -*- coding: utf-8 -*-
"""
Created on Thu Oct 11 09:27:16 2018

@author: mlopes
"""

import sys
import numpy as np
import RL

# Unlocks np printing's MAXIMUM POTENTIAL
np.set_printoptions(threshold=np.nan)

# Prints trajectory without duplicates
def traj_rm_dups(traj):
	unique, indices, counts = np.unique(traj, axis=0, return_inverse=True, return_counts=True)
	occur  = np.copy(counts)
	result = np.copy(unique)

	ii = 0
	for idx in indices:
		if occur[idx] != 0:
			occur[idx] -= counts[idx]
			result[ii] = unique[idx]
			ii += 1

	return result

def traj_graph(traj):
	graph = {}

	for elem in traj:
		s = int(elem[0])
		a = int(elem[1])
		n = int(elem[2])
		r = elem[3]

		if s not in graph:
			graph[s]  = [{ "action": a, "next" : n, "reward" : r }]
		else:
			graph[s] += [{ "action": a, "next" : n, "reward" : r }]

	return graph

def traj_print(traj):
	print(" [ s.  a.  n.  r.]")
	print(" -----------------")
	print(traj)

def print_graph(graph):
	print("Graph:")
	print("s\t=  r ; a => n")
	print("----------------------")
	for node in graph:
		print(node, end='')
		for neighbor in graph[node]:
			a = neighbor["action"]
			n = neighbor["next"]
			r = neighbor["reward"]

			print("\t= %2.0f ; %d =>" % (r,a), n)
		print()

# Prints contents of npz file
def print_npz(name, npz_file):
	# padding npz file and its inner files
	separator = "[%s]" % ("-"*(10 + len(name) + 4 + 10))
	centered_files = (len(separator) >> 1) - (len(str(npz_file.files)) >> 1)
	print(">>>>>>>>>> %s.npz <<<<<<<<<<\n" % name, " "*(centered_files), npz_file.files, sep='')
	print(separator)

	# printing contents of npz_file
	for data in npz_file.files:
		print(data, ":")
		if "traj" in data:
			traj = traj_rm_dups(npz_file[data])
			traj_print(traj)
		else:
			print(npz_file[data], "\n")
		print()

	print(separator, "\n")

print("""Variables:
	s : state
	a : action
	n : next state
	r : reward
""")

#-------------------------------------------------------------------------------

print("exercise 1")

## Environment 1
Pl = np.zeros((7,2,7))
Pl[0,0,1]=1
Pl[1,0,2]=1
Pl[2,0,3]=1
Pl[3,0,4]=1
Pl[4,0,5]=1
Pl[5,0,6]=0.9
Pl[5,0,5]=0.1
Pl[6,0,6]=1
Pl[0,1,0]=1
# Pl[1,1,1]=0 # unnecessary
Pl[1,1,0]=1
Pl[2,1,1]=1
Pl[3,1,2]=1
Pl[4,1,3]=1
Pl[5,1,4]=1
Pl[6,1,5]=1

print("Pl : 7x2x7 matrix : Pl[s,a,n] = probability of successful action\n", Pl, "\n")

Rl = np.zeros((7,2))
Rl[[0,6]]=1
print("Rl : 7x2 matrix : Rl[s,a] = reward of action\n", Rl, "\n")

absorv = np.zeros((7,1))
absorv[[0,6]]=1
print("absorv : 7x1 matrix : absorv[s] = state has reward\n", absorv, "\n")

# Creating finiteMDP based on the data above
fmdp = RL.finiteMDP(7,2,0.9,Pl,Rl,absorv)

data = np.load("Q1.npz")
print_npz("Q1", data)

#-------------------------------------------------------------------------------
print("exploration policy:")

J,traj = fmdp.runPolicy(500,3,poltype = "exploration")
print("J :\n", J)
print("""traj : nx4 matrix :
	traj[x,0] = state
	traj[x,1] = action
	traj[x,2] = next state
	traj[x,3] = reward
""")
unique_traj = traj_rm_dups(traj)
graph = traj_graph(unique_traj)
print_graph(graph)

Qr = fmdp.traces2Q(traj)
print("Qr : traces2Q of %s.npz['traj']\n" % "Q1", Qr, "\n")

result = np.sqrt(sum(sum((data['Q1']-Qr)**2)))
print("result < 1:\n", result)

if result < 1:
    print("Aproximação de Q dentro do previsto. OK\n")
else:
    print("Aproximação de Q fora do previsto. FAILED\n")

#-------------------------------------------------------------------------------
print("\nexploitation policy:")

J,traj = fmdp.runPolicy(3,3,poltype = "exploitation", polpar = Qr)
print("J :\n", J)
print("""traj : nx4 matrix :
	traj[x,0] = state
	traj[x,1] = action
	traj[x,2] = next state
	traj[x,3] = reward
""")
unique_traj = traj_rm_dups(traj)
graph = traj_graph(unique_traj)
print_graph(graph)

result = np.sqrt(sum(sum((data['traj2']-traj)**2)))
print("result < 1:\n", result, "\n")
if result < 1:
    print("Trajectória óptima. OK\n")
else:
    print("Trajectória não óptima. FAILED\n")


#===============================================================================
print("\n")

print("exercise 2")

data = np.load("traj.npz")
print_npz("traj", data)

fmdp = RL.finiteMDP(8,4,0.9)

unique_traj = traj_rm_dups(data['traj'])
graph = traj_graph(unique_traj)
print_graph(graph)

q2 = fmdp.traces2Q(data['traj'])
print("q2 : traces2Q of %s.npz['traj']\n" % "traj", q2, "\n")

result = np.sqrt(sum(sum((data['Q']-q2)**2)))
print("result < 1:\n", result)
if result < 1:
    print("Aproximação de Q dentro do previsto. OK\n")
else:
    print("Aproximação de Q fora do previsto. FAILED\n")
