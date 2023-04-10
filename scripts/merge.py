# Importing libraries
import pandas as pd
import os
import numpy as np
import glob
import pickle as pkl 
import fnmatch

# Function -------------------------------------------------------------
def read_data(files):
    data = pd.DataFrame()

    for f in files:
        df = pd.read_pickle(f)
        data = pd.concat([data,df])
    
    for par in data.columns:
        data[par] = data[par].astype(float)

    data.index = data.index.set_names(['local_date'])
    data.reset_index(inplace=True)

    return data

# Meteorological and air quality files saved as pickle (.pkl)------------
mes = input('Month (e.g.: jul19): ')
path = '../data/'+mes + '/' 

met_files = [f for f in sorted(glob.glob(path+'met*'))] 
aq_files = [f for f in sorted(glob.glob(path+'photo*'))] 

print(met_files, aq_files)

# Merge data ------------------------------------------------------------
met = read_data(met_files)
aq  = read_data(aq_files)

obs = pd.merge(aq, met, on=['local_date','code'])

print(obs.info())

# Save merge files as pickle file
obs.to_pickle('../post/obs_'+mes+'.pkl')

