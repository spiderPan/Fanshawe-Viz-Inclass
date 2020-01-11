# %% Load Library
import requests

URL = 'https://movie.thepan.cn/'

# %% Request
r = requests.get(URL)

#%% Check the requests details
print(r.request.headers)

# %% Check Response Details
print(r.headers)
print(r.status_code)

# %% Check the Response text
print(r.text)
