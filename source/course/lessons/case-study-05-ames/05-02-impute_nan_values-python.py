#!/usr/bin/env python
# coding: utf-8

# ## Impute Missing Values
# 
# This data set contains many columns with missing values. This notebook deals with accounting for missing values. Note that all of these commands were added to the file, `src/load_data-02.py` so that in subsequent notebooks the data is loaded via script.
# 
# There is a challenge to handling these missing values specific to the dataset. The file `doc/data_description.txt` contains a detailed description of each feature in this data set. Here, we see the description for `MasVnrType`.
# 
#     MasVnrType: Masonry veneer type
# 
#            BrkCmn	Brick Common
#            BrkFace	Brick Face
#            CBlock	Cinder Block
#            None	None
#            Stone	Stone
#            
# Note that one attribute for this feature is the value `None` meaning that the house in question does not have a Veneer. This is common in the data set. Unfortunately, upon loading the data, these `None` values will be taken to mean that the data is missing when they should be taken to mean `None`. Adding further complication to this, is the fact that there are features that contain actual missing values.

# In[1]:


import pandas as pd
import numpy as np


# In[2]:


test_df = pd.read_csv('data/test.csv')


# In[3]:


# Import the data loading function from our previous script
from src.load_data_01 import load_data
housing_df = load_data()


# In[ ]:


housing_df.shape


# In[ ]:


type(np.nan)


# In[ ]:


housing_df.MasVnrType


# In[ ]:


housing_df.head()


# ### Impute `nan` Values

# We begin by investigating the dataset for `nan` or "not a number" values. This value was added to numerical features with missing data. These should be taken as actual missing values.

# In[ ]:


# Count NaN values in each column
nan_sums = housing_df.isna().sum()
nan_sums[nan_sums > 0]


# In[ ]:


# Check NaN values in test dataset
nan_sums = test_df.isna().sum()
nan_sums[nan_sums > 0]


# We will impute the missing values by simply assigning to them the mean of the extant values. In pandas, we can use the `fillna()` method to replace NaN values with the mean.

# In[ ]:


housing_df['LotFrontage'].mean()


# Here we calculate the mean values for the columns with missing data.

# In[11]:


mean_LotFrontage = housing_df['LotFrontage'].mean()
mean_MasVnrArea = housing_df['MasVnrArea'].mean()
mean_GarageYrBlt = housing_df['GarageYrBlt'].mean()


# Next, we use the `fillna()` method to replace the missing values with the calculated mean values.

# In[12]:


housing_df['LotFrontage'] = housing_df['LotFrontage'].fillna(mean_LotFrontage)
housing_df['MasVnrArea'] = housing_df['MasVnrArea'].fillna(mean_MasVnrArea)
housing_df['GarageYrBlt'] = housing_df['GarageYrBlt'].fillna(mean_GarageYrBlt)


# In[ ]:


# Check if we still have NaN values in numeric columns
nan_sums = housing_df.isna().sum()
nan_sums[nan_sums > 0]


# ### Handling `None` Values

# Here, we write a set of helper functions to help us to identify the `None` values for our categorical features. In pandas, missing values in categorical columns are represented as NaN.

# In[14]:


def count_empty_values(df, feature):
    """Count empty string values in a column"""
    empty_string_mask = df[feature] == ""
    return empty_string_mask.sum()

def count_empty_total(df):
    """Count empty string values in all columns"""
    for feature in df.columns:
        if df[feature].dtype == 'object' or df[feature].dtype.name == 'category':
            empty_count = count_empty_values(df, feature)
            if empty_count > 0:
                print(f"{feature}: {empty_count}")


# In[15]:


count_empty_total(housing_df)


# Here, we note that missing values for one of the features should be taken to mean `nan`
# 
#     Electrical: Electrical system
# 
#            SBrkr	Standard Circuit Breakers & Romex
#            FuseA	Fuse Box over 60 AMP and all Romex wiring (Average)	
#            FuseF	60 AMP Fuse Box and mostly Romex wiring (Fair)
#            FuseP	60 AMP Fuse Box and mostly knob & tube wiring (poor)
#            Mix	Mixed
# 
# To handle for this, we create two lists one where an empty string signifies `None` and the other where the empty string signifies `nan`.

# In[16]:


empty_means_without = [
    "Alley", "BsmtQual", "BsmtCond", "BsmtExposure", "BsmtFinType1",
    "BsmtFinType2", "FireplaceQu", "GarageType", "GarageFinish",
    "GarageQual", "GarageCond", "PoolQC", "Fence", "MiscFeature", "MasVnrType"
]

empty_means_NA = ["Electrical"]


# In[ ]:


type(None)


# In[ ]:


type(str("None"))


# We then write a series of helper functions to use the masking on empty strings to properly handle all of these empty strings. Note that where an empty string signifies `None` we assigned the value `"None"`.

# In[19]:


def replace_empty_with_none(df, feature):
    """Replace empty strings with 'None' in categorical columns"""
    if df[feature].dtype.name != 'category':
        df[feature] = df[feature].astype('category')
    
    # Get current categories and add 'None' if not present
    current_categories = df[feature].cat.categories.tolist()
    if 'None' not in current_categories:
        new_categories = current_categories + ['None']
        df[feature] = df[feature].cat.set_categories(new_categories)
    
    # Create a mask for empty strings
    empty_string_mask = df[feature] == ''
    
    # Replace empty strings with 'None'
    df.loc[empty_string_mask, feature] = 'None'
    return df[feature]

def replace_empty_with_NA(df, feature):
    """Replace empty strings with NaN in categorical columns"""
    if df[feature].dtype.name != 'category':
        df[feature] = df[feature].astype('category')
    
    # Create a mask for empty strings
    empty_string_mask = df[feature] == ''
    
    # Replace empty strings with NaN
    df.loc[empty_string_mask, feature] = np.nan
    return df[feature]


# In[20]:


for feature in empty_means_without:
    if feature in housing_df.columns:
        housing_df[feature] = replace_empty_with_none(housing_df, feature)

for feature in empty_means_NA:
    if feature in housing_df.columns:
        housing_df[feature] = replace_empty_with_NA(housing_df, feature)


# In[21]:


count_empty_total(housing_df)


# In[ ]:


# Check remaining NaN values
nan_sums = housing_df.isna().sum()
nan_sums[nan_sums > 0]


# Following this, we still have a `nan` value that has not been dealt with. As the affected data amounts to less than .1% our our total data, we simply drop the affected row.

# In[23]:


housing_df = housing_df.dropna()


# In[ ]:


housing_df.shape


# In[ ]:




