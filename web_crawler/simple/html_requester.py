# %% Load library
import wget
import json
from requests_html import HTMLSession

# %% Build the session
session = HTMLSession()

# %% Request
URL = 'https://movie.thepan.cn/'
r = session.get(URL)
print(r)

# %%
print(r.html.links)
print(r.html.absolute_links)

# %%
site_nav = r.html.find('#site-nav a', first=True)
print(site_nav.html)
print(site_nav.text)

# %%
movie_titles = [movie.text for movie in r.html.find('.movie-item h2')]
print(movie_titles)
print(len(movie_titles))


# %% TODO: 2 mins to get a list of movie release date
movie_dates = [movie.text for movie in r.html.find('.movie-item p')]
print(movie_dates)

# %%
output_file = 'movie.json'
movies = dict(zip(movie_titles, movie_dates))

with open(output_file, 'w') as output_handler:
    json.dump(movies, output_handler, indent=4)

# %%
movie_imgs = [movie.attrs['src'] for movie in r.html.find('.movie-item img')]
for url in movie_imgs:
    wget.download(URL+'/'+url)

# %%
