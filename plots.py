import pickle
import mpu
import numpy as np
import pandas as pd
import gudhi as gd


fileObj = open('simplex_tree.obj', 'rb')
simplex_tree = pickle.load(fileObj)
fileObj.close()

# not working
print(simplex_tree.num_simplices())