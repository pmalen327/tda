import pandas as pd
import numpy as np
import wfdb
import ast
import pickle
import matplotlib.pyplot as plt

def load_raw_data(df, sampling_rate, path):
    if sampling_rate == 100:
        data = [wfdb.rdsamp(path+f) for f in df.filename_lr]
    else:
        data = [wfdb.rdsamp(path+f) for f in df.filename_hr]
    data = np.array([signal for signal, meta in data])
    return data

path = '/Users/stone/Desktop/project files/repos/tda/ecg_EX/ptbxl/'
sampling_rate=100

# load and convert annotation data
Y = pd.read_csv(path+'ptbxl_database.csv', index_col='ecg_id')
Y.scp_codes = Y.scp_codes.apply(lambda x: ast.literal_eval(x))

# Load raw signal data
X = load_raw_data(Y, sampling_rate, path)

# Load scp_statements.csv for diagnostic aggregation
agg_df = pd.read_csv(path+'scp_statements.csv', index_col=0)
agg_df = agg_df[agg_df.diagnostic == 1]

def aggregate_diagnostic(y_dic):
    tmp = []
    for key in y_dic.keys():
        if key in agg_df.index:
            tmp.append(agg_df.loc[key].diagnostic_class)
    return list(set(tmp))

# Apply diagnostic superclass
Y['diagnostic_superclass'] = Y.scp_codes.apply(aggregate_diagnostic)

# Split data into train and test
test_fold = 10
# Train
X_train = X[np.where(Y.strat_fold != test_fold)]
y_train = Y[(Y.strat_fold != test_fold)].diagnostic_superclass
# Test
X_test = X[np.where(Y.strat_fold == test_fold)]
y_test = Y[Y.strat_fold == test_fold].diagnostic_superclass


data = X_train.transpose(2,0,1)
data = data.reshape(12*19601,1000)
data = np.array(data)

# filtering for 100ish samples
indices = list(range(1201))
indices = indices[0::12]

batch = np.array([data[i] for i in indices])

fileObj = open('ecgARRAY.obj', 'wb')
pickle.dump(batch, fileObj)
fileObj.close()


# need to plot/extract one waveform measured at all 1000 mesh points
# each "data point" seems to be a set of 12 waveforms


# format and export a matrix of waveforms
# run matrix through ~/driver