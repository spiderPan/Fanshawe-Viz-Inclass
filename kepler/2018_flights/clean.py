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
airports.to_csv('./data/formatted_airports.csv',index=False)
