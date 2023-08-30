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
from scipy.stats import energy_distance


from random import randrange


def main(data, t, max_edge_length, max_dimension, shift, metric):

    data = np.array(data)
    # computes W_1 for two probability measures u and v
    # discretely, we need pairs (t, u(t)) and (t, v(t))
    # will normalize u and v if sum neq 1

    # args are ordered like (u(t), v(t), t, t) where t is the Dirac mass centered
    # at t
    def w1(u, v):   # the distance matrix metric arg. can only take two inputs
        return wasserstein_distance(u, v, t, t)
    
    def e1(u, v):
        return energy_distance(u, v, t, t)


    # if inf(f) is negative, we send f - inf(f) to the new value
    # i.e. shifting everything up by the value of the min
    def vert_shift(f):
        try:
            if min(f) < 0:
                vert_f = [i + abs(min(f)) for i in f]
            return vert_f
        
        except:
            print('f has no negative values')

    # this is not working as expected
    if shift == True:
        dataShifted = []
        for i in range(data.shape[1]):
                # this line may or may not work
                # need to account for the shape of data
            dataShifted.append(np.apply_along_axis(vert_shift, axis=-1, arr=data[i,:]))
    else:
        dataShifted = np.array(data)


    if metric == 'w1' or metric == None:
        ds = sklearn.metrics.pairwise_distances(dataShifted, metric = w1)

    elif metric == 'e1':
        ds = sklearn.metrics.pairwise_distances(dataShifted, metric = e1)


    skeleton = gd.RipsComplex(
        distance_matrix = ds,
        max_edge_length = max_edge_length
    )

    simplex_tree = skeleton.create_simplex_tree(max_dimension = max_dimension)
    return simplex_tree
   


if __name__ == "__main__":
    n = 1000
    # here, the mesh t needs to be previously computed
    t = np.linspace(0, 100, 11)
    # u = [np.random.randint(-20, 20) for i in t]
    # v = [np.random.randint(-20, 20) for i in t]

    test_matrix = []
    for i in range(n):
        test_matrix.append([np.random.randint(-20, 20) for i in t])

    test_matrix = np.array(test_matrix)

    # need to figure out how to find a good edge length/alpha
    simplex_tree = main(test_matrix, t, max_edge_length=3.5, max_dimension=4, shift=None, metric='w1')

    fileObj = open('simplex_tree.obj', 'wb')
    pickle.dump(simplex_tree, fileObj)
    fileObj.close()
    print(simplex_tree.num_simplices())


#TODO
# fix the shift if/else tree
# fix noise on n-sphere demo (lives in ~\RiemannTDA)