# %%
import os
try:
    os.chdir(os.path.join(os.getcwd(), 'web/drinks/data'))
    print(os.getcwd())
except:
    pass
# %%
import pandas as pd
# %%
drinks = pd.read_csv('./raw/drinks.csv')
drinks.to_json('./json/drinks_by_countries.json', orient='records')


#%%
drinks_by_continent = drinks.groupby('continent',as_index=False).mean()
drinks_by_continent.to_json('./json/drinks_by_continent.json', orient='records')

# %%
