#!/usr/bin/env python
# coding: utf-8

# ## Basic EDA

# In this notebook, we perform basic data analysis for our dataset. This mostly consists of preparing distribution plots for the numerical features. We also begin to explore the technique of preparing distribution plots for numerical features separated by a categorical feature.

# In[1]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Import our custom functions
from src.load_data_02 import load_data, count_empty_total
from src.multiplot import multiplot, hist_with_kde, hist_with_kde_numerical_by_category

plt.rcParams['figure.figsize'] = (20, 4)


# In[ ]:


# Load the data
housing_df = load_data()


# To get to this point, we have done ETL (Extract, Transform, Load).
# 
# Data Engineering is the process of preparing data for analysis.

# In[ ]:


housing_df.shape


# In[ ]:


housing_df.head()


# In[ ]:


count_empty_total(housing_df)


# In[ ]:


# Get information about numeric columns
housing_df.select_dtypes(include=['number']).info()


# In[ ]:


# Get list of numeric column names
numeric_columns = housing_df.select_dtypes(include=['number']).columns.tolist()
numeric_columns


# ### Histogram of Target Feature

# Here, we display a histogram of the target feature `SalePrice`. We have also included a kernel density estimation (KDE) and the mean and median values plotted as vertical lines. The mean greater than the median signifies a right or positive skew, common with strictly non-negative data.

# In[ ]:


housing_df.head()


# In[ ]:


hist_with_kde(housing_df['SalePrice'])


# #### Plot some Histograms with KDE Plots for other Numerical Features

# Next we plot histograms with KDE plots for some of the other numerical features in our dataset.

# In[ ]:


numeric_columns


# In[ ]:


fig, ax = plt.subplots(1, 4, figsize=(20, 5))

features = ['LotFrontage', 'LotArea', '1stFlrSF', '2ndFlrSF']
for i, feature in enumerate(features):
    ax[i].set_title(feature)
    sns.histplot(housing_df[feature], kde=True, ax=ax[i])
    ax[i].axvline(housing_df[feature].mean(), color='blue', linestyle='dashed', linewidth=1, label=f'Mean: {housing_df[feature].mean():.2f}')
    ax[i].axvline(housing_df[feature].median(), color='red', linestyle='dashed', linewidth=1, label=f'Median: {housing_df[feature].median():.2f}')
    ax[i].legend()


# In[ ]:


fig, ax = plt.subplots(1, 4, figsize=(20, 5))

features = ['PoolArea', 'YrSold', 'GarageArea', 'LowQualFinSF']
for i, feature in enumerate(features):
    ax[i].set_title(feature)
    sns.histplot(housing_df[feature], kde=True, ax=ax[i])
    ax[i].axvline(housing_df[feature].mean(), color='blue', linestyle='dashed', linewidth=1, label=f'Mean: {housing_df[feature].mean():.2f}')
    ax[i].axvline(housing_df[feature].median(), color='red', linestyle='dashed', linewidth=1, label=f'Median: {housing_df[feature].median():.2f}')
    ax[i].legend()


# PCA is the eigenvector decomposition of the covariance matrix (Gramiam matrix X^T X) of the data.

# ## Correlation

# Assessing correlation in a data set with mixed numerical and categorical features can be challenging. One way to perform such an analysis is to prepare a series of distribution plots for a single numerical feature each distribution plot corresponds to the values for the numerical feature for a given attribute of a categorical feature.
# 
# Here is a list of our categorical features:
# 
# | | | |
# |:-:|:-:|:-:|
# | `Alley`         | `ExterCond`     | `GarageType`    | `MSSubClass`    |        
# | `BedroomAbvGr`  | `Exterior1st`   | `HalfBath`      | `MSZoning`      |                         
# | `BldgType`      | `Exterior2nd`   | `Heating`       | `Neighborhood`  |                          
# | `BsmtCond`      | `ExterQual`     | `HeatingQC`     | `OverallCond`   |                         
# | `BsmtExposure`  | `Fence`         | `HouseStyle`    | `OverallQual`   |                             
# | `BsmtFinType1`  | `FireplaceQu`   | `KitchenAbvGr`  | `PavedDrive`    |                           
# | `BsmtFinType2`  | `Fireplaces`    | `KitchenQual`   | `PoolQC`        |                      
# | `BsmtFullBath`  | `Foundation`    | `LandContour`   | `RoofMatl`      |                         
# | `BsmtHalfBath`  | `FullBath`      | `LandSlope`     | `RoofStyle`     |                          
# | `BsmtQual`      | `Functional`    | `LotConfig`     | `SaleCondition` |                          
# | `CentralAir`    | `GarageCars`    | `LotShape`      | `SaleType`      |                      
# | `Condition1`    | `GarageCond`    | `MasVnrType`    | `Street`        |                      
# | `Condition2`    | `GarageFinish`  | `MiscFeature`   | `TotRmsAbvGrd`  |                           
# | `Electrical`    | `GarageQual`    | `MoSold`        | `Utilities`     |    

# We can begin by looking at the distribution of `SalePrice` disaggregated by any one of these categorical features.

# In[ ]:


hist_with_kde_numerical_by_category(housing_df['SalePrice'], housing_df['BldgType'])


# It may even make sense to treat one of the numerical features as a categorical feature, for example, `YrSold`.

# In[ ]:


hist_with_kde(housing_df['SalePrice'])


# In[ ]:


# Convert YrSold to category for this analysis
hist_with_kde_numerical_by_category(housing_df['SalePrice'], housing_df['YrSold'].astype('category'))


# This plot shows that, for this dataset, the year of the sale has nearly no impact on the `SalePrice`. Note that `SalePrice` has a nearly identical distribution for all five years in the dataset.

# In[ ]:


# Create multiple plots to compare different categorical features
fig, axes = plt.subplots(1, 4, figsize=(20, 5))

# Plot SalePrice by HouseStyle
sns.histplot(data=housing_df, x='SalePrice', hue='HouseStyle', kde=True, alpha=0.4, ax=axes[0])
axes[0].set_title('SalePrice by HouseStyle')

# Plot SalePrice by ExterQual
sns.histplot(data=housing_df, x='SalePrice', hue='ExterQual', kde=True, alpha=0.4, ax=axes[1])
axes[1].set_title('SalePrice by ExterQual')

# Plot SalePrice by Street
sns.histplot(data=housing_df, x='SalePrice', hue='Street', kde=True, alpha=0.4, ax=axes[2])
axes[2].set_title('SalePrice by Street')

# Plot SalePrice by MoSold
sns.histplot(data=housing_df, x='SalePrice', hue='MoSold', kde=True, alpha=0.4, ax=axes[3])
axes[3].set_title('SalePrice by MoSold')

plt.tight_layout()


# Here, we see that `HouseStyle`, `ExterQual`, and `Street` all have some impact on `SalePrice`, while `MoSold` does not.

# Another way to analyze the influence of a categorical feature it is to create a scatter plot of two numerical features, colored by a categorical feature.

# In[ ]:


plt.figure(figsize=(12, 8))
sns.scatterplot(data=housing_df, x='GrLivArea', y='SalePrice', hue='MSSubClass', alpha=0.3)
plt.title('Sale Price vs. Living Area by Building Class')
plt.xlabel('Above Ground Living Area (square feet)')
plt.ylabel('Sale Price ($)')


# In[ ]:


# Create a scatter plot of SalePrice vs. GrLivArea, colored by MSSubClass
plt.figure(figsize=(12, 8))
sns.scatterplot(data=housing_df, x='GrLivArea', y='SalePrice', hue='MSSubClass', alpha=0.3)
plt.title('Sale Price vs. Living Area by Building Class')
plt.xlabel('Above Ground Living Area (square feet)')
plt.ylabel('Sale Price ($)')
plt.show()


# In[ ]:




