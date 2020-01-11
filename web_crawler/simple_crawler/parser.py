#%% Load Library
from requests_html import HTMLSession
import json

# %% Build the session
session = HTMLSession()

#%% Request
URL = 'https://movie.thepan.cn/'
r = session.get(URL)

# %% Check the request

# Check all links
print(r.html.links)
print(r.html.absolute_links)

# %% Find element by CSS selector (id, class)
site_title = r.html.find('#site-title', first=True)
print(site_title.html)
print(site_title.text)

# %% Get movie titles
movie_titles = [movie.text for movie in r.html.find('.movie-item h2')]
print(movie_titles)


## 20 mins Try it out get all movies' release date??
movie_dates = [movie.text for movie in r.html.find('.movie-item .release-date')]
print(movie_dates)

# %% Combine them together to JSON
movies = dict(zip(movie_titles,movie_dates))
print(movies)

# Save into json file
output_file = 'movie.json'
with open(output_file, "w") as output_handler:
    json.dump(movies, output_handler, indent=4)
