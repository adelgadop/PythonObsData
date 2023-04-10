# Downloading meteorological and air quality parameters from CETESB stations
import numpy as np
import pandas as pd
import qualar as qr
import sys, os
import requests
import pickle as pkl

#%%
cetesb_stations = pd.read_csv('../namelists/stations.csv')
                              #encoding = "ISO-8859-1")

print(cetesb_stations)
start = int(input('start station (number): '))
cetesb_stations = cetesb_stations.iloc[start:,:].head(15)
print(cetesb_stations)

fecha = input('date (YYYY-MM-DD):')

obs_dates = pd.DataFrame({'date': pd.date_range(fecha, 
            periods=int(input('days:'))*24, freq='H')})
obs_dates['date_qualar']=obs_dates['date'].dt.strftime('%d/%m/%Y')

cetesb_login = input('login: ')  

if len(sys.argv) < 2 and not 'RDAPSWD' in os.environ:
    try:
        import getpass
        input = getpass.getpass
    except:
        try:
            input = raw_input
        except:
            pass

    cetesb_password = input('Password: ')
else:
    try:
       cetesb_password = sys.argv[1]
    except:
        cetesb_password = os.environ['RDAPSWD']

start_date = obs_dates.date_qualar.values[0]
end_date = obs_dates.date_qualar.values[-1]

print(obs_dates)
ruta ='../data/jul19/' # input('Insert path to save: ')

for c,n in zip(cetesb_stations.code,cetesb_stations.name):
    print('Downloading poll ' + n + ' Station')
    qr.all_photo(cetesb_login, cetesb_password, start_date, end_date, c, csv_photo=False, path=ruta)
    print('Downloading meteo ' + n + ' Station')
    qr.all_met(cetesb_login, cetesb_password,  start_date, end_date, c, csv_met=False, path=ruta)

print("""
Successfully
""")
