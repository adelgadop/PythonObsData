# mergedData.py
import pandas as pd
import os
import numpy as np

stations = pd.read_csv('cetesb_station_2017_codes_qualr.csv',
                      encoding = "ISO-8859-1")

# Meteorological parameters
f16 = [file for file in os.listdir('./data/met/Y2016/')]
f17 = [file for file in os.listdir('./data/met/Y2017/')]
f18 = [file for file in os.listdir('./data/met/Y2018/')]

# Function
def readDat(files, path = './data/met/'):
    Data = pd.DataFrame()
    
    for file in files:
        df = pd.read_csv(path + file)
        Data = pd.concat([Data,df])
    return Data
# End

met16 = readDat(f16, path = './data/met/Y2016/')
met17 = readDat(f17, path = './data/met/Y2017/')
met18 = readDat(f18, path = './data/met/Y2018/')

metData = pd.concat([met16,met17,met18])
metData['station'] = [stations[stations.code == i].name.values[0] for i in metData.code]

# Air quality parameters
f16 = [file for file in os.listdir('./data/photo/Y2016/')]
f17 = [file for file in os.listdir('./data/photo/Y2017/')]
f18 = [file for file in os.listdir('./data/photo/Y2018/')]

aq16 = readDat(f16, path = './data/photo/Y2016/')
aq17 = readDat(f17, path = './data/photo/Y2017/')
aq18 = readDat(f18, path = './data/photo/Y2018/')

aqData = pd.concat([aq16,aq17,aq18])
aqData['station'] = [stations[stations.code == i].name.values[0] for i in aqData.code]
data = pd.merge(metData, aqData)
data.to_csv("airData.csv", index=False)