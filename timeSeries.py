import pickle
import mpu
import numpy as np
import pandas as pd
import gudhi as gd
import sklearn

from sklearn.preprocessing import normalize
from sklearn.metrics import pairwise_distances
from scipy.stats import wasserstein_distance

from driver import main


df = pd.read_csv('stocks.csv')
df = df.drop('Date', axis=1)
df = df.drop('Volume', axis=1)
data = pd.DataFrame(df).to_numpy()

# I have something backwards, I think I know but will need to sketch it out
if __name__ == '__main__':
    t = [i+1 for i in range(data.shape[1])]
    simplex_tree = main(data, t, max_edge_length=3, max_dimension=4, regularization='none')
    print(simplex_tree.num_simplices())

    fileObj = open('timeSeries_simplex_tree.obj', 'wb')
    pickle.dump(simplex_tree, fileObj)
    fileObj.close()
