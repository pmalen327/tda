# tda
Add line returns and white space appropriately. Polish things up.

To run, navigate to the parent directory and pass with the arguments:
`fig, ax = main(data, t, max_edge_length, min_dimension, max_dimension)`
then to display the figure, just call `plt.show()`.\
\
Code in `driver` can be easily modified to save plots as objects or images or return
additional information such as Betti Numbers or stars etc.\
\
For inputs:\
    `data` is the matrix as a numpy array or pandas dataframe\
    `t` is a 1-D array with length of that of the the columns of `data`. For time series,\
        this will be an array of timestamps.\
    `max_edge_length` is the maximum filtration or "alpha" value\
    `min_dimension` is the lower bound for the dimension of homological features\
        to be returned and produced in the barcode graph\
    `max_dimension` is the upper bound for the dimension of homological features\
        to be returned and produced in the barcode graph\


The pipeline is structured as follows:\
    1: input data is received as a matrix in the form of a numpy array or pandas dataframe\
    \
    2: a pairwise distance matrix, is computed from the data with respect to the first\
        Wasserstein metric\
    \
    3: a simplex tree object is computed from the distance matrix\
    \
    4: a persistence barcode plot is generated and returned from the simplex tree object\
\
All other files and directories were used to produce the figures and examples as outlined\
in the paper. To reproduce these figures, simply run `main()` with the `data` argument as\
`fileObj = open('ecgARRAY.obj', 'rb')`\
`data = pickle.load(fileObj)`\
`fileObj.close()`\
\
for the ECG example, and similarly for the stock time series data:\
`fileObj = open('time_series_array.obj', 'rb')`\
`data = pickle.load(fileObj)`\
`fileObj.close()`\
\
The `data loaders` and `ecg_EX` directories contain the data and scripts used
to preprocess the appropriate data and pickle the daata into the `ecgARRAY.obj`
and `time_series_array.obj` objects.