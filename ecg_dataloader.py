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

# path to ~/ptbxl 
PATH = '/Users/stone/Desktop/project files/repos/tda/ecg_EX/ptbxl/'
sampling_rate=100

# load and convert annotation data
Y = pd.read_csv(PATH+'ptbxl_database.csv', index_col='ecg_id')
Y.scp_codes = Y.scp_codes.apply(lambda x: ast.literal_eval(x))

# Load raw signal data
X = load_raw_data(Y, sampling_rate, PATH)

# Load scp_statements.csv for diagnostic aggregation
agg_df = pd.read_csv(PATH+'scp_statements.csv', index_col=0)
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

# stacking time series into a square array
data = X_train.transpose(2,0,1)
data = data.reshape(12*19601,1000)
data = np.array(data)

# filtering for 1000ish samples
indices = list(range(1500))
indices = indices[0::12]
t = np.linspace(0, 1000, 1000)

batch = np.array([data[i] for i in indices])
plt.plot(t, batch[0], c='blue')
plt.plot(t, batch[3], c='red')
# plt.plot(t, batch[6], c='orange')
# plt.plot(t, batch[10], c='green')
plt.savefig('ecgSigs2.png', dpi=2000, transparent=True)
# plt.show()


# fileObj = open('ecgARRAY175.obj', 'wb')
# pickle.dump(batch, fileObj)
# fileObj.close()