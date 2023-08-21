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

    dims = []
    
    for x in pHomology:
        for i in range(minDim, maxDim):
            if x[0] == i:
                if x[1][1] < np.inf:
                    dims.append(x)

    dims = np.array(dims)
    return dims

if __name__ == "__main__":
    temp = main(1, 4)
    print(temp)
# fuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuu