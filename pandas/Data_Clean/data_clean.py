# %%
import pandas as pd
import os
import re
import matplotlib.pyplot as plt
import seaborn

# %%
try:
    os.chdir(os.path.join(os.getcwd(), 'pandas/Data_Clean'))
    print(os.getcwd())
except:
    pass

# %% Import Data
df = pd.read_csv('./data/sales.csv')
df.head()

# %%
df.shape

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
