# %% Define a list and adding value to it
a = 'tiger'
b = 'giraffe'
animals = ['elephant', 'lion', a, b]
animals

# %% Adding values to list

animals += ['monkey', 'dog']
animals.append('cat')
animals.extend(['bird'])
animals

# %% Update list
list = ['Google', 'Microsoft', '1997', '2000']
list[::3]

list[1] = 'Uber'
list

# %% Delete from List
list = ['Google', 'Microsoft', '1997', '2000']

list.remove('Microsoft')
del list[2]
list


# %%
print(list.pop())
print(list)

# %% Try it out
# %% Write a list with two kinds of fruits
list = ['Apple','Banana']
list
# %% Adding three more into it
# list+=['Pear','Grape','Peach']
list.extend(['Pear','Grape','Peach'])
list
# %% Swap the second one with the third one
swap = list[1]
list[1] = list[2]
list[2] = swap
list

# %% Remove the last one
# list.pop()
# list

del list[-1]

# %% Remove the second one from the list
del list[1]