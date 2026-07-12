#!/usr/bin/env python
# coding: utf-8

# ## Analysis of Variance (ANOVA)
# 
# In this notebook, we explore the Analysis of Variance (ANOVA) technique. Analysis of Variance (ANOVA) is a statistical procedure for comparing means of two or more populations. Essentially, we wish to understand whether two populations are significantly different from each other by comparing their means. 
# 
# Previously, we prepared a series of distribution plots for a single numerical feature where each distribution plot corresponds to the values for the numerical feature for a given attribute of a categorical feature. Here, we use ANOVA to evaluate statistically and what we see in those plots.

# In[1]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import scipy.stats as stats

# Import our custom functions
from src.load_data_02 import load_data, count_empty_total
from src.multiplot import multiplot, hist_with_kde, hist_with_kde_numerical_by_category

# Set plot style
plt.rcParams['figure.figsize'] = (20, 4)


# In[ ]:


# Load the data
housing_df = load_data()


# In[ ]:


housing_df.shape


# In[ ]:


housing_df.head()


# In[ ]:


count_empty_total(housing_df)


# ### One-way ANOVA
# 
# One-way ANOVA is perhaps the simplest ANOVA technique and handles a special case of this problem, testing for equal group means using a single feature. The idea is essentially this:
# 
# 1. Identify a numerical feature for analysis (often the target feature)
# 2. Split that numerical features into groups using a categorical feature
# 3. Run a one-way ANOVA on these groups
# 4. If it is found that than means are equal for all groups, then this categorical feature may be less relevant for predicting the numerical feature in question
# 5. If it is found that the means are not equal for all groups, then this categorical feature may be important for predicting the numerical feature in question

# In a one-way ANOVA, the null hypothesis is that the mean responses are equal for all groups. The alternative hypothesis is that the mean responses are not equal for all groups. It is helpful to recall that any statistical test, it is standard that if the $p$-value of the test is less than 0.05, then the null hypothesis can be rejected.
# 
# **A $p$-value greater than 0.05 does not necessarily mean that the null hypothesis should be accepted.**

# In[ ]:


# Create plots to visualize the distributions
plots = [
    hist_with_kde_numerical_by_category(housing_df['SalePrice'], housing_df['MoSold']),
    hist_with_kde_numerical_by_category(housing_df['SalePrice'], housing_df['ExterQual'])
]


# In[ ]:


fig, ax = plt.subplots(3, 4, figsize=(20, 15))

months = housing_df['MoSold'].unique()

for i, month in enumerate(months):

    j = i % 4
    k = i // 4
    sns.histplot(housing_df[housing_df['MoSold'] == month]['SalePrice'], ax=ax[k, j])
    ax[k, j].set_title(f'Month Sold: {month}')
    ax[k, j].set_xlabel('Sale Price ($)')
    ax[k, j].set_ylabel('Frequency')
    ax[k, j].set_xlim(0, 800000)
plt.tight_layout()
plt.show()


# In[ ]:


fig, ax = plt.subplots(1, 4)

exterior_qualities = housing_df['ExterQual'].unique()

for i, qual in enumerate(exterior_qualities):
    sns.histplot(housing_df[housing_df['ExterQual'] == qual]['SalePrice'], ax=ax[i])
    ax[i].set_title(f'Exterior Quality: {qual}')
    ax[i].set_xlabel('Sale Price ($)')
    ax[i].set_ylabel('Frequency')
    ax[i].set_xlim(0, 800000)
plt.tight_layout()
plt.show()


# #### Month Sold
# 
# Consider the null hypothesis:
# 
# $$H_0: \text{the mean responses are equal for all groups}$$

# In[ ]:


# Function to calculate mean and standard deviation for each group
def mean_sd(data):
    return pd.DataFrame({
        'mean': data.mean(),
        'sd': data.std()
    })

# Group by MoSold and calculate statistics
housing_df.groupby('MoSold')['SalePrice'].agg(['mean', 'std'])


# In[ ]:


# Perform one-way ANOVA
groups = [
    housing_df[housing_df['MoSold'] == month]['SalePrice'].values 
    for month in housing_df['MoSold'].unique()
]

f_stat, p_value = stats.f_oneway(*groups)

print(f"F-statistic: {f_stat:.4f}")
print(f"p-value: {p_value:.4f}")
print(f"Reject null hypothesis: {p_value < 0.05}")


# ##### This test shows that we CAN NOT reject the null hypothesis

# #### Exterior Quality
# 
# Consider the null hypothesis:
# 
# $$H_0: \text{the mean responses are equal for all groups}$$

# In[ ]:


# Group by ExterQual and calculate statistics
housing_df.groupby('ExterQual')['SalePrice'].agg(['mean', 'std'])


# In[ ]:


# Perform one-way ANOVA
groups = [
    housing_df[housing_df['ExterQual'] == qual]['SalePrice'].values 
    for qual in housing_df['ExterQual'].unique()
]

f_stat, p_value = stats.f_oneway(*groups)
print(f"F-statistic: {f_stat:.4f}")
print(f"p-value: {p_value:.10f}")
print(f"Reject null hypothesis: {p_value < 0.05}")


# ##### This test shows that we CAN reject the null hypothesis

# In[ ]:




