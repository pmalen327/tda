import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0, 1, 20)

y1 = [(.8*x**3 - .9*x**2 + .5) for x in x]
y2 = [x**3 - .5*x - 1 for x in x]


plt.rcParams.update({
    "text.usetex": True,
    "font.family": "sans-serif",
    "font.sans-serif": "Helvetica",
})


# need to remove labels from right side
# probs need to change labels, its gross

# plt.yticks([y1[0], y1[3], y1[6], y1[10], y1[-1]],
#             ['$f(x_0)$', '$f(x_1)$', '$f(x_2)$', '$f(x_i)$', '$f(x_n)$'],
#             visible=True, rotation="horizontal")
# plt.xticks([0, x[1], x[2],  1/2, 1],
#             ['$x_0$', '$x_1$', '$x_2$', '$x_i$', '$x_n$'],
#             visible=True, rotation="horizontal")
# plt.tick_params(
#     axis='x',         
#     which='both',
#     bottom=True,      
#     labeltop=False)
# plt.scatter(x, y1, s = 5, color = 'black')

            

# plt.yticks([y2[0], y2[3], y2[6], y2[10], y2[-1]],
#             ['$g(x_0)$', '$g(x_1)$', '$g(x_2)$', '$g(x_i)$', '$g(x_n)$'],
#             visible=True, rotation="horizontal")
# plt.xticks([0, x[1], x[2],  1/2, 1],
#             ['$x_0$', '$x_1$', '$x_2$', '$x_i$', '$x_n$'],
#             visible=True, rotation="horizontal")
# plt.tick_params(
#     axis='x',         
#     which='both',
#     bottom=True,      
#     labeltop=False)
# plt.scatter(x, y2, s = 5, color = 'black')


plt.show()



