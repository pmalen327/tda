import numpy as np
import pandas as pd
import gudhi as gd
import glob
import matplotlib.pyplot as plt

from scipy.stats import wasserstein_distance
from driver import main


files = glob.glob("data/*.csv")

n = 1000
data = []
for f in files:
    df = pd.read_csv(f)
    df = df['High']
    df = df.iloc[:n]
    data.append(df.to_numpy())

data = np.array(data)

# mesh spacing up to n days
t = np.linspace(0, n, n)
