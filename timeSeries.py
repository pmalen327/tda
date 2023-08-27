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
print(data.shape)

# I have something backwards, I think I know but will need to sketch it out
if __name__ == '__main__':
    t = np.linspace(0, data.shape[0])
    simplex_tree = main(data, t, max_edge_length=2, max_dimension=3, regularization='none')
    print(simplex_tree.num_simplices())








