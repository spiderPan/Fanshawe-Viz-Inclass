# %% Change working directory from the workspace root to the ipynb file location. Turn this addition off with the DataScience.changeDirOnImportExport setting
# ms-python.python added
import os
try:
    os.chdir(os.path.join(
        os.getcwd(), 'pandas/midterm'))
    print(os.getcwd())
except:
    pass

# %% [markdown]
# ### Step 1. Import the necessary libraries
import pandas as pd

# %% [markdown]
# ### Step 2. (No code) Download the dataset from FOL drinks.csv, set up folder strucutre
# %% [markdown]
# ### Step 3. Assign it to a variable called drinks.
drinks = pd.read_csv('./data/drinks.csv')
drinks
# %% [markdown]
# ### Step 4. Which continent drinks more beer on average?
drinks.groupby('continent').beer_servings.agg(
    ['mean']).sort_values(['mean'], ascending=False)
# %% [markdown]
# ### Step 5. For each continent print the statistics for wine consumption.
# Hint: to print the statistics for certain dataframe, you can use `.describe()`
drinks.groupby('continent').wine_servings.describe()

# drinks.wine_servings.describe()
# %% [markdown]
# ### Step 6. Print the mean alcoohol consumption per continent for every column
drinks.groupby('continent').mean()
# %% [markdown]
# ### Step 7. Print the median alcoohol consumption per continent for every column
drinks.groupby('continent').median()
# %% [markdown]
# ### Step 8. Print the mean, min and max values for spirit consumption per continent.
# #### This time output a DataFrame
drinks.groupby('continent').spirit_servings.agg(['mean', 'min', 'max'])

# %%
# ### Step 9. Find out the country's name for
# - Consumed the most beer_servings
# - Consumed the most spirit_servings
most_beer_country = drinks.sort_values(
    ['beer_servings'], ascending=False).head(1)['country']
most_spirit_country = drinks.sort_values(
    ['spirit_servings'], ascending=False).head(1)['country']

print(most_beer_country)
print(most_spirit_country)

# %%
# ### Step 10. Find out countries name that consumed more than 200 wine_servings
drinks[drinks['wine_servings'] > 200]
