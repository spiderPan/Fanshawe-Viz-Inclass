# %% Change working directory from the workspace root to the ipynb file location. Turn this addition off with the DataScience.changeDirOnImportExport setting
# ms-python.python added
import os
try:
    os.chdir(os.path.join(os.getcwd(), 'pandas/lab_1'))
    print(os.getcwd())
except:
    pass

# %%
# # ### Step 1. Import the necessary libraries


# %%
# # ### Step 2. (No code) Download the dataset from FOL users.csv, set up folder strucutre

# %%
# # ### Step 3. Load the csv and assign it to a variable called users.

# %%
# # ### Step 4. Check the first five rows of the data

# %%
# # ### Step 5. Check all data types of each column

# %%
# # ### Step 6. Discover what is the mean age per occupation
# Hint: use users.groupby(COLUMN_NAME_LIST).age.mean() to get the mean age per COLUMN_NAME or multiple COLUMN_NAMEs

# %%
# ### Step 7. For each occupation, calculate the minimum and maximum ages
# Hint: use users.groupby[COLUMN_NAME_LIST].age.agg(['min', 'max']) to get the minimum and maximum ages per COLUMN_NAME

# %%
# ### Step 8. Filter all users who are older than 40

# %%
# ### Step 9. Sort all users by age in descending order (older)

# %%
# ### Step 10. Count the number of the male users vs female users
