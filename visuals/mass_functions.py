import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0, 1, 20)

y1 = [(.8*x**3 - .9*x**2 + .5) for x in x]
y2 = [(.7*x**3 - .5*x**2 + .3) for x in x]

plt.rcParams.update({
    "text.usetex": True,
    "font.family": "sans-serif",
    "font.sans-serif": "Helvetica"
})

plt.ylabel('$f_{\mu,\\nu}$', rotation='horizontal', labelpad=25)
plt.yticks(visible=False)

plt.xticks([0, x[1], x[2],  1/2, 1],
            ['$x_0$', '$x_1$', '$x_2$', '$x_i$', '$x_n$'],
            visible=True, rotation='horizontal')

plt.tick_params(
    axis='x',         
    which='both',
    bottom=True,      
    labeltop=False)

plt.scatter(x, y1, s=5, label='$f_\mu$', color='red')
plt.scatter(x, y2, s=5, label='$f_\\nu$', color='blue')
plt.legend(loc='upper center')
plt.show()