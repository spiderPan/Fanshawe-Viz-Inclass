# %%
import pandas as pd
import numpy as np
import os

try:
    os.chdir(os.path.join(os.getcwd(),'pandas/Getting_&_Knowing_Your_Data/'))
    print(os.getcwd())
except:
    pass

# %%
food = pd.read_csv('./data/en.openfoodfacts.org.products.tsv', sep='\t')

food.shape


# %%
