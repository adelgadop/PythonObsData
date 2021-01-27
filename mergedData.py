# mergedData.py
import pandas as pd
import os
import numpy as np
import glob
import pickle as pkl

stations = pd.read_csv('stations.csv')
#                      encoding = "ISO-8859-1")

# Meteorological parameters
f14 = [file for file in sorted(glob.glob('./Y2014/*met*'))]
f15 = [file for file in sorted(glob.glob('./Y2015/*met*'))]
f16 = [file for file in sorted(glob.glob('./Y2016/*met*'))]
f17 = [file for file in sorted(glob.glob('./Y2017/*met*'))]
f18 = [file for file in sorted(glob.glob('./Y2018/*met*'))]

# Function
def readDat(files):
    Data = pd.DataFrame()

    for file in files:
        df = pd.read_csv(file)
        Data = pd.concat([Data,df])
    return Data
# End

met14 = readDat(f14)
met15 = readDat(f15)
met16 = readDat(f16)
met17 = readDat(f17)
met18 = readDat(f18)

metData = pd.concat([met14,met15,met16,met17,met18])
metData['station'] = [stations[stations.code == i].name.values[0] for i in metData.code]

# Air quality parameters
f14 = [file for file in sorted(glob.glob('./Y2014/*photo*'))]
f15 = [file for file in sorted(glob.glob('./Y2015/*photo*'))]
f16 = [file for file in sorted(glob.glob('./Y2016/*photo*'))]
f17 = [file for file in sorted(glob.glob('./Y2017/*photo*'))]
f18 = [file for file in sorted(glob.glob('./Y2018/*photo*'))]

aq14 = readDat(f14)
aq15 = readDat(f15)
aq16 = readDat(f16)
aq17 = readDat(f17)
aq18 = readDat(f18)

aqData = pd.concat([aq14,aq15,aq16,aq17,aq18])
aqData['station'] = [stations[stations.code == i].name.values[0] for i in aqData.code]
data = pd.merge(metData, aqData)
data.loc[:,'local_date'] = pd.to_datetime(data['date'], format='%Y-%m-%d %H:%M:%S').dt.tz_localize("UTC")
data.to_pickle('air_data.pkl')

