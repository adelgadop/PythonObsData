# PythonObsData
Developed by **Alejandro Delgado**

## Description of `download_CETESB.py`
We have scripts to download air quality and meteorological data from CETESB station networks.

Parameters downloaded are:
- Meteorological:
  * temperature (tc)
  * relative humidity (rh)
  * solar radiation (sr)
  * wind speed (ws)
  * wind direction (wd)
- Air quality:
  * ozone (o3)
  * nitrogen monoxide (no)
  * nitrogen dioxide (no2)
  * carbon monoxide (co)

### Encoding
In the terminal (for Linux) write:
```bash
$ echo $LC_CTYPE="pt_BR.utf8"
```
In `~/.bash_profile`, add:

```bash
export LC_CTYPE=pt_BR.UTF-8
```
With this encoding configuration, you won't have issues with file names created (e.g. Carapicu**í**ba.pdf).

### Run the script
Then, you have to select the date and period when `download_CETESB.py` run in the terminal. The follow is an example:

```bash
$ python download_CETESB.py 
                 name        lat        lon  code
0           Americana -22.724253 -47.339549   290
1           Araçatuba -21.186841 -50.439317   107
2          Araraquara -21.782522 -48.185832   106
3               Bauru -22.326608 -49.092759   108
4             Cambuci -23.567708 -46.612273    90
..                ...        ...        ...   ...
63  S.Miguel Paulista -23.498526 -46.444803   236
64           Sorocaba -23.502427 -47.479030    67
65    Taboão da Serra -23.609324 -46.758294   103
66              Tatuí -23.360752 -47.870799   256
67            Taubaté -23.032351 -45.575805   280

[68 rows x 4 columns]
start station (number):0
                 name        lat        lon  code
0           Americana -22.724253 -47.339549   290
1           Araçatuba -21.186841 -50.439317   107
2          Araraquara -21.782522 -48.185832   106
3               Bauru -22.326608 -49.092759   108
4             Cambuci -23.567708 -46.612273    90
..                ...        ...        ...   ...
63  S.Miguel Paulista -23.498526 -46.444803   236
64           Sorocaba -23.502427 -47.479030    67
65    Taboão da Serra -23.609324 -46.758294   103
66              Tatuí -23.360752 -47.870799   256
67            Taubaté -23.032351 -45.575805   280

[68 rows x 4 columns]
date (YYYY-MM-DD):2017-01-01
days:2
login: xxxxx@example.com
password: xxxx
                  date date_qualar
0  2017-01-01 00:00:00  01/01/2017
1  2017-01-01 01:00:00  01/01/2017
2  2017-01-01 02:00:00  01/01/2017
3  2017-01-01 03:00:00  01/01/2017
4  2017-01-01 04:00:00  01/01/2017
5  2017-01-01 05:00:00  01/01/2017
6  2017-01-01 06:00:00  01/01/2017
7  2017-01-01 07:00:00  01/01/2017
8  2017-01-01 08:00:00  01/01/2017
9  2017-01-01 09:00:00  01/01/2017
10 2017-01-01 10:00:00  01/01/2017
11 2017-01-01 11:00:00  01/01/2017
12 2017-01-01 12:00:00  01/01/2017
13 2017-01-01 13:00:00  01/01/2017
14 2017-01-01 14:00:00  01/01/2017
15 2017-01-01 15:00:00  01/01/2017
16 2017-01-01 16:00:00  01/01/2017
17 2017-01-01 17:00:00  01/01/2017
18 2017-01-01 18:00:00  01/01/2017
19 2017-01-01 19:00:00  01/01/2017
20 2017-01-01 20:00:00  01/01/2017
21 2017-01-01 21:00:00  01/01/2017
22 2017-01-01 22:00:00  01/01/2017
23 2017-01-01 23:00:00  01/01/2017
24 2017-01-02 00:00:00  02/01/2017
25 2017-01-02 01:00:00  02/01/2017
26 2017-01-02 02:00:00  02/01/2017
27 2017-01-02 03:00:00  02/01/2017
28 2017-01-02 04:00:00  02/01/2017
29 2017-01-02 05:00:00  02/01/2017
30 2017-01-02 06:00:00  02/01/2017
31 2017-01-02 07:00:00  02/01/2017
32 2017-01-02 08:00:00  02/01/2017
33 2017-01-02 09:00:00  02/01/2017
34 2017-01-02 10:00:00  02/01/2017
35 2017-01-02 11:00:00  02/01/2017
36 2017-01-02 12:00:00  02/01/2017
37 2017-01-02 13:00:00  02/01/2017
38 2017-01-02 14:00:00  02/01/2017
39 2017-01-02 15:00:00  02/01/2017
40 2017-01-02 16:00:00  02/01/2017
41 2017-01-02 17:00:00  02/01/2017
42 2017-01-02 18:00:00  02/01/2017
43 2017-01-02 19:00:00  02/01/2017
44 2017-01-02 20:00:00  02/01/2017
45 2017-01-02 21:00:00  02/01/2017
46 2017-01-02 22:00:00  02/01/2017
47 2017-01-02 23:00:00  02/01/2017
['Downloading poll Americana Station']
```
In `start station (number):` you have to write the station position number in order to starting the downloading. 
Sometimes, the internet connection fall and it's needed to reinit the dowloading, not since the beginning. 

The `download_CETESB.py` requires libraries to download information for all network stations belong to CETESB, located at the Metropolitan Area of São Paulo (MASP):

```python
import numpy as np
import pandas as pd
```

Also, we import a [`qualR.py`](https://github.com/quishqa/qualR.py/blob/master/qualR.py) package created by **quishqa** (Mario Gavidia). You will need to clone this package or download this script.

```python
import qualR.py as qr
```
We read the file with station locations points, it is important to locate this :

```python
cetesb_stations = pd.read_csv(
    '../3_Validation/cetesb_station_2017_codes_qualr.csv', # change this path if it's needed
    encoding = "ISO-8859-1")
```
## Acknowledgments
Thanks CETESB


