# Preston Malen
# July 2023

import pickle
import mpu
import numpy as np
import pandas as pd
import gudhi as gd
import sklearn

from sklearn.metrics import pairwise_distances
from scipy.stats import wasserstein_distance


def main(data, t, max_edge_length, max_dimension):

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
# FIX DIS - the indexing is fucked or something
    def vert_shift(f):
        if min(f) < 0:
            vert_f = [i + abs(min(f)) for i in f]
        return vert_f

    dataShifted = []
    for i in range(data.shape[0]):
        dataShifted.append(vert_shift(data[i,:]))

    dataShifted = np.array(dataShifted)

    ds = sklearn.metrics.pairwise_distances(dataShifted, metric = w1)

    skeleton = gd.RipsComplex(
        distance_matrix = ds,
        max_edge_length = max_edge_length
    )

    simplex_tree = skeleton.create_simplex_tree(max_dimension = max_dimension)
    return simplex_tree
   


if __name__ == "__main__":
    n = 1000
    t = np.linspace(0, 100, 11)

    test_matrix = []
    for i in range(n):
        test_matrix.append([np.random.randint(-20, 20) for i in t])

    test_matrix = np.array(test_matrix)

    # need to figure out how to find a good edge length/alpha
    simplex_tree = main(test_matrix, t, max_edge_length=3, max_dimension=4)

    fileObj = open('simplex_tree.obj', 'wb')
    pickle.dump(simplex_tree, fileObj)
    fileObj.close()
    print(simplex_tree.num_simplices())


#TODO
# fix noise on n-sphere demo (lives in ~\RiemannTDA)