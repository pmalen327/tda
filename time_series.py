import numpy as np
import pandas as pd
import gudhi as gd
import glob
import matplotlib.pyplot as plt
import pickle

from scipy.stats import wasserstein_distance
from sklearn.preprocessing import normalize
from driver import main

files = glob.glob("data/*.csv")

n = 1500
data = []
for f in files:
    df = pd.read_csv(f)
    df = df['High']
    df = df.iloc[:n]
    data.append(df.to_numpy())

data = np.array(data)
data = normalize(data, axis=1, norm='l1')

# mesh spacing up to n days
t = np.linspace(0, n, n)


simplex_tree = main(data, t, max_edge_length=10, max_dimension=4)
simplex_tree.expansion(5)
simplex_tree.compute_persistence()
print(simplex_tree.upper_bound_dimension())


# gd.plot_persistence_barcode(simplex_tree.persistence())
# plt.show()

fileObj = open('time_series_tree.obj', 'wb')
pickle.dump(simplex_tree, fileObj)
fileObj.close()
print(simplex_tree.num_simplices())