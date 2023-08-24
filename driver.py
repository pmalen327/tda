# Preston Malen
# July 2023

import pickle
import mpu
import numpy as np
import pandas as pd
import gudhi as gd
import sklearn

from sklearn.preprocessing import normalize
from sklearn.metrics import pairwise_distances
from scipy.stats import wasserstein_distance

from random import randrange


def main(data, max_edge_length, max_dimension, regularization):

    data = np.array(data)

    # computes W_1 for two probability measures u and v
    # discretely, we need pairs (t, u(t)) and (t, v(t))
    # will normalize u and v if sum neq 1

    # args are ordered like (u(t), v(t), t, t) where t is the Dirac mass centered
    # at t
    def w1(u, v):   # the distance matrix metric arg. can only take two inputs
        return wasserstein_distance(u, v, t, t)


    # if inf(f) is negative, we send f - inf(f) to the new value
    # i.e. shifting everything up by the value of the min
    def vert_shift(f):
        try:
            if min(f) < 0:
                vert_f = [i + abs(min(f)) for i in f]
            return vert_f
        
        except:
            print('f has no negative values')


    if regularization == 'shift':
        dataShifted = []
        # FUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUK
        for i in range(data.shape[1]):
            # this line may or may not work
            # need to account for the shape of data
            dataShifted.append(np.apply_along_axis(vert_shift, axis=1, arr=data[i,:]))

    elif regularization == 'positive':
        pass # this is where we will call the other function to fix negative values
    
    elif regularization == 'none':
        dataShifted = data # this is cursed and probs a better way, but that's a 
                           # future Preston problem
    

    dataShifted = np.array(dataShifted)

    ds = sklearn.metrics.pairwise_distances(dataShifted, metric = w1)

    skeleton = gd.RipsComplex(
        distance_matrix = ds,
        max_edge_length = max_edge_length
    )

    simplex_tree = skeleton.create_simplex_tree(max_dimension = max_dimension)
    return simplex_tree
   


if __name__ == "__main__":
    n = 50
    # here, the mesh t needs to be previously computed
    t = np.linspace(0, 100, 11)
    # u = [np.random.randint(-20, 20) for i in t]
    # v = [np.random.randint(-20, 20) for i in t]

    test_matrix = []
    for i in range(n):
        test_matrix.append([np.random.randint(-20, 20) for i in t])

    test_matrix = np.array(test_matrix)
    simplex_tree = main(test_matrix, max_edge_length=8 , max_dimension=5, regularization='shift')

    fileObj = open('simplex_tree.obj', 'wb')
    pickle.dump(simplex_tree, fileObj)
    fileObj.close()
    print(simplex_tree.num_simplices())


#TODO
# ACCOUNT FOR NEGATIVE VALUES IN TIME SERIES >> need to write the other function to
    # check for negative values and adjust accordingly
# fix if/else tree
# fix noise on n-sphere demo (lives in ~\RiemannTDA)
