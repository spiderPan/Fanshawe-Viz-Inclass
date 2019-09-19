# %% Tuple: Immuteable

# Define Tuple

tup1 = ('Google', 'Microsoft', 1997, 2000)
tup2 = "a","b","c","d"

type(tup2)
print(tup2)

#%% Read values from Tuple
tup1 = ('Google', 'Microsoft', 1997, 2000)
tup2 = "a","b","c","d"

print(tup1[0])
print(tup2[1:3])



#%% "Modify" tuple
tup1 = ('Google', 'Microsoft', 1997, 2000)
tup2 = "a","b","c","d"

tup3 = tup1 + tup2
print(tup3)


#%% Delete tuple
tup1 = ('Google', 'Microsoft', 1997, 2000)
tup2 = "a","b","c","d"

del tup1


#%%
List = ['a','b','c']
Dict = {'a':'a','b':'b'}
Tuple = ('a','b','c')