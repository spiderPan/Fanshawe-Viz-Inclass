# %%
import os
try:
    os.chdir(os.path.join(os.getcwd(), 'kepler/london_transit'))
    print(os.getcwd())
except:
    pass

# %% Import all packages
import json  
import pandas as pd
from pandas.io.json import json_normalize

# %% Import Data
stops = pd.read_csv('./data/September-2018.csv')
stops.head()


# %% Count how many routes
stops['Route Count'] = stops['Routes'].str.count(',') +1
stops.head()

# %%
# stations[['latitude','longitude']] = pd.DataFrame(stations['Coords'].tolist(),index=stations.index)
# stations.head()

# %% 
stations = stations.drop(['Coords'], axis=1)
stations.head()

# %%
stops.to_csv('./data/stops.csv',index=False)