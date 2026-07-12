#!/usr/bin/env python
# coding: utf-8

# # Interpreting the PCA
#
# Estimated time: 30 minutes
# 
# One of the most useful applications of the Principal Component Analysis is to use the interpretation of the analysis for Latent Feature Extraction.

# Recall that each dimension found by the PCA is a linear combination of the $p$ features so that each Principal Component is given by 
# 
# $$Z_i = \phi_{1i}X_1 + \phi_{2i}X_2 + \dots + \phi_{pi}X_p$$

# It is of note that each $\phi_i = (\phi_{i1}, \phi_{i2}, \dots, \phi_{p1})$ is normalized in the linear algebra sense so that the magniture of each, $\rvert\phi_i\rvert = 1$.

# *Introduction to Statistical Learning* refers to these $\phi_{ij}$ as **loadings**. 
# 
# Consider the following example we looked at previously:
# 

# In[ ]:


cd ..


# In[2]:


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


# In[3]:


customer_df = pd.read_pickle('data/final.p')


# In[ ]:


np.random.seed(42)

sample_df = customer_df.sample(5)
sample_df


# In[ ]:


sample_df.plot(kind='bar', figsize=(12,8))
_ = plt.xticks(range(5),['Sample 1','Sample 2','Sample 3', 'Sample 4','Sample 5'])


# In[6]:


from sklearn.decomposition import PCA


# In[ ]:


np.random.seed(1)
pca = PCA()
pca.fit(customer_df)


# In[ ]:


(pd.DataFrame(pca.components_, columns=customer_df.columns)
 .plot(kind='bar', figsize=(20,5)))


# In[9]:


pca.components_[0] = -pca.components_[0]


# In[ ]:


import lib.viz_helper as viz
pca_df = viz.pca_results(customer_df, pca)


# In[ ]:


pca_reduced = PCA(2)
pca_reduced.fit(customer_df)


# In[12]:


pca_reduced.components_[0] = -pca_reduced.components_[0]


# In[13]:


latent_variables = ['retailer', 'restaurant']


# In[14]:


sample_pca_df = pd.DataFrame(pca_reduced.transform(sample_df), 
                             columns=latent_variables,
                             index=sample_df.index)


# In[ ]:


sample_df.plot(kind='bar', figsize=(12,8))
plt.title("Original Data")
_ = plt.xticks(range(5),['Sample 1','Sample 2','Sample 3', 'Sample 4','Sample 5'])

sample_pca_df.plot(kind='bar', figsize=(12,8))
plt.title("PCA transformed Data")
_ = plt.xticks(range(5),['Sample 1','Sample 2','Sample 3', 'Sample 4','Sample 5'])


# In[ ]:


plt.plot(pca.explained_variance_ratio_)


# In[ ]:




