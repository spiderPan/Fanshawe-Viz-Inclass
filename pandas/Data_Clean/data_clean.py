# %% Change working directory from the workspace root to the ipynb file location. Turn this addition off with the DataScience.changeDirOnImportExport setting
# ms-python.python added
import os
try:
    os.chdir(os.path.join(os.getcwd(), 'pandas/Data_Clean'))
    print(os.getcwd())
except:
    pass

# %% Import all packages
import pandas as pd

# %% Import Data
df = pd.read_csv('./data/sales.csv')
df.head()

# %%
df.shape


# %%
df.dtypes

# %% Covert the ordered_at to time format
df['ordered_at'] = pd.to_datetime(df['ordered_at'])
df.dtypes
# %% Covert the price to float by dropping the $
for column in ['price', 'line_total']:
    df[column] = df[column].apply(lambda x: float(x[1:]))

df.head()

# %% Deal with the duplication
is_duplicated = df.duplicated()
print(is_duplicated)
df[is_duplicated].shape[0]

# Drop all duplications
df = df.drop_duplicates()
df
# %% Deal with Null values
df.isnull().sum()

# Since missing data has nothing to do with this data set,
# we are going to drop all
df = df.dropna()
df
# %% Sanity check..
is_line_total_cal_right = (df['price'] * df['quantity']) == df['line_total']
is_line_total_cal_not_right = (
    df['price'] * df['quantity']) != df['line_total']
df[is_line_total_cal_not_right]

# if we decide to drop the mis cal rows
df = df[is_line_total_cal_right]

# %% Check if all data makes sense??
df.describe()
df[df['line_total'] < 0].shape[0]

# Only keep the rows with positive line_total
df = df[df['line_total'] >= 0]
df.describe()
# %% Let's assume we done everything...
df.to_json('./data/sales_clean_col_row.json')
df.to_json('./data/sales_clean_obj.json', orient='records')
df.to_csv('./data/sales_clean.csv', index=None)

# %%
