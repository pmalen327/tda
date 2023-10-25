from time_series import simplex_tree, ds
import numpy as np

# this is gross af
def metric_filter(minDim, maxDim, minDS, maxDS):
    filter = []
    metrics = []

    simplex_tree.compute_persistence()

    for item in simplex_tree.persistence():
        if item[0] in range(minDim, maxDim + 1):
            filter.append(item)

    for item in filter:
        if (item[1][0] in range(minDS, maxDS)) and (item[1][1] in range(minDS, maxDS)):
            metrics.append([item[1][0], item[1][1]])
    
    return metrics

print(ds.shape)


# dsFilter = np.array(ds[np.triu_indices(ds.shape[0], k=1)])
# print(dsFilter)
# print(len(dsFilter))



# TODO
# threshold out values in ds
# get indices of values that survive
# retrieve the corresponding symbols from time_series_df.obj
# I know HOW to do this I just don't WANT to do this lolz

# FUCKCKCKCKCKCKCKCKCKCKCKYWUCKY









