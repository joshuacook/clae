#!/usr/bin/env python
# coding: utf-8

# # Don't Drop Out Of Numpy

# In[1]:


import numpy as np
import matplotlib.pyplot as plt


# Remember, its very important when working in `numpy` that you do not "drop out of `numpy`" that is change your data into regular lists.

# In[6]:


type(1.4)


# In[2]:


type([1,2])


# In[3]:


type(np.array([1,2]))


# The most common way to "drop out of `numpy`" is to use a list comprehension on a `numpy` array.

# In[7]:


l = []
for v in range(10):
    l.append(1 if v%2==0 else 0)
l


# In[8]:


[1 if v%2==0 else 0 for v in range(10)] # list comprehension


# In[9]:


type([v for v in np.array([1,2])])


# #### `numpy` vs `math`
# 
# Python has a `math` library in addition to `numpy`. The main difference is that `numpy` works on vectors, whereas `math` works on scalar values.

# In[12]:


import math


# We will need cosine and sine functions to define our true function. As we will be performing vector calculations, we will need to use the `numpy` trigonometric functions as opposed to the `math` trigonometric functions.

# In[10]:


vv = np.linspace(-2*np.pi,2*np.pi,100)
plt.scatter(vv, np.cos(vv)) # this is a vectorized operation


# In[16]:


try:
    math.cos(vv)
except TypeError as e:
    print("ERROR:", e)


# In[17]:


vv[:20]


# We could perform a list comprehension using the `math` function.

# In[18]:


cos_vv = [math.cos(v) for v in vv] # not vectorized, list comprehension where math.cos is applied to each element of vv


# In[19]:


cos_vv[:20]


# The issue is time.

# In[20]:


cos_vv_np = np.cos(vv)
cos_vv_np[:20]


# In[21]:


get_ipython().run_cell_magic('timeit', '', 'np.cos(vv)\n')


# In[22]:


get_ipython().run_cell_magic('timeit', '', '[math.cos(v) for v in vv]\n')


# This difference only increases for larger $n$.

# In[23]:


get_ipython().run_cell_magic('timeit', '', 'np.cos(np.linspace(1,1000,10000))\n')


# In[24]:


get_ipython().run_cell_magic('timeit', '', '[math.cos(v) for v in np.linspace(1,1000,10000)]\n')


# In[ ]:




