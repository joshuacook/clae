#!/usr/bin/env python
# coding: utf-8

# ## Redundancy and Correlation
# 
# In preparation for a principal component analysis, we look at redundancy and correlation in our dataset. In this analysis, we will focus on the numeric features.

# In[1]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.tree import DecisionTreeRegressor
from sklearn.model_selection import train_test_split

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


# In[6]:


# Get numeric features
numeric_df = housing_df.select_dtypes(include=['number']).copy()
numeric_features = numeric_df.columns.tolist()


# In[7]:


# Remove SalePrice from features for redundancy analysis
numeric_df = numeric_df.drop('SalePrice', axis=1)
numeric_features = numeric_df.columns.tolist()


# ### Redundancy
# 
# Here, we use machine learning to assess redundancy in our dataset. We iterate through each numeric feature in our dataset. For each feature, we drop the feature from our input/feature set $X$ and use it as our target $y$ for the training of a supervised regression model. In this case, we use a decision tree regressor.
# 
# In other words, we are training a regression model where we use the remaining features to predict each individual feature. We will thus have an $R^2$ score for each numeric feature. We use the `DecisionTreeRegressor` from scikit-learn, which is the Python equivalent of the `rpart` function in R.
# 
# Note that we also use machine learning best practices and perform a train-test split on our data. Each model is trained using the training data and assessed using the testing data. In this way, each model tells us if, upon removing a feature, the remaining features are able to predict the removed feature. If the remaining features are able to make this prediction, we may take the removed feature to be somewhat redundant. It is worth clarifying that this is an exploratory data analysis technique, and is not intended to be used at this time as a technique for removing features. We simply wish to understand the relationships within our data.

# In[8]:


def calculate_r_2(actual, prediction):
    """Calculate R^2 score manually"""
    ss_total = np.sum((actual - np.mean(actual)) ** 2)
    ss_residual = np.sum((actual - prediction) ** 2)
    return 1 - (ss_residual / ss_total)

def calculate_r_2_for_feature(data, feature):
    """Calculate R^2 for predicting a feature from all other features"""
    # Create X (all features except the target) and y (the target feature)
    X = data.drop(feature, axis=1)
    y = data[feature]
    
    # Split data into train and test sets
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)
    
    # Train a decision tree regressor
    model = DecisionTreeRegressor()
    model.fit(X_train, y_train)
    
    # Make predictions and calculate R^2
    predictions = model.predict(X_test)
    return calculate_r_2(y_test, predictions)

def mean_r2_for_feature(data, feature, n_iterations=10):
    """Calculate mean R^2 over multiple iterations"""
    scores = []
    for i in range(n_iterations):
        scores.append(calculate_r_2_for_feature(data, feature))
    return np.mean(scores)


# In[ ]:


# Test the function on one feature
calculate_r_2_for_feature(numeric_df, 'LotFrontage')


# In[ ]:


# Calculate R^2 for each feature
for feature in numeric_features:
    r2 = mean_r2_for_feature(numeric_df, feature)
    print(f"{feature}: {r2:.4f}")


# ### Correlation
# 
# Next, we assess correlation between our features. Correlation is a function of covariance data, which is itself a measure of linear relationships within data. In the previous section, we used a decision tree to assess redundancy. A decision tree is an information-based (non-linear) analysis. By performing this analysis using two different techniques, one linear and one non-linear, we have a more robust assessment of the underlying relationships in our data. Again, this technique is exploratory data analysis and is not intended at this time to remove features from our dataset.

# In[ ]:


# Calculate correlation matrix
corr_matrix = numeric_df.corr()
corr_matrix.round(3)


# In[ ]:


# Create a heatmap of the correlation matrix
plt.figure(figsize=(16, 12))

# Create a mask for the upper triangle
mask = np.triu(np.ones_like(corr_matrix, dtype=bool))

# Generate a custom diverging colormap
cmap = sns.diverging_palette(230, 20, as_cmap=True)

# Draw the heatmap with the mask and correct aspect ratio
sns.heatmap(corr_matrix, mask=mask, cmap=cmap, vmax=1, vmin=-1, center=0,
            square=True, linewidths=.5, cbar_kws={"shrink": .5})

plt.title('Feature Correlation Matrix', fontsize=16)
plt.tight_layout()


# In[ ]:




