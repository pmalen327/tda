import pickle
import mpu
import numpy as np
import pandas as pd
import gudhi as gd
import matplotlib.pyplot as plt




def main(minDim, maxDim):
    fileObj = open('simplex_tree.obj', 'rb')
    simplex_tree = pickle.load(fileObj)
    fileObj.close()

    pHomology = simplex_tree.persistence()

    dims = [[] for i in range(minDim, maxDim)] # idk this is cursed, pls fix ffs
    
    for x in pHomology:
        pass

    return 0

# Reference >> want to get all dimensions in range of max/min
    # 0 and 1 homology features probably aren't that interesting

# dim0_bc = []
# dim1_bc = []

# for x in diag:
#   if x[0] == 0:
#     if x[1][1] < np.inf:
#       dim0_bc.append(x[1])
#   else:
#     dim1_bc.append(x[1])

# dim0_bc = np.array(dim0_bc)
# dim1_bc = np.array(dim1_bc)








# print(simplex_tree.num_simplices())