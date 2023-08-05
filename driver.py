# Preston Malen
# July 2023

import numpy as np
import pandas as pd
import gudhi as gd
import sklearn
from sklearn.preprocessing import normalize
from sklearn.metrics import pairwise_distances
from scipy.stats import wasserstein_distance

from random import randrange
np.random.seed(0)

n = 100
# here, the mesh t needs to be previously computed
t = np.linspace(0, 100, 11)
u = [np.random.randint(-20, 20) for i in t]
v = [np.random.randint(-20, 20) for i in t]


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


# takes the L1 norm of every value in f
# man this is cursed, will definitely need to be optimized later
def pos_shift(f):
    try:
        for i in f:
            if i < 0:
                break
            else: 
                raise Exception('f has no negative values')
            
        pos_f = [abs(val) for val in f]
        return pos_f
    
    except:
        print('f has no negative values')


test_matrix = []
for i in range(n):
    test_matrix.append([np.random.randint(-20, 20) for i in t])

test_matrix = np.array(test_matrix)
    
ds = sklearn.metrics.pairwise_distances(test_matrix, metric = w1)

# will normalizing affect the w1 distance??
skeleton = gd.RipsComplex(
    distance_matrix = ds,
    max_edge_length = 8
)

simplex_tree = skeleton.create_simplex_tree(max_dimension = 5)
print(simplex_tree.num_simplices())


