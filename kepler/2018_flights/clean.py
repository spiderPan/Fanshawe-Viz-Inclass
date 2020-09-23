# %% Change working directory from the workspace root to the ipynb file location. Turn this addition off with the DataScience.changeDirOnImportExport setting
# ms-python.python added
import os
try:
    os.chdir(os.path.join(os.getcwd(), 'kepler/2018_flights'))
    print(os.getcwd())
except:
    pass

# %% Import all packages
import pandas as pd

# %% Import Data
flights = pd.read_csv('./data/Cleaned_2018_Flights.csv')
flights.head()
# %% Import Airport Data
airports = pd.read_csv('./data/GlobalAirportDatabase.csv',
                       names=[
                           'Airport ID',
                           'Name', 'City',
                           'Country', 'IATA',
                           'ICAO', 'Latitude',
                           'Longitude', 'Altitude',
                           'Timezone', 'DST',
                           'Tz database time zone', 'Type',
                           'Source'])
airports.head()
airports.to_csv('./data/formatted_airports.csv')

# %%
flights.head()
# %% Look up the Origin Lat/Lng

flights_full = flights.merge(airports[['IATA', 'Longitude', 'Latitude']],
                             left_on='Origin', right_on='IATA')
# %% Clean up
flights_full['origin_lat'] = flights_full['Latitude']
flights_full['origin_long'] = flights_full['Longitude']
flights_full = flights_full.drop(['Latitude', 'Longitude', 'IATA'], axis=1)
flights_full.head()

# %% Look up the Origin Lat/Lng

flights_full = flights_full.merge(airports[['IATA', 'Longitude', 'Latitude']],
                                  left_on='Dest', right_on='IATA')
# %% Clean up
flights_full['dest_lat'] = flights_full['Latitude']
flights_full['dest_long'] = flights_full['Longitude']
flights_full = flights_full.drop(['Latitude', 'Longitude', 'IATA'], axis=1)
flights_full.head()

# %% Shrink the Data
flights_full['Quarter'] == 1
flight_info = flights_full[['AirlineCompany','Quarter', 'dest_lat',
                            'dest_long', 'origin_lat', 'origin_long']]

# %% Save datap
s1 = flight_info[flight_info['Quarter'] == 1].sample(50000).index
s2 = flight_info[flight_info['Quarter'] == 2].sample(50000).index
s3 = flight_info[flight_info['Quarter'] == 3].sample(50000).index
s4 = flight_info[flight_info['Quarter'] == 4].sample(50000).index


flight_info.loc[s1.union(s2).union(s3).union(s4)].to_csv('./data/all.csv')