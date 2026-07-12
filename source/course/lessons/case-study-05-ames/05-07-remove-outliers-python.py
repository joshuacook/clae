#!/usr/bin/env python
# coding: utf-8

# ## Remove Outliers
# 
# In the file `src/preprocessing.py`, we perform the preprocessing steps necessary for the next phase of this project. This file does the following:
# 
# 1. Load and merge data, using the `Id` feature as we did previously
# 2. Assign correct data types, in particular, designating which features are categorical
# 3. Handle missing values, using the work we did previously
# 4. Preprocessing

# In[1]:


run src/preprocessing.py


# #### Complete Feature Sets
# 
# We are starting to do some fairly complicated feature engineering. It makes sense that we should spend some time thinking about the different data sets we are creating so that we can keep track of what we have.
# 
# 1. merged data from three different sources
# 2. handled missing values
# 3. removed skew via a log transformation on the numeric features
# 4. one-hot encoded the categorical features, kept the significant features (variance > 0.2)

# ##### Standard Scaled Data Set
# 
# One data set is the standard scaled data set. For this data set, there is no need to separate the encoded categorical features. These two dataframes comprise a complete data set
# 
# - Log Transformed, Standard Scaled Numerical Features (`numeric_log_std_sc_df`)
# - Complete One-hot Encoded Categorical Features (`categorical_encoded_df`)

# `gelman scaled` the standard deviation would be 0.5, variance would be 0.25

# In[3]:


variance = 0.2
std_dev = np.sqrt(variance)
print(std_dev, variance)


# ##### Gelman Scaled Data Set
# 
# The other data set is the Gelman scaled data set. For this data set, we have separated the encoded categorical features based on a threshold for variance. These three dataframes comprise a complete data set
# 
# - Log Transformed, Gelman Scaled Numerical Features (`numeric_log_gel_sc_df`)
# - One-hot Encoded Categorical Features with Significant Variance, Centered (`categorical_encoded_features_significant_variance_centered`)
# - One-hot Encoded Categorical Features with Insignificant Variance (`categorical_encoded_features_insignificant_variance`)
# 
# 
# 

# In[4]:


numeric_log_std_sc_df.shape, categorical_encoded_df.shape


# In[5]:


import numpy as np


# In[6]:


np.testing.assert_array_equal(numeric_log_std_sc_df.index, 
                              categorical_encoded_df.index)


# In[7]:


(numeric_log_gel_sc_df.shape,
 categorical_encoded_features_significant_variance_centered.shape,
 categorical_encoded_features_insignificant_variance.shape)


# In[8]:


np.testing.assert_array_equal(numeric_log_gel_sc_df.index,
                              categorical_encoded_features_significant_variance_centered.index)
np.testing.assert_array_equal(numeric_log_gel_sc_df.index,
                              categorical_encoded_features_insignificant_variance.index)
np.testing.assert_array_equal(categorical_encoded_features_significant_variance_centered.index,
                              categorical_encoded_features_insignificant_variance.index)


# ### Identify Outliers

# Next, we will work with the numeric features to identify outliers. As before, we will use the Tukey Method.

# In[11]:


def display_outliers(dataframe, col, param=1.5):
    Q1 = np.percentile(dataframe[col], 25)
    Q3 = np.percentile(dataframe[col], 75)
    tukey_window = param*(Q3-Q1)
    less_than_Q1_filter = dataframe[col] < Q1 - tukey_window
    greater_than_Q3_filter = dataframe[col] > Q3 + tukey_window
    tukey_filter = (less_than_Q1_filter | greater_than_Q3_filter)
    return dataframe[tukey_filter]


# In[12]:


print("Column.             Standard      Gelman ")
print("--------------------------------------------")
for col in numeric_log_std_sc_df.columns:
    print(
        "{:20} {:12} {}".format(col, 
        str(display_outliers(numeric_log_std_sc_df, col).shape),
        str(display_outliers(numeric_log_gel_sc_df, col).shape)
    ))


# Note that both scaling techniques return the same number of outliers.

# ### Count Multiple Outliers
# 
# As before, we will count row that are outlier for more than one feature.

# In[13]:


from collections import Counter


# In[14]:


def multiple_outliers(dataframe, count=2, tukey_param=1.5):
    raw_outliers = []
    for col in dataframe:
        outlier_df = display_outliers(dataframe, col, tukey_param)
        raw_outliers += list(outlier_df.index)

    outlier_count = Counter(raw_outliers)
    outliers = [k for k,v in outlier_count.items() if v >= count]
    return outliers


# In[15]:


len(multiple_outliers(numeric_log_std_sc_df)), len(multiple_outliers(numeric_log_gel_sc_df))


# Again, the two scaling techniques return the same number of multiple outliers. Unfortunately, this number of outliers represents an unacceptable loss of data, approximately 20% of our data.

# In[16]:


len(multiple_outliers(numeric_log_std_sc_df))/numeric_log_std_sc_df.shape[0]


# We set the multiple feature count higher and reassess.

# In[17]:


print(len(multiple_outliers(numeric_log_std_sc_df, count=4)), len(multiple_outliers(numeric_log_gel_sc_df, count=4)))
print(len(multiple_outliers(numeric_log_std_sc_df, count=4))/numeric_log_std_sc_df.shape[0])


# In[21]:


print(len(multiple_outliers(numeric_log_std_sc_df, count=5)), len(multiple_outliers(numeric_log_gel_sc_df, count=5)))
print(len(multiple_outliers(numeric_log_std_sc_df, count=5))/numeric_log_std_sc_df.shape[0])


# In[19]:


print(len(multiple_outliers(numeric_log_std_sc_df, count=2, tukey_param=2.5)), 
      len(multiple_outliers(numeric_log_gel_sc_df, count=2, tukey_param=2.5)))
print(len(multiple_outliers(numeric_log_std_sc_df, count=2))/numeric_log_std_sc_df.shape[0])


# Instances that are an outlier in four or more features amount to 1.3% of the data. Instances that are an outlier in five or more features amount to 0.5% of the data.  Both of these represent acceptable losses. Here we will use Instances that are outlier in five or more features.

# In[22]:


numeric_log_std_sc_out_rem_df = numeric_log_std_sc_df.drop(multiple_outliers(numeric_log_std_sc_df, 5))
numeric_log_gel_sc_out_rem_df = numeric_log_gel_sc_df.drop(multiple_outliers(numeric_log_gel_sc_df, 5))


# In[23]:


(numeric_log_std_sc_out_rem_df.shape,
numeric_log_gel_sc_out_rem_df.shape)


# In[ ]:




