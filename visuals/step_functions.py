import matplotlib.pyplot as plt
import numpy as np

x = [1, 2, 3, 4, 5, 6, 7] 
y = [1, 1, 5, 6, 6, 9, 11]
y2 = [2, 4, 4, 4, 9, 10, 12]


plt.tick_params(axis='y', which='major', pad=15)

plt.ylabel('$F_j$', rotation='horizontal', labelpad=15)
plt.yticks(visible=False)
plt.xticks([1, 2, 3, 4, 5, 6, 7],
            ['$x_1$', '$x_2$', '$x_3$', '$x_4$', '$x_5$', '$x_6$', '$x_7$'],
            visible=True, rotation='horizontal')
plt.tick_params(
    axis='x',         
    which='both',
    bottom=True,      
    labeltop=False)

plt.step(x, y, label='$F_\mu$', color='blue')
plt.step(x, y2, label='$F_\\nu$', color='red')
plt.legend(loc='upper left')
plt.show()