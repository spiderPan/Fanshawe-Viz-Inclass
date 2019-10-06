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

# %% [markdown]
# ### Step 2. (No code) Download the dataset from FOL drinks.csv, set up folder strucutre
# %% [markdown]
# ### Step 3. Assign it to a variable called drinks.

# %% [markdown]
# ### Step 4. Which continent drinks more beer on average?

# %% [markdown]
# ### Step 5. For each continent print the statistics for wine consumption.
# Hint: to print the statistics for certain dataframe, you can use `.describe()`

# %% [markdown]
# ### Step 6. Print the mean alcoohol consumption per continent for every column

# %% [markdown]
# ### Step 7. Print the median alcoohol consumption per continent for every column

# %% [markdown]
# ### Step 8. Print the mean, min and max values for spirit consumption.
# #### This time output a DataFrame

# %% 
# ### Step 9. Find out the country's name for 
# - Consumed the most beer_servings
# - Consumed the most spirit_servings

# %% 
# ### Step 10. Find out countries name that consumed more than 200 wine_servings

