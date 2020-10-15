# %%
import os
try:
    os.chdir(os.path.join(os.getcwd(), 'kepler/london_transit'))
    print(os.getcwd())
except:
    pass

# %% Import all packages
import pandas as pd

# %% Import all data
stops = pd.read_csv('./data/stops.csv')
trips = pd.read_csv('./data/trips.csv')
stop_times = pd.read_csv('./data/stop_times.csv')

print(stop_times)

# %% Merge stops into stop_times by stop_id
full_trips = stop_times.merge(
    stops[['stop_lat', 'stop_lon', 'stop_id', 'stop_name']], on='stop_id')
full_trips.head()

# %% Merge trips into full_trips by trip_id
full_trips = full_trips.merge(
    trips[['trip_id', 'route_id']], on='trip_id'
)
full_trips.head()

# %% customize function

def validate_time(date_str):
    x = int(date_str.split(':', 1)[0])
    if x >= 24:
        return str(x % 24) + date_str[2:]
    else:
        return date_str


print(validate_time('27:01:47'))

# %% Clean the time format
full_trips['arrival_time'] = full_trips['arrival_time'].apply(validate_time)
full_trips['arrival_time'] = full_trips['arrival_time'].apply(
    lambda x: x.replace(' ', '0')
)
full_trips['departure_time'] = full_trips['departure_time'].apply(validate_time)
full_trips['departure_time'] = full_trips['departure_time'].apply(
    lambda x: x.replace(' ', '0')
)
print(full_trips)

# %% Convert arrival_time departure_time to be time
full_trips['arrival_time'] = pd.to_datetime(
    full_trips['arrival_time'], format="%H:%M:%S").dt.time
full_trips['departure_time'] = pd.to_datetime(
    full_trips['departure_time'], format="%H:%M:%S").dt.time

print(full_trips)

# %% Export to new csv
full_trips.to_csv('./data/full_trips.csv')
