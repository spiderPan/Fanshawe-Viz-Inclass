# %%
import pandas as pd

# %%
try:
    os.chdir(os.path.join(os.getcwd(), 'pandas/Getting_&_Knowing_Your_Data/'))
    print(os.getcwd())
except:
    pass

# %%
euro12 = pd.read_csv('./data/Euro_2012_stats_TEAM.csv', sep=",")
euro12

# %%
euro12.head()

euro12.shape

print(euro12.shape[1])
# %%
euro12.info()
euro12.columns

# %%
euro12['Clearances off line']
euro12.index
# %%
euro12.values[1][0]
euro12.Team

# %%
euro12.Team.count()


# %%
cards = euro12[['Team', 'Yellow Cards', 'Red Cards']]
cards

# %%
cards.sort_values(['Red Cards', 'Yellow Cards'], ascending=False)

# %%
cards['Yellow Cards'].mean()

# %%
morethan6 = euro12[euro12['Goals'] > 6]
morethan6

# %% Shooting Accuracy > 40%
moreaccuracy = euro12[euro12['Shooting Accuracy'] > '40%']
moreaccuracy



#%% Find out the most accurate shooting team
euro12.sort_values(['Shooting Accuracy'],ascending=False)


#%%
