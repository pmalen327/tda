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
    data.append(df.to_numpy())

for i in range(len(data)):
    if len(data[i]) != n: # the fuck is this out of range lol
        data.pop(i)

data = np.array(data)