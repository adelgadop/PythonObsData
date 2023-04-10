import pandas as pd
import matplotlib.pyplot as plt
from funciones import split

# Importing stations and meteorological and air quality observations
stations = pd.read_csv('../namelists/stations.csv')
my = input('Enter monthyear (e.g., jul15): ')
obs = pd.read_pickle('../post/obs_' + my + '.pkl')

grupos = list(obs.code.unique())
grup_codes = list(split(grupos, 4))

# Explore Data Analysis ---------------------------------------------
print('We analyze stations with completed hourly data for pm2.5 and other gases')

def plot_grupos(pol,obs,grup_codes,stations):
    if pol == 'pm2_5':
        unidades = 'PM$_{2.5}$ ($\mu$g m$^{-3}$)'
    elif pol =='pm10':
        unidades = 'PM$_{10}$ ($\mu$g m$^{-3}$)'
    elif pol =='no':
        unidades = 'NO ($\mu$g m$^{-3}$)'
    elif pol =='no2':
        unidades = 'NO$_2$ ($\mu$g m$^{-3}$)'
    elif pol =='o3':
        unidades = 'O$_3$ ($\mu$g m$^{-3}$)'
    elif pol =='co':
        unidades = 'CO (ppm)'

    for i, grupo in enumerate(grup_codes):
        fig, axes = plt.subplots(len(grupo),figsize=(8,8),sharex=True)
        for ax, c in zip(axes.flatten(),grupo):
            obs.loc[obs.code == c,].plot(x='local_date',y=pol, ax=ax)
            t = stations.loc[stations.code == c,'abb'].values[0]
            ax.set_title(t+' ('+str(c)+')', loc='left')
            fig.text(0.04, 0.5, unidades, va='center', rotation='vertical')

        fig.savefig('../fig/'+ my +'/grupo_'+str(i+1)+'_'+pol+'.png', dpi=200, bbox_inches='tight', facecolor='white')

pol = input('pollutant (e.g., pm2_5, pm10, o3, no2, co, no): ')
plot_grupos(pol,obs,grup_codes,stations)

print("!!!!!! Sucessfully !!!!!!")
