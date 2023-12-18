# Topological Data Analysis for Electrocardiogram Signals
We used PTB-XL data available here:
https://www.physionet.org/content/ptb-xl/1.0.3/#files-panel\
\
To run, navigate to the parent directory and pass with the arguments:
`fig, ax = main(data, t, max_edge_length, min_dimension, max_dimension)`
then to display the figure, just call `plt.show()`.\
\
Code in `driver` can be easily modified to save plots as objects or images or return
additional information such as Betti Numbers or stars etc.\
\
For inputs:\
    \
    1. `data` is the matrix as a numpy array or pandas dataframe\
    \
    2. `t` is a 1-D array with length of that of the the columns of `data`. For time series, this will be an array of timestamps.\
    \
    3. `max_edge_length` is the maximum filtration or "alpha" value\
    \
    4. `min_dimension` is the lower bound for the dimension of homological features\
        to be returned and produced in the barcode graph\
    \
    5. `max_dimension` is the upper bound for the dimension of homological features to be returned and produced in the barcode graph\
    \
The pipeline is structured as follows:\
    \
    1. input data is received as a matrix in the form of a numpy array or pandas dataframe\
    \
    2. a pairwise distance matrix is computed from the data with respect to the first Wasserstein distance\
    \
    3. a simplex tree object is computed from the distance matrix\
    \
    4. a persistence barcode plot is generated and returned from the simplex tree object\
