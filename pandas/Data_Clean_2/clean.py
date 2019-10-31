# %% Change working directory from the workspace root to the ipynb file location. Turn this addition off with the DataScience.changeDirOnImportExport setting
# ms-python.python added
import os
try:
    os.chdir(os.path.join(os.getcwd(), 'pandas/Data_Clean_2'))
    print(os.getcwd())
except:
    pass

# %%
import pandas as pd
import numpy as np

# %%
df = pd.read_csv('./data/real_estate_dataset.csv')
df


# Common questions guid you through
# 1. What are the features??
# 2. Whare the expected types? (int, float, string, boolean ...)
# 3. Is there obvious missing data (values that Pandas can detect)?
# 4. Is there other types of missing data that's not so obvious? (Pandas won't easily detect)

# %%
df.head()
df.sample(5)


# %%
df.dtypes

# %%
for column in ['ST_NUM']:
    df[column] = df[column].apply(lambda x: int(x[1:]))

# %%
print(df['ST_NUM'])
print(df['ST_NUM'].isnull())


# %% What if Pandas doesn't recognize it?
print(df['NUM_BEDROOMS'])
print(df['NUM_BEDROOMS'].isnull())


# %% Reload the data
missing_values_symbols = ["n/a", "na", "--"]
df_formatted = pd.read_csv(
    './data/real_estate_dataset.csv', na_values=missing_values_symbols)


df_formatted

# %% Not so obvious missing data
is_own_occupied_valid = df_formatted['OWN_OCCUPIED'].isin(['Y','N'])
df_formatted[~is_own_occupied_valid]

df_formatted.loc[~is_own_occupied_valid,'OWN_OCCUPIED'] = np.nan

df_formatted['OWN_OCCUPIED']



# %% 
df_formatted['ST_NUM']
df_formatted.loc[2,'ST_NUM'] = 125
df_formatted['ST_NUM']

df_formatted['ST_NUM'].fillna(125, inplace=True)
df_formatted['ST_NUM']
# %%
median = df_formatted['NUM_BEDROOMS'].median()
df_formatted['NUM_BEDROOMS'].fillna(median, inplace=True)
df_formatted['NUM_BEDROOMS']
# %%
#df_formatted.to_json('./data/real_estate_clean_col_row.json')
df_formatted.to_json('./data/real_estate_clean_obj.json', orient='records')
#df_formatted.to_csv('./data/real_estate_clean.csv', index=None)


# %%
