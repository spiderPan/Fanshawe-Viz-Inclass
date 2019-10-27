<<<<<<< HEAD
# %%
import pandas as pd
import os
import re
import matplotlib.pyplot as plt
import seaborn

# %%
=======
# %% Change working directory from the workspace root to the ipynb file location. Turn this addition off with the DataScience.changeDirOnImportExport setting
# ms-python.python added
import os
>>>>>>> bb13863a958036ba06d659b9d9dde6a4d9e222f9
try:
    os.chdir(os.path.join(os.getcwd(), 'pandas/Data_Clean'))
    print(os.getcwd())
except:
    pass

<<<<<<< HEAD
=======
# %% Import all packages
import pandas as pd

>>>>>>> bb13863a958036ba06d659b9d9dde6a4d9e222f9
# %% Import Data
df = pd.read_csv('./data/sales.csv')
df.head()

# %%
df.shape

<<<<<<< HEAD
# %%
df.dtypes

# %% Fix column datatypes
df['ordered_at'] = pd.to_datetime(df['ordered_at'])
for column in ['price', 'line_total']:
    df[column] = df[column].apply(lambda x: float(x[1:]))

df.dtypes
# %% Duplicate Rows?
df[df.duplicated()].shape[0]
df = df.drop_duplicates()

# %% Deal with null values
df.isnull().sum()
# %%
df[df['name'].isnull()].head()

# %% Missing name has nothing to do with the rest data, remove
df = df.dropna()

# %% Sanity check for value ranges and to check assumptions

# Some math issue?
df[(df['price'] * df['quantity']) != df['line_total']].shape[0]

# %% Only keep those valid line_total
df = df[(df['price'] * df['quantity']) == df['line_total']]
df.describe()
# %% Line total less than 0??
df[df['line_total'] < 0].shape[0]

# %% Only keep those valid
df = df[df['line_total'] >= 0]
df.describe()

# %% Text Clean up
pattern = r'^"([A-Z ]+)" (.*)'


def transform_func(x): return re.findall(pattern, x)[0]


df[['category', 'name']] = df['name'].apply(transform_func).apply(pd.Series)


# %%
f, ax = plt.subplots(figsize=(8, 6))
df.groupby('category')['line_total'].sum().sort_values(
    ascending=False).plot(kind='bar')
f.autofmt_xdate()
plt.show()

# %% Save the clean data into json
df.to_json('./data/sales_clean.json', orient='records')
=======

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
>>>>>>> bb13863a958036ba06d659b9d9dde6a4d9e222f9
