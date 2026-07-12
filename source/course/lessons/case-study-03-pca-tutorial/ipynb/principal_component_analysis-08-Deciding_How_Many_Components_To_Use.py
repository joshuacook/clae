#!/usr/bin/env python
# coding: utf-8

# # Deciding How Many Components To Use
#
# Estimated time: 15 minutes

# > This is done by eyeballing the scree plot, and looking for a point at which the proportion of variance explained by each subsequent principal component drops off ... this type of visual analysis is inherently ad hoc. Unfortunately, there is no well-accepted objective way to decide how many principal components are enough.
# 
# - *An Introduction to Statistical Learning, pg. 384

# In[ ]:


cd ..


# In[2]:


import matplotlib.pyplot as plt
get_ipython().run_line_magic('matplotlib', 'inline')

import numpy as np
import pandas as pd


# In[3]:


X = pd.read_pickle('data/ames_features.p')
y = pd.read_pickle('data/ames_target.p')


# In[4]:


from sklearn.decomposition import PCA


# In[ ]:


pca = PCA()
pca.fit(X)


# In[6]:


explained_var_ratio = pca.explained_variance_ratio_
cumulative_exp_var = np.cumsum(explained_var_ratio)


# In[ ]:


plt.plot(explained_var_ratio)
plt.plot(cumulative_exp_var)


# ### LESSON: The PCA is highly dependent upon scaled data

# In[ ]:


from sklearn.preprocessing import StandardScaler
X_sc = StandardScaler().fit_transform(X)
pca.fit(X_sc)


# In[ ]:


explained_var_ratio = pca.explained_variance_ratio_
cumulative_exp_var = np.cumsum(explained_var_ratio)
plt.plot(explained_var_ratio)
plt.plot(cumulative_exp_var)


# In[ ]:


plt.plot(explained_var_ratio)


# > [We are] looking for a point at which the proportion of variance explained by each subsequent principal component drops off. This is often referred to as an *elbow* in the scree plot.

# In[ ]:


plt.plot(explained_var_ratio[:10])


# > However, this type of visual analysis is inherently ad hoc. Unfortunately, there is no well-accepted objective way to decide how many principal components are enough. In fact, **the question of how many principal components are enough is inherently ill-defined**, and will depend on the specific area of application and the specific data set. In practice, we tend to look at the first few principal components in order to find interesting patterns in the data. If no interesting patterns are found in the first few principal components, then further principal components are unlikely to be of interest. Conversely, if the first few principal components are interesting, then we typically continue to look at subsequent principal components until no further interesting patterns are found. This is admittedly a subjective ap- proach, and is reflective of the fact that PCA is generally used as a tool for exploratory data analysis.

# In[ ]:




