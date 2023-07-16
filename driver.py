# Preston Malen
# July 2023

import numpy as np
import pandas as pd
import gudhi as gd
from scipy.stats import wasserstein_distance

from random import randrange
np.random.seed(0)

t = np.linspace(0, 100, 11)
u = [np.random.randint(-20, 20) for i in t]
v = [np.random.randint(0, 20) for i in t]

# computes W_1 for two probability measures u and v
# discretely, we need pairs (t, u(t)) and (t, v(t))
# will normalize u and v if sum neq 1

# args are ordered like (u(t), v(t), t, t) where t is the Dirac mass centered
# at t
w1 = wasserstein_distance(u, v, t, t)

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
                return None # how to throw exception here??
        pos_f = [abs(val) for val in f]
        return pos_f
    except:
        print('f has no negative values')


#TODO
# figure out line 49, small technicality
# wrap in a main method maybe?? not sure 
    




    















