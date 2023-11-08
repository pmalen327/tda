# This returns the dataframe indices of features that correspond to the
# dim-dimensional homology groups

from time_series import simplex_tree, ds
import numpy as np
import pandas as pd
import pickle
import itertools
import glob
import os


fileObj = open('time_series_df.obj', 'rb')
df = pickle.load(fileObj)
fileObj.close()

dim = 1

simplex_tree.compute_persistence()
filter = list(itertools.chain(*simplex_tree.persistence_intervals_in_dimension(dim)))
indices = []
for i in range(1,ds.shape[0]-1):
    for j in range(1,i-1):
        if ds[i][j] in filter:
            indices.append((i,j))

indices = list(itertools.chain(*indices))

files = glob.glob("data/*.csv")
symbols = []
for f in files:
    symbols.append(os.path.basename(f'/Users/stone/Desktop/project files/repos/tda/data/{f}',))

# these are the homology features associated with dim
dim_homology = [symbols[i] for i in indices]

# now what tf to do with these
print(dim_homology)