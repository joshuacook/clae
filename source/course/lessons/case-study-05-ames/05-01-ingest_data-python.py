#!/usr/bin/env python
# coding: utf-8

# ## Ingest the Data
# 
# This notebook contains the basic commands required to ingest the data for our work. Note that all of these commands were added to the file, `src/load_data-01.py` so that in subsequent notebooks the data is loaded via script.
# 
# ### Join the Data Sets
# 
# Often you will receive data describing the same instances from multiple data sources. The original Ames, Iowa housing data has been arbitrarily split in order to allow us the opportunity to practice joining data from different sources. 

# In[1]:


import pandas as pd
import numpy as np

zoning_df = pd.read_csv('data/zoning.csv')
listing_df = pd.read_csv('data/listing.csv')
sale_df = pd.read_csv('data/sale.csv')


# In[ ]:


zoning_df.head()


# In[ ]:


listing_df.head()


# In[ ]:


sale_df.head()


# Here, we join the three datasets using the `merge` method using the column `Id` as reference.

# In[5]:


housing_df = pd.merge(zoning_df, listing_df, on="Id") # similar to SQL join
housing_df = pd.merge(housing_df, sale_df, on="Id")


# In[ ]:


housing_df.head()


# In[ ]:


housing_df.shape


# In[ ]:


housing_df.select_dtypes(include=['number']).info()


# In[9]:


housing_df = housing_df.set_index('Id')


# In[ ]:


housing_df.head()


# In[ ]:


housing_df.loc[2]


# ### Convert Categorical Features
# 
# Several features are categorical in nature in spite of the fact that the data is stored as integer values. We must explicitly convert these features to categorical type.

# In[12]:


categorical_columns = [
    'MSSubClass', 'OverallQual', 'OverallCond', 'BsmtFullBath',
    'BsmtHalfBath', 'FullBath', 'HalfBath', 'BedroomAbvGr',
    'KitchenAbvGr', 'TotRmsAbvGrd', 'Fireplaces', 'GarageCars', 'MoSold'
]

for col in categorical_columns:
    housing_df[col] = housing_df[col].astype('category')


# In[ ]:


housing_df.info()


# In[ ]:




