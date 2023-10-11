# Preston Malen
# June 2023

# Kaggle dataset: https://shorturl.at/pBIU9

# Looking at the homology of a lat/long dataset, nothing interesting is expected,
# this is primarily for practice

import sklearn
import numpy as np
import gudhi as gd
import pandas as pd
import matplotlib.pyplot as plt
from sklearn import metrics
from mpl_toolkits.mplot3d import Axes3D
from sklearn.preprocessing import normalize
from skspatial.objects import Sphere

path = '/Users/stone/Desktop/project files/repos/RiemmanTDA/nSphere Demo/latlong_vals.csv'
df = pd.read_csv(path)
df = df.select_dtypes(include=np.number)

temp = df[['usa_state_latitude', 'usa_state_longitude']]
temp = temp.dropna(axis=0)
temp = temp.rename(columns={'usa_state_latitude':'latitude', 'usa_state_longitude':'longitude'})

df = df.drop(['usa_state_latitude', 'usa_state_longitude'], axis=1)
df = df.dropna(axis=0)
df = pd.concat([df, temp])

data = df.to_numpy()

# data = [lat, long]
# lat = phi
# long = theta
# rho = 1

x = []
for i in data:
    x.append(np.cos(i[0])*np.cos(i[1]))
x = np.array(x)

y = []
for i in data:
    y.append(np.cos(i[0])*np.sin(i[1]))
y = np.array(y)

z = np.array([np.sin([i[0]])] for i in data)


# just need to fix the formatting shitttttt ugh
data = [x, y, z]
# data = normalize(data, axis=1, norm='l1')  --idk if this will even be needed



ds = sklearn.metrics.pairwise.cosine_distances(data, Y = None)
skeleton = gd.RipsComplex(distance_matrix = ds)
simplexTree = skeleton.create_simplex_tree(max_dimension = 2)
diag = simplexTree.persistence()