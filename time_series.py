import numpy as np
import pandas as pd
import gudhi as gd
import glob
import matplotlib.pyplot as plt
import pickle
import springpy as sp


from scipy.stats import wasserstein_distance
from sklearn.preprocessing import normalize
from driver import main

# files = glob.glob("data/*.csv")

# # n = 1500
# data = []
# for f in files:
#     df = pd.read_csv(f)
#     df = df['high']
#     # this line is the problem child, only want to get one datapoint per day
#     df = df.to_numpy()
#     df = df[:144000:1440]
#     data.append(df)

# print(len(data))

# # data = np.array(data)
# for item in data:
#     if len(item) != 100:
#         data.remove(item)

# print(len(data))

# data = np.array(data)

# fileObj = open('time_series_df.obj', 'wb')
# pickle.dump(data, fileObj)
# fileObj.close()

# mesh spacing up to n days
t = np.linspace(0, 100, 100)

fileObj = open('time_series_df.obj', 'rb')
data = pickle.load(fileObj)
fileObj.close()

simplex_tree, ds = main(data, t, max_edge_length=100, max_dimension=1)
simplex_tree.expansion(3)
simplex_tree.compute_persistence()
print(simplex_tree.upper_bound_dimension())
print(simplex_tree.num_simplices())
print(simplex_tree.betti_numbers())



# Tune Wasserstein Distance
# Return and check distance matrix
# Plot distance matrix
# Interpret 1-dimensional homology


# gd.plot_persistence_barcode(simplex_tree.persistence())
# plt.show()

# sp.h = 1000
# sp.w = 1000
# sp.graph(ds)


fileObj = open('time_series_tree.obj', 'wb')
pickle.dump(simplex_tree, fileObj)
fileObj.close()