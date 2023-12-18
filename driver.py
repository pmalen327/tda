import pickle
import mpu
import numpy as np
import pandas as pd
import gudhi as gd
import sklearn
import springpy as sp
from visuals.plots import plot_barcode
import matplotlib.pyplot as plt

from sklearn.metrics import pairwise_distances
from scipy.stats import wasserstein_distance

def main(data, t, max_edge_length, min_dimension, max_dimension):
    

    def compute_tree(data, t, max_edge_length, max_dimension):

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
            if min(f) < 0:
                vert_f = [i + abs(min(f)) for i in f]
            else:
                return f
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
        simplex_tree.expansion(max_dimension + 1)
        return simplex_tree, ds
    

    def plot_barcode(min_dimension, max_dimension):
        
        simplex_tree, ds = compute_tree(data=data, t=t, max_edge_length=max_edge_length, max_dimension=max_dimension)

        simplex_tree.compute_persistence()
        
        dims = []
        for i in range(min_dimension, max_dimension + 1):
            dims.append(simplex_tree.persistence_intervals_in_dimension(i))


        colors = ['red', 'blue', 'green', 'yellow', 'orange', 'black']
        fig, ax = plt.subplots(figsize = (7, 7))
        counter = 1
        for i in range(len(dims)):
            color = colors[i]
            for bc in dims[i]:
                ax.plot(bc, [counter, counter], linewidth=3, color=color)
                counter += 1

        ax.set_ylabel("index of feature")
        ax.set_xlabel("filtration value")
        ax.set_title("persistence barcode")
        return fig, ax
    
    fig, ax = plot_barcode(min_dimension, max_dimension)
    return fig, ax


# for this example, the data was sampled at 1000 nodes
t = np.linspace(0, 1000, 1000)
min_dimension = 0
max_dimension = 3
max_edge_length = 10

data = 'DATA_MATRIX'
fig, ax = main(data, t, max_edge_length, min_dimension, max_dimension)
plt.show()
