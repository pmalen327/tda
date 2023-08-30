import numpy as np
import pandas as pd
import gudhi as gd
import matplotlib.pyplot as plt

from scipy.stats import wasserstein_distance
from scipy.stats import energy_distance


df = pd.read_csv('stocks.csv')
df = df.drop(['Date', 'Volume', 'Open', 'Close'], axis=1)
data = pd.DataFrame(df).to_numpy()
t = [i+1 for i in range(data.shape[0])]


h = np.array(df['High'])
l = np.array(df['Low'])
L1 = np.array([abs(h[i]-l[i]) for i in range(len(t))])
W1 = np.array([wasserstein_distance(h[:i], l[:i]) for i in range(1, len(t))])
E1 = np.array([energy_distance(h[:i], l[:i]) for i in range(1, len(t))])


fig, ax = plt.subplots(2, 2, figsize=(10, 7))

ax[0, 0].plot(t, h, linewidth=.3)
ax[0, 0].plot(t, l, linewidth=.3)
ax[0, 0].set_ylabel('Stock Price')
ax[0, 0].legend(['High', 'Low'])
ax[0, 0].title.set_text('Microsoft Stock Prices 4/1/2015 - 3/31/21')

ax[0, 1].plot(t, L1, linewidth=.3, color='green')
ax[0, 1].set_ylabel('L1 Norm')
ax[0, 1].title.set_text('Pointwise L1 Norm Between High and Low')

ax[1, 1].plot(t[1:], W1, linewidth=.3, color='red')
ax[1, 1].set_ylabel('Wasserstein Distance')
ax[1, 1].title.set_text('Rolling Wasserstein Distance')

ax[1, 0].plot(t[1:], E1, linewidth=.5, color='purple')
ax[1, 0].set_ylabel('Energy Distance')
ax[1, 0].title.set_text('Rolling Energy Distance')

plt.show()