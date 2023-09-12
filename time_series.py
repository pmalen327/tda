import numpy as np
import pandas as pd
import gudhi as gd
import glob
import matplotlib.pyplot as plt

from scipy.stats import wasserstein_distance
from driver import main



files = glob.glob("data/*.csv")

n = 10
data = []
for f in files:
    df = pd.read_csv(f)
    df = df['High']
    df = df.iloc[:n]
    df = df.to_numpy()
    data.append(df)

# why tf no go numpy array
print(data)