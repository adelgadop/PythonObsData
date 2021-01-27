# Downloading meteorological and air quality parameters from CETESB stations
import numpy as np
import pandas as pd
import qualar_py as qr
import sys, os
import requests
import pickle as pkl

cetesb_stations = pd.read_csv('./stations.csv')
                              #encoding = "ISO-8859-1")

print(cetesb_stations)
start = int(input('start station (number):'))
cetesb_stations = cetesb_stations[start:]
print(cetesb_stations)

obs_dates = pd.DataFrame({'date': pd.date_range(input('date (YYYY-MM-DD):'), 
            periods=int(input('days:'))*24, freq='H')})
obs_dates['date_qualar']=obs_dates['date'].dt.strftime('%d/%m/%Y')

cetesb_login = 'adelgado@iag.usp.br' # input('login:') 

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


met_dict = {}
pol_dict = {}
fname = input('Filename: ')

for c,n in zip(cetesb_stations.code,cetesb_stations.name):
    print('Downloading poll ' + n + ' Station')
    pol_dict[n] = (qr.all_photo(cetesb_login, cetesb_password, start_date, end_date, c, csv_photo=False))
    print('Downloading meteo ' + n + ' Station')
    met_dict[n]=(qr.all_met(cetesb_login, cetesb_password,  start_date, end_date, c, csv_met=False))

pho_name = open(fname+'_all_photo.pkl', "wb")
met_name = open(fname+'_all_met.pkl',"wb")
pkl.dump(pol_dict,pho_name)
pkl.dump(met_dict,met_name)
pho_name.close()
met_name.close()

print("""
Successfully
""")

