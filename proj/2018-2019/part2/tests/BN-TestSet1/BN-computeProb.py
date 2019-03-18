import numpy as np
np.set_printoptions(precision=4, suppress=True)

from BN import *

ev = (1,1,1,1,1)

p1 = Node( np.array([.001]), [] ) # burglary
print(p1.computeProb(ev))
[0.999, 0.001]

p3 = Node( np.array([[.001,.29],[.94,.95]]), [0,1] ) # alarm
print(p3.computeProb(ev))

ev = (0,0,1,1,1)
print(p3.computeProb(ev))
print("=", [0.999, 0.001], "\n")

ev = (0,1,1,1,1)
print(p3.computeProb(ev))
print("=", [0.71, 0.29], "\n")

ev = (1,0,1,1,1)
print(p3.computeProb(ev))
print("=", [0.06, 0.94], "\n")

ev = (1,1,1,1,1)
print(p3.computeProb(ev))
print("=", [0.05, 0.95], "\n")
