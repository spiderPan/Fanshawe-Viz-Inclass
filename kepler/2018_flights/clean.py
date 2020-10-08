# %% Import OS
import os

try:
    os.chdir(os.path.join(os.getcwd(), 'kepler/2018_flights'))
    print(os.getcwd())
except:
    pass

# %% Import all packages
import pandas as pd

# %% check the data
flights = pd.read_csv('./data/Cleaned_2018_Flights.csv')
flights.head()

# %% Check the airpot data
airports = pd.read_csv('./data/GlobalAirportDatabase.csv', names=[
    'Airport ID',
    'Name', 'City',
    'Country', 'IATA',
    'ICAO', 'Latitude',
    'Longitude', 'Altitude',
    'Timezone', 'DST',
    'Tz database time zone', 'Type',
    'Source'
])
airports.head()
airports.to_csv('./data/formatted_airports.csv', index=False)

# %% Look up the origin lat/lng
flights_full = flights.merge(
    airports[['IATA', 'Longitude', 'Latitude']], left_on='Origin', right_on='IATA')
flights_full.head()

# %% Clean up the Origin
flights_full['origin_lat'] = flights_full['Latitude']
flights_full['origin_long'] = flights_full['Longitude']
flights_full = flights_full.drop(['Latitude', 'Longitude', 'IATA'], axis=1)
flights_full.head()


# %% Look up the dest lat/lng and then clean it up
flights_full = flights_full.merge(
    airports[['IATA', 'Longitude', 'Latitude']], left_on='Dest', right_on='IATA')
flights_full.head()

# %% Clean up
flights_full['dest_lat'] = flights_full['Latitude']
flights_full['dest_long'] = flights_full['Longitude']
flights_full = flights_full.drop(['Latitude', 'Longitude', 'IATA'], axis=1)
flights_full.head()

# %% Output the data
flights_full.to_csv('./data/all_flights.csv')

# %%
flights_full.shape

# %% Shrink the data

s1 = flights_full[flights_full['Quarter'] == 1].sample(5000).index
s2 = flights_full[flights_full['Quarter'] == 2].sample(5000).index
s3 = flights_full[flights_full['Quarter'] == 3].sample(5000).index
s4 = flights_full[flights_full['Quarter'] == 4].sample(5000).index

flights_full.loc[s1.union(s2).union(s3).union(
    s4)].to_csv('./data/simplified_flights.csv')
