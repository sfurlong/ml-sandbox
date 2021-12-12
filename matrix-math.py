import numpy as np


A = [[1,2,1],
        [4 ,4,5],
        [6 ,7,7]]

B = [[-7,-7,6],
        [2,1,-1],
        [4,5,-4]]

print (A)

print (B)

print (np.dot(A,B))
print (np.dot(B,A))

np.set_printoptions(suppress_small=True)
np.transpose(A)