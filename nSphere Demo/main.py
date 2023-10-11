# Preston Malen
# April 2023

# analyzing data on surface of a 3-sphere of unit radius

import sklearn
import numpy as np
import gudhi as gd
import matplotlib.pyplot as plt
from sklearn import metrics
from mpl_toolkits.mplot3d import Axes3D
from skspatial.objects import Sphere

np.random.seed(80085)

# use spherical coordinates with default radius of r=1
# we will want to use a similar shape like in the Wesley.ipynb demo


# Gram-Schmidt via QR
def gs(matrix):
    Q,R = np.linalg.qr(matrix)
    return Q


# takes P1 and P2 then generates the rotation matrix U
def rotation(P1,P2):
    P3 = np.random.rand(3)
    U = np.array([P1,P2,P3]).transpose()
    U = gs(U)
    return U

# Given two points P1 and P2, finds the map that sends P1 --> P2 and applies the
# same map to V. Returns V --> V2.
def mapper(P1, P2, V):
    U = rotation(P1,P2)
    Q1 = np.matmul(U.transpose(),P1)
    Q2 = np.matmul(U.transpose(),P2)
    angle = (np.arcsin(Q1[1])-np.arcsin(Q2[1]))
    QV = np.matmul(U.transpose(),V)
    angleQV = np.arctan2(QV[0], QV[1]) - np.pi/2 # four quad. arctan
    new_angleQV = angleQV + angle

    r_QV = np.linalg.norm(QV[:2])
    rotated_QV = np.zeros(3)
    rotated_QV[:2] = r_QV * np.array([np.cos(new_angleQV), np.sin(new_angleQV)])
    rotated_QV[2] = QV[2]
    V2 = U @ rotated_QV 
    return V2


    # function mapper(P1, P2)
    # Same as above
    # Define Q1, Q2, U here
    # Create subfunction:
    #   def mapper2(V):
            # Here Q1, Q2, U already defined
    # return mapper2


# plotting a circle with fixed phi and varying theta
N = 100
phiFixed = np.pi/9 # this is determines the "radius" for the small circle
phiFixed2 = np.pi/4 # big circle
theta = [np.random.uniform(low=0,high=np.pi*2) for x in range(N)]
theta2 = [np.random.uniform(low=0,high=np.pi*2) for x in range(N)]

low = -.1
high = .1

# Added synthetic noise, there's probably a better a better way to do this
xs = [np.sin(phiFixed + np.random.uniform(low=low,high=high))*np.cos(t) for t in theta]
ys = [np.sin(phiFixed + np.random.uniform(low=low,high=high))*np.sin(t) for t in theta]
zs = [np.cos(phiFixed + np.random.uniform(low=low,high=high)) for t in theta]
d1 = np.array([xs,ys,zs])
d1 = d1.transpose()

x2 = [np.sin(phiFixed2 + np.random.uniform(low=low,high=high))*np.cos(t) for t in theta2]
y2 = [np.sin(phiFixed2 + np.random.uniform(low=low,high=high))*np.sin(t) for t in theta2]
z2 = [np.cos(phiFixed2 + np.random.uniform(low=low,high=high)) for t in theta2]
d2 = np.array([x2,y2,z2])


# need to shift the large circle in a random direction by a geo. The sum of radii is used here
radSum = phiFixed2 + phiFixed - .1

# shifting the center of the large circle
# these points can really be whatever
P1 = [0,0,1]
P2 = [0,np.sin(radSum),np.cos(radSum)] # this direction was chosen for simplicity

bigC = np.array([mapper(P1,P2,d2[:,i]) for i in range(N)])

# Adding some more circles and seeing how TDA tracks the homology
rad3 = np.random.uniform(low=np.pi/11, high=np.pi/4)
# there is 100% a more efficient way to do this but optimization can wait
theta3 = [np.random.uniform(low=0,high=np.pi*2) for x in range(N)]
P3 = np.random.rand(3)
P3 = P3 / np.linalg.norm(P3)

x3 = [np.sin(rad3 + np.random.uniform(low=low,high=high))*np.cos(t) for t in theta3]
y3 = [np.sin(rad3 + np.random.uniform(low=low,high=high))*np.sin(t) for t in theta3]
z3 = [np.cos(rad3 + np.random.uniform(low=low,high=high)) for t in theta3]
d3 = np.array([x3,y3,z3])
circ3 = np.array([mapper(P1,P3,d3[:,i]) for i in range(N)])

rad4 = np.random.uniform(low=np.pi/11, high=np.pi/4)
theta4 = [np.random.uniform(low=0,high=np.pi*2) for x in range(N)]
P4 = np.random.rand(3)
P4 = P4 / np.linalg.norm(P4)

x4 = [np.sin(rad4 + np.random.uniform(low=low,high=high))*np.cos(t) for t in theta4]
y4 = [np.sin(rad4 + np.random.uniform(low=low,high=high))*np.sin(t) for t in theta4]
z4 = [np.cos(rad4 + np.random.uniform(low=low,high=high)) for t in theta4]
d4 = np.array([x4,y4,z4])
circ4 = np.array([mapper(P1,P4,d4[:,i]) for i in range(N)])



data = np.vstack([d1, bigC, circ3, circ4])
ds = sklearn.metrics.pairwise.cosine_distances(data, Y = None)
skeleton = gd.RipsComplex(distance_matrix = ds)
simplexTree = skeleton.create_simplex_tree(max_dimension = 2)
diag = simplexTree.persistence()
# gd.plot_persistence_barcode(diag)
# plt.show()

# barcode and persistence line graphs
dim0_bc = []
dim1_bc = []

for x in diag:
  if x[0] == 0:
    if x[1][1] < np.inf:
      dim0_bc.append(x[1])
  else:
    dim1_bc.append(x[1])

dim0_bc = np.array(dim0_bc)
dim1_bc = np.array(dim1_bc)

#plot the barcode 
fig,ax = plt.subplots(ncols = 2, figsize = (12,5))
counter = 1 #to align the barcodes vertically
for bc in dim0_bc:
  ax[0].plot(bc,[counter,counter],c="r")
  counter +=1
for bc in dim1_bc:
  ax[0].plot(bc,[counter,counter],c="b")
  counter +=1
ax[0].set_ylabel("index of feature")
ax[0].set_xlabel("filtration value")
ax[0].set_title("Persistence barcode")

#plot the diagram
ax[1].scatter(dim0_bc[:,0],dim0_bc[:,1],c="r")
ax[1].scatter(dim1_bc[:,0],dim1_bc[:,1],c="b")

#we also draw a diagonal line for the birth=death comparison
max_plot_pt = np.max([np.max(dim0_bc),np.max(dim1_bc)])
ax[1].plot([0,max_plot_pt],[0,max_plot_pt],c="k")
ax[1].set_ylabel("death time")
ax[1].set_xlabel("birth time")
ax[1].set_title("Persistence line graph")
plt.show()


# plotting points on unit sphere
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.scatter(d1[:,0],d1[:,1],d1[:,2], c='blue')
ax.scatter(bigC[:,0],bigC[:,1],bigC[:,2], c='red')
ax.scatter(circ3[:,0],circ3[:,1],circ3[:,2], c='green')
ax.scatter(circ4[:,0],circ4[:,1],circ4[:,2], c='orange')
sphere = Sphere([0,0,0],.97) # slightly < 1 for sake of visualization
sphere.plot_3d(ax, alpha=.5)
plt.show()
