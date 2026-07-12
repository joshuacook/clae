#!/usr/bin/env python
# coding: utf-8

# ## Preprocessing
# 
# In the file `src/preprocessing.py`, we perform the preprocessing steps necessary for the next phase of this project. This file does the following:
# 
# 1. Load and merge data, using the `Id` feature as we did previously
# 2. Assign correct data types, in particular, designating which features are categorical
# 3. Handle missing values, using the work we did previously

# In[ ]:


run src/preprocessing.py


# ### Skew-Normalization
# 
# Next, we look at skew-normalizing our data. We have two methods that we have worked with to apply skew-normalization:
# 
# - applying a log transform
# - applying a box-cox transform
# 
# In the past, we have seen that the box-cox transform has been more performant in terms of removing skew from a dataset. With this data set, however, there is another issue.
# 

# In[ ]:


get_ipython().run_line_magic('whos', '')


# In[3]:


import scipy.stats as st


# To see this issue, let's look at the `LotArea` feature from the numeric dataset.

# In[4]:


box_cox_trans = st.boxcox(numeric_df['LotArea'] + 1)


# Note that applying a box-cox transform to this feature causes a `RunTimeWarning`. This is a known an open issue for the `scipy` library and can be tracked here: https://github.com/scipy/scipy/issues/6873. The details of the issue are complicated, but the short of it is that a floating-point arithmetic error is introduced. As such, we are not able to easily use the Box-Cox transform on this data set. We will stick to applying a log transform.

# In[5]:


numeric_log_df = np.log(numeric_df + 1)


# ### One-hot Encoding
# 
# In order to understand our categorical data from a numerical perspective, and ultimately in order to use our categorical data in a machine learning model, we need to numerically encode our categorical data.The standard way to do this is to perform a so-called "One-hot Encoding". This is also known as encoding with dummy variables. Using Pandas, it is possible to perform this encoding on properly typed data using the function `pd.get_dummies()`.

# # one-hot encoding
# 
# | id | color |
# |----|-------|
# | 1  | red   |
# | 2  | blue  |
# | 3  | green |
# | 4  | red   |
# | 5  | blue  |
# 
# unique categories: `{ red, blue, green }`
# 
# one-hot encoding will create 2 new features:
# 
# | id | color_red | color_blue |
# |----|-----------|------------|
# | 1  | 1         | 0          |
# | 2  | 0         | 1          |
# | 3  | 0         | 0          |
# | 4  | 1         | 0          |
# | 5  | 0         | 1          |
# 

# In[ ]:


categorical_df.head()


# In[ ]:


for col in categorical_df.columns[:5]:
    print(col)
    print(categorical_df[col].unique())
    print("\n")


# In[ ]:


get_ipython().run_line_magic('pinfo', 'pd.get_dummies')


# In[9]:


categorical_encoded_df = pd.get_dummies(categorical_df)


# In[ ]:


categorical_encoded_df.head()


# In[ ]:


categorical_encoded_df.shape


# In[ ]:


categorical_encoded_df.sample(5)


# Let us now consider this statistical description of an encoded categorical feature. Note that the categorical feature `MSSubClass` Has been converted it to 15 columns, one for each possible category.

# In[ ]:


categorical_encoded_df.columns


# In[ ]:


[col for col in categorical_encoded_df.columns if 'MSSubClass' in col]


# In[ ]:


ms_sub_class_encoded_cols = [col for col in categorical_encoded_df.columns if 'MSSubClass' in col]
ms_sub_class_encoded_cols


# We can use this list to filter the full categorical data frame to simply look at the encoded `MSSubClass` feature.

# In[ ]:


categorical_encoded_df[ms_sub_class_encoded_cols].head()


# Next, we take a sum for each column and over the whole filtered dataframe. Note that to sum over the whole data frame, we must request the `.values` of the DataFrame which has the effect of converting the data into a simple Numpy array. This is because the `.sum()` method in Pandas can only be performed over columns (`.sum(axis=1)`) or rows (`.sum(axis=0)`), whereas the `.sum()` method in Numpy can be performed over the entire array.

# In[ ]:


(categorical_encoded_df[ms_sub_class_encoded_cols].sum(), 
 categorical_encoded_df[ms_sub_class_encoded_cols].values.sum())


# In[ ]:


categorical_df.MSSubClass.value_counts()


# In[ ]:


categorical_encoded_df[ms_sub_class_encoded_cols].shape


# In[ ]:


1-(1460/(1460*15))


# In[ ]:


import scipy
scipy.sparse


# It is useful to think about the sparsity of the one-hot encoded data. This filtered dataframe, `categorical_encoded_df[ms_sub_class_encoded_cols]` has a shape of `(1451, 15)`, that is, 21765 datapoints, but only 1451 contain a value of 1, the rest containing a value of 0. In other words, 14 out of 15 or 93% of values in this filtered dataframe are 0.

# Next, let's look at mean and standard deviation of the filtered dataframe.

# In[ ]:


stats = pd.DataFrame()
stats['mean'] = categorical_encoded_df[ms_sub_class_encoded_cols].mean()
stats['std'] = categorical_encoded_df[ms_sub_class_encoded_cols].std()
stats['var'] = categorical_encoded_df[ms_sub_class_encoded_cols].var()
stats.sort_values('std', ascending=False)


# We note that most of the one-hot encoded columns have very little variance. In a moment, we'll restrict our analysis to one-hot encoded features that have a variance greater than 0.2. Below is a list of these features. Remember that each of these represents a Boolean variable as to whether or not each row has this particular category-attribute. 

# In[ ]:


stats = pd.DataFrame()
stats['mean'] = categorical_encoded_df.mean()
stats['std'] = categorical_encoded_df.std()
stats['var'] = categorical_encoded_df.var()
categorical_encoded_features_significant_variance_stats = stats[stats['var'] > 0.2].sort_values('std', ascending=False)
categorical_encoded_features_insignificant_variance_stats = stats[stats['var'] <= 0.2].sort_values('std', ascending=False)
categorical_encoded_features_significant_variance_stats.head(5)


# In[ ]:


categorical_encoded_features_significant_variance_stats.shape


# ### Gelman Scaling 
# 
# This data set is a mixed data set. It includes both numerical and categorical features. In his [2007 paper](http://www.stat.columbia.edu/~gelman/research/published/standardizing7.pdf), Gelman outlines a simple adjustment to the standard scaling technique we have been using that can help with mixed datasets. The standard scaling technique performs the following transformation
# 
# $$Z = \frac{X-\mu}{\sigma}$$
# 
# Gelman proposes this alternative
# 
# $$Z_g = \frac{X-\mu}{2\sigma}$$

# Here, we explore the implications of this.

# In[ ]:


numeric_log_df.shape, categorical_df.shape


# First, let's look at the statistics for data prepared by each scaling technique. For ease of viewing, we will only look at the first five features.

# In[26]:


numeric_first_five_features = numeric_log_df.columns[:5]


# In[ ]:


numeric_first_five_features


# In[28]:


from sklearn.preprocessing import StandardScaler
scaler = StandardScaler()


# In[29]:


numeric_log_std_sc_df = scaler.fit_transform(numeric_log_df)


# In[30]:


numeric_log_std_sc_df = (numeric_log_df - numeric_log_df.mean())/numeric_log_df.std()


# In[31]:


numeric_log_gel_sc_df = (numeric_log_df - numeric_log_df.mean())/(2*numeric_log_df.std())


# In[ ]:


stats = pd.DataFrame()
stats['mean'] = numeric_log_std_sc_df[numeric_first_five_features].mean()
stats['std'] = numeric_log_std_sc_df[numeric_first_five_features].std()
stats['var'] = numeric_log_std_sc_df[numeric_first_five_features].var()
stats


# In[ ]:


stats = pd.DataFrame()
stats['mean'] = numeric_log_gel_sc_df[numeric_first_five_features].mean()
stats['std'] = numeric_log_gel_sc_df[numeric_first_five_features].std()
stats['var'] = numeric_log_gel_sc_df[numeric_first_five_features].var()
stats


# Note that the diagonal of each covariance matrix signifies the variance of each feature. With standard scaling, the standard deviation $\sigma$ of a scaled feature is 1 and the variance $\sigma^2$ is also 1. With Gelman scaling, the standard deviation $\sigma$ of a scaled feature is 0.5. The variance $\sigma^2$ is 0.25. Compare this to the standard deviation and variance of the categorical features:

# In[ ]:


categorical_encoded_features_significant_variance_stats.head(5)


# Note that with Gelman scaling, we are able to directly compare one-hot encoded categorical features with significant variance to our numerical features. 
# 
# Gelman notes:
# 
# > Our procedure scales inputs to be comparable with binary variables that are roughly symmetric: if the probability falls between 0.3 and 0.7, then 2 standard deviations will be between 0.9 and 1. Highly skewed binary inputs still create difficulty in interpretation, however; for example, two standard deviations for a 90 per cent/10 per cent binary variable come to only 0.6. Thus, leaving this binary variable unscaled is not quite equivalent to dividing by two standard deviations. One might argue, however, that when considering rare subsets of the population, a full comparison from 0 to 1 could overstate the importance of the predictor in the regression, hence it might be reasonable to consider this two-standard-deviation comparison, which is less than the comparison of the extremes. Our main point, however, is that 2 standard deviations is a more reasonable scaling than 1—even if neither automatic approach solves all problems of interpretation.
# 
# Following these guidelines, we will only compare Gelman scaled numeric features and one-hot encoded categorical features with a variance above 0.2. Note that a variance of 0.2 corresponds approximately to features for whom "2 standard deviations will be between 0.9 and 1".

# In[35]:


categorical_encoded_features_significant_variance = categorical_encoded_df[categorical_encoded_features_significant_variance_stats.index]
categorical_encoded_features_insignificant_variance = categorical_encoded_df[categorical_encoded_features_insignificant_variance_stats.index]


# In[ ]:


categorical_encoded_features_significant_variance.columns


# In[ ]:


categorical_df.OverallQual.value_counts()


# In[ ]:


categorical_encoded_features_insignificant_variance.columns


# ### Centering Categorical Features with Significant Variance

# We apply one last transformation to the `categorical_encoded_features_significant_variance` dataframe. Namely, we subtract the meaning from each column. In doing this we have an apples to apples comparison between the numeric features and the categorical features with significant variance. Simply subtracting the meaning is known as centering
# 
# $$Z_c = X - \mu$$

# In[39]:


categorical_encoded_features_significant_variance_centered = (categorical_encoded_features_significant_variance - 
                                                              categorical_encoded_features_significant_variance.mean())


# This work was added to `src/preprocessing.py` as we continue.

# In[ ]:


numeric_df.shape


# In[ ]:


categorical_df.shape


# In[ ]:


categorical_encoded_features_significant_variance.shape


# In[ ]:




