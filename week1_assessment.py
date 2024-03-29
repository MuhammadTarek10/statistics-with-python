
# coding: utf-8

# You will use the values of what you find in this assignment to answer questions in the quiz that follows. You may want to open this notebook to be displayed side-by-side on screen with this next quiz.

# 1. Write a function that inputs an integers and returns the negative

# In[1]:


# Write your function here
def make_nagative(value):
    return (-1)*value


# In[2]:


# Test your function with input x
x = 4
make_nagative(x)


# 2. Write a function that inputs a list of integers and returns the minimum value

# In[3]:


# Write your function here
def get_min(values):
    return min(values)


# In[4]:


# Test your function with input lst
lst = [-3, 0, 2, 100, -1, 2]
get_min(lst)

# Create you own input list to test with


# #### Challenge problem:  
# Write a function that take in four arguments: lst1, lst2, str1, str2, and returns a pandas DataFrame that has the first column labeled str1 and the second column labaled str2, that have values lst1 and lst2 scaled to be between 0 and 1.
# 
# For example
# ```
# lst1 = [1, 2, 3]
# lst2 = [2, 4, 5]
# str1 = 'one'
# str2 = 'two'
# 
# my_function(lst1, lst2, str1, str2)
# ``` 
# should return a DataFrame that looks like:
# 
# 
# 
# |  <i></i> | one | two |
# | --- | --- | --- |
# | 0 | 0 | 0 |
# | 1 | .5 | .666 |
# | 2 | 1 | 1 |
# 
# 

# In[17]:


import pandas as pd
def make_df(lst1, lst2, str1, str2):
    df = dict(str1=lst1, str2=lst2)
    return pd.DataFrame(df)


# In[18]:


# test your challenge problem function
import numpy as np

lst1 = np.random.randint(-234, 938, 100)
lst2 = np.random.randint(-522, 123, 100)
str1 = 'one'
str2 = 'alpha'
make_df(lst1, lst2, str1, str2)

