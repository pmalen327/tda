import pickle
import mpu
import numpy as np
import pandas as pd
import gudhi as gd
import matplotlib.pyplot as plt

def main(minDim, maxDim):
    fileObj = open('timeSeries_simplex_tree.obj', 'rb')
    simplex_tree = pickle.load(fileObj)
    fileObj.close()

    simplex_tree.compute_persistence()
    
    dims = []
    for i in range(minDim, maxDim + 1):
        dims.append(simplex_tree.persistence_intervals_in_dimension(i))


    colors = ['red', 'blue', 'green', 'yellow', 'orange', 'black']
    fig, ax = plt.subplots(figsize = (7, 7))
    counter = 1
    for i in range(len(dims)):
        color = colors[i]
        for bc in dims[i]:
            ax.plot(bc, [counter, counter], color=color)
        counter += 1

    ax.set_ylabel("index of feature")
    ax.set_xlabel("filtration value")
    ax.set_title("barcode plot")
    plt.show()
    return dims


if __name__ == "__main__":
    main(1, 4)