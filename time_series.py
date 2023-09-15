import numpy as np
import pandas as pd
import gudhi as gd
import glob
import matplotlib.pyplot as plt
import pickle

from sklearn.preprocessing import normalize
from scipy.stats import wasserstein_distance
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

print(data.shape)

simplex_tree = main(data, t, max_edge_length=5, max_dimension=5)
fileObj = open('time_series_tree.obj', 'wb')
pickle.dump(simplex_tree, fileObj)
fileObj.close()
print(simplex_tree.num_simplices())