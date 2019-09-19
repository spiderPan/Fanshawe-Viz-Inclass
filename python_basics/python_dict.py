# %% Python Dict

dict1 = {'abc': 123}
dict2 = {'abc': 123, 98.6: 37}

dict2

# %% Read values from dict
dict = {'Name': 'Tom',
        'Age': 7,
        'Class': 'First'}

print('dict["Name"]:', dict['Name'])


print(dict.get('Hometown', 0))
print(dict.get('Name', ''))
# %% Update value from Dict
dict = {'Name': 'Tom',
        'Age': 7,
        'Class': 'First'}

dict['Age'] = 11
dict['School'] = 'Fanshawe'

print(dict)

# %% Delete value from Dict
dict = {'Name': 'Tom',
        'Age': 7,
        'Class': 'First'}

del dict['Name']
print(dict)
dict.clear()
print(dict)
del dict
print(dict)

# %% Iterate through the Dict
dict = {'Name': 'Tom',
        'Age': 7,
        'Class': 'First'}

for i, j in dict.items():
    print(i, '===>', j)


# %% Try to get rid of the duplicated value from the following dict

d1 = {'a': 300,
      'b': 200,
      'c': 300,
      'd': 200}

# Hint: check if item exists in List, if(item in List){}

# Solutin One
d2 = {}

for i, j in d1.items():
    if j not in d2.values():
        d2[i] = j
d2
        



#%%
