import numpy as np
import sys
np.set_printoptions(precision=4, suppress=True)

from BN import *

gra = [[],[0],[0],[0],[1,2], [2]]
ev = (1,1,1,1,1,1)

p1 = Node( np.array([.01]), gra[0] )# A

p2 = Node( np.array([.4,.1]), gra[1] )# B

p3 = Node( np.array([.2,.8]), gra[2] )# C
#print( "p3 = ", p3.computeProb(ev))

p4 = Node( np.array([.2,.8]), gra[3] )# D

p5 = Node( np.array([[.6,.9],[.9,.99]]), gra[4] ) # E
#print( "p5 = ", p3.computeProb(ev))

p6 = Node( np.array([.2,.8]), gra[5] )#F


prob = [p1,p2,p3,p4,p5,p6]

bn = BN(gra, prob)

ev = ([],0,1,[],1,1)

print ("Inference : ", bn.inference(ev))
