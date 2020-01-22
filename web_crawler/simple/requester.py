# %% Load Library
import requests
import json
URL = 'https://movie.thepan.cn/'
InstgrameURL = 'https://www.instagram.com/fanshawecollege/?__a=1'

# %% Send out the request
r = requests.get(InstgrameURL)

# %% Checkout the Results
print(r)

# %%
print(r.request.headers)
print(r.headers)
# %%
print(r.text)

# %%
print(r.status_code)


# %%
data = json.loads(r.text)

print(data["graphql"]['user']['edge_followed_by']['count'])


# %%

import requests

