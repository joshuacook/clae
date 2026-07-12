#!/usr/bin/env python
# coding: utf-8

# # Principal Component Analysis (PCA)
# 
# ## Introduction to PCA
# 
# Principal Component Analysis (PCA) is a dimensionality reduction technique that transforms a dataset with potentially correlated variables into a set of linearly uncorrelated variables called principal components. These principal components are ordered so that the first component captures the most variance in the data, the second component captures the second most variance, and so on.
# 
# ### Key concepts of PCA:
# 
# 1. **Dimensionality Reduction**: PCA reduces the number of features while preserving as much information (variance) as possible.
# 
# 2. **Principal Components**: These are new variables that are linear combinations of the original variables. They are orthogonal to each other (uncorrelated).
# 
# 3. **Variance Explained**: Each principal component explains a certain percentage of the total variance in the data.
# 
# 4. **Eigenvalues and Eigenvectors**: PCA is mathematically based on the eigenvector decomposition of the covariance matrix of the data.
# 
# ### Why use PCA?
# 
# - **Reduce dimensionality**: Simplify models by reducing the number of features
# - **Remove multicollinearity**: Create uncorrelated features
# - **Visualize high-dimensional data**: Project data onto 2D or 3D space
# - **Noise reduction**: Lower-ranked components often capture noise
# - **Feature extraction**: Create new meaningful features

# In[1]:


import matplotlib.pyplot as plt
# Import seaborn for visualization if needed later
import numpy as np
import pandas as pd
from IPython.display import display
from sklearn.decomposition import PCA


# In[ ]:


# Load preprocessed data from our preprocessing script
# This includes:
# - Data loading and merging
# - Handling missing values
# - Log transformation of numeric features
# - Scaling (both standard and Gelman scaling)
# - One-hot encoding of categorical features
# - Outlier removal
try:
    # Try to use IPython magic if in notebook environment
    get_ipython().run_line_magic('run', 'src/preprocessing.py')
except (NameError, AttributeError):
    # If not in notebook environment, import directly
    import sys
    import os
    sys.path.append(os.path.join(os.path.dirname(__file__), 'src'))
    from preprocessing import *


# ## Dataset Organization
# 
# Before we proceed with PCA, let's understand the different datasets we've created through our preprocessing steps:
# 
# ### Dataset 1 - Standard Scaled Data Set
# 
# One data set is the standard scaled data set. For this data set, there is no need to separate the encoded categorical features. These two dataframes comprise a complete data set:
# 
# - Log Transformed, Standard Scaled Numerical Features (`numeric_log_std_sc_out_rem_df`)
# - Complete One-hot Encoded Categorical Features (`categorical_encoded_df`)
# 
# ### Dataset 2 - Standard Scaled, PCA Augmented Data Set
# 
# One data set is the standard scaled data set, augmented with transformed data from a PCA Run on the numeric features. We know that there is significant redundancy in this data set. These three dataframes comprise a complete data set:
# 
# - Log Transformed, Standard Scaled Numerical Features (`numeric_log_std_sc_out_rem_df`)
# - Complete One-hot Encoded Categorical Features (`categorical_encoded_df`)
# - PCA-transformed Numeric Data (`numeric_log_std_sc_out_rem_pca_df`) - we'll create this in this notebook
# 
# ### Dataset 3 - Gelman Scaled Data Set
# 
# Another data set is the Gelman scaled data set. For this data set, we have separated the encoded categorical features based on a threshold for variance. These three dataframes comprise a complete data set:
# 
# - Log Transformed, Gelman Scaled Numerical Features (`numeric_log_gel_sc_out_rem_df`)
# - One-hot Encoded Categorical Features with Significant Variance, Centered (`categorical_encoded_features_significant_variance_centered_out_rem`)
# - One-hot Encoded Categorical Features with Insignificant Variance (`categorical_encoded_features_insignificant_variance`)
# 
# ### Dataset 4 - Gelman Scaled, PCA Augmented Data Set
# 
# Our final data set is the Gelman scaled data set, augmented with transformed data from a PCA Run on the numeric features and categorical features with significant variance. This Data sets also has significant redundancy. These dataframes comprise a complete data set:
# 
# - Log Transformed, Gelman Scaled Numerical Features (`numeric_log_gel_sc_out_rem_df`)
# - One-hot Encoded Categorical Features with Significant Variance, Centered (`categorical_encoded_features_significant_variance_centered_out_rem`)
# - One-hot Encoded Categorical Features with Insignificant Variance (`categorical_encoded_features_insignificant_variance`)
# - PCA-transformed Numeric and Significant Categorical (`numeric_gelman_categorical_significant_pca`) - we'll create this in this notebook


# In[ ]:


# Inspect the pandas merge function documentation
try:
    get_ipython().run_line_magic('pinfo', 'pd.merge')
except (NameError, AttributeError):
    # Skip if not in notebook environment
    pass


# In[ ]:


# Check the index of our Gelman scaled numeric features dataframe
# This will be important for merging datasets later
try:
    print("Gelman scaled numeric features index:", numeric_log_gel_sc_out_rem_df.index[:5], "...")
except (NameError, AttributeError):
    pass


# In[ ]:


# Display the first few rows of our preprocessed datasets to understand their structure
print("Numeric features (log-transformed, Gelman-scaled, outliers removed):")
try:
    display(numeric_log_gel_sc_out_rem_df.head())
except (NameError, AttributeError):
    print("Dataset not available in this environment")
print("\nCategorical features with significant variance (centered, outliers removed):")
try:
    display(categorical_encoded_features_significant_variance_centered_out_rem.head())
except (NameError, AttributeError):
    print("Dataset not available in this environment")


# In[6]:


# Merge numeric features with categorical features that have significant variance
# This combined dataset will be used for one of our PCA analyses
try:
    numeric_gelman_categorical_significant = pd.merge(
        numeric_log_gel_sc_out_rem_df, 
        categorical_encoded_features_significant_variance_centered_out_rem,
        left_index=True,
        right_index=True
    )
except (NameError, AttributeError):
    # Create a placeholder if not in the right environment
    print("Creating placeholder for merged dataset")
    numeric_gelman_categorical_significant = pd.DataFrame()


# In[ ]:

# Create three different PCA models for different datasets:
# 1. For standard scaled numeric features
pca_log_std_sc_out_rem = PCA() # just numeric features, conditioned on the standard scaled data

# 2. For Gelman scaled numeric features
pca_log_gel_sc_out_rem = PCA() # just numeric features, conditioned on the gelman scaled data

# 3. For combined numeric and categorical features (with Gelman scaling)
pca_num_gel_cat = PCA() # numeric and significant categorical features, conditioned on the gelman scaled data and categorical features with significant variance

# Fit each PCA model to its respective dataset
try:
    pca_log_std_sc_out_rem.fit(numeric_log_std_sc_out_rem_df)
    pca_log_gel_sc_out_rem.fit(numeric_log_gel_sc_out_rem_df)
    pca_num_gel_cat.fit(numeric_gelman_categorical_significant)
except (NameError, AttributeError):
    print("Unable to fit PCA models - datasets not available")


# In[ ]:


# Visualize the explained variance ratio for each principal component
# This shows how much variance each component explains
try:
    fig, ax = plt.subplots(1, 2, figsize=(20,5))

    # Left plot: Individual explained variance for each component
    ax[0].plot(pca_log_std_sc_out_rem.explained_variance_ratio_, label='Standard Scaled Numeric')
    ax[0].plot(pca_log_gel_sc_out_rem.explained_variance_ratio_, label='Gelman Scaled Numeric', linestyle='--')
    ax[0].plot(pca_num_gel_cat.explained_variance_ratio_, label='Gelman Scaled Numeric + Significant Categorical')
    ax[0].set_title('Explained Variance Ratio by Component')
    ax[0].set_xlabel('Principal Component Index')
    ax[0].set_ylabel('Explained Variance Ratio')
    ax[0].legend()

    # Right plot: Cumulative explained variance
    ax[1].plot(np.cumsum(pca_log_std_sc_out_rem.explained_variance_ratio_), label='Standard Scaled Numeric')
    ax[1].plot(np.cumsum(pca_log_gel_sc_out_rem.explained_variance_ratio_), label='Gelman Scaled Numeric', linestyle='--')
    ax[1].plot(np.cumsum(pca_num_gel_cat.explained_variance_ratio_), label='Gelman Scaled Numeric + Significant Categorical')
    ax[1].set_title('Cumulative Explained Variance')
    ax[1].set_xlabel('Number of Components')
    ax[1].set_ylabel('Cumulative Explained Variance')
    ax[1].legend()

    # The cumulative plot helps us determine how many components to keep
    # A common rule is to keep enough components to explain 80-90% of variance
except (NameError, AttributeError):
    print("Unable to create plots - PCA models not fitted")


# In[ ]:


# Focus on the first 10 components for a closer look
plt.figure(figsize=(20,5))
plt.plot(pca_log_std_sc_out_rem.explained_variance_ratio_[:10], label='Standard Scaled Numeric')
plt.plot(pca_log_gel_sc_out_rem.explained_variance_ratio_[:10], label='Gelman Scaled Numeric')
plt.plot(pca_num_gel_cat.explained_variance_ratio_[:10], label='Gelman Scaled Numeric + Significant Categorical')
plt.title('Explained Variance Ratio for First 10 Components')
plt.xlabel('Principal Component Index')
plt.ylabel('Explained Variance Ratio')
plt.legend()

# Based on the plots, we can see that the first few components explain most of the variance
# This suggests we can reduce dimensionality significantly while retaining most information


# In[ ]:


# Based on our analysis, we'll keep 8 components for each PCA model
# This is a hyperparameter we can tune based on how much variance we want to retain
pca_log_std_sc_out_rem = PCA(8)  # Keep 8 components for standard scaled data
pca_log_gel_sc_out_rem = PCA(8)  # Keep 8 components for Gelman scaled data
pca_num_gel_cat = PCA(8)         # Keep 8 components for combined data

# Refit the PCA models with the specified number of components
try:
    pca_log_std_sc_out_rem.fit(numeric_log_std_sc_out_rem_df)
    pca_log_gel_sc_out_rem.fit(numeric_log_gel_sc_out_rem_df)
    pca_num_gel_cat.fit(numeric_gelman_categorical_significant)
except (NameError, AttributeError):
    print("Unable to refit PCA models - datasets not available")


# In[11]:


# Store the explained variance ratios for each PCA model
# These represent how much variance each principal component explains
L_log_std_sc_out_rem = pca_log_std_sc_out_rem.explained_variance_ratio_
L_log_gel_sc_out_rem = pca_log_gel_sc_out_rem.explained_variance_ratio_
L_num_gel_cat = pca_num_gel_cat.explained_variance_ratio_


# In[12]:


# Create DataFrames of the principal components (loadings)
# These show how each original feature contributes to each principal component
try:
    P_log_std_sc_out_rem = pd.DataFrame(pca_log_std_sc_out_rem.components_, columns=numeric_log_std_sc_out_rem_df.columns)
    P_log_gel_sc_out_rem = pd.DataFrame(pca_log_gel_sc_out_rem.components_, columns=numeric_log_gel_sc_out_rem_df.columns)
    P_num_gel_cat = pd.DataFrame(pca_num_gel_cat.components_, columns=numeric_gelman_categorical_significant.columns)
except (NameError, AttributeError):
    print("Unable to create component DataFrames - datasets not available")
    # Create empty DataFrames as placeholders
    P_log_std_sc_out_rem = pd.DataFrame()
    P_log_gel_sc_out_rem = pd.DataFrame()
    P_num_gel_cat = pd.DataFrame()

# The components_ attribute contains the principal components (eigenvectors)
# Each row represents a principal component, and each column represents the contribution
# of the original feature to that component


# In[ ]:


# Visualize the principal components (loadings) for each PCA model
# This shows how each original feature contributes to each principal component
_, ax = plt.subplots(3,1,figsize=(20,20))

# Plot loadings for standard scaled numeric data
P_log_std_sc_out_rem.plot(kind='bar', rot=0, title="Standard Scaled Numeric Features - Principal Components", ax=ax[0])

# Plot loadings for Gelman scaled numeric data 
P_log_gel_sc_out_rem.plot(kind='bar', rot=0, title="Gelman Scaled Numeric Features - Principal Components", ax=ax[1])

# Plot loadings for combined numeric and categorical data
P_num_gel_cat.plot(kind='bar', rot=0, title="Gelman Scaled Numeric + Categorical Features - Principal Components", ax=ax[2])

# Adjust legends
ax[0].legend(loc='center left', bbox_to_anchor=(1, 0.5), mode='expand')
ax[1].legend(loc='center left', bbox_to_anchor=(1, 0.5), mode='expand')
ax[2].legend(loc='center left', bbox_to_anchor=(1, 0.5), ncol=3)

# Add explained variance to x-axis labels
ax[0].set_xticklabels(['PC ' + str(i+1) +' // ' + str(round(ratio,2)) for i, ratio in enumerate(L_log_std_sc_out_rem)])
ax[1].set_xticklabels(['PC ' + str(i+1) +' // ' + str(round(ratio,2)) for i, ratio in enumerate(L_log_gel_sc_out_rem)])
ax[2].set_xticklabels(['PC ' + str(i+1) +' // ' + str(round(ratio,2)) for i, ratio in enumerate(L_num_gel_cat)])

# Interpretation: 
# - Bars represent the weight (loading) of each original feature in the principal component
# - Larger bars (positive or negative) indicate features that strongly influence that component
# - Features with the same sign (all positive or all negative) are positively correlated in that component
# - Features with opposite signs are negatively correlated in that component
# - The number after each PC shows the proportion of variance explained by that component


# In[14]:


# Create a DataFrame with absolute values of loadings to identify most important features
P_num_gel_cat_abs = P_num_gel_cat.abs()

# Function to find the top 20 features with highest absolute loadings for a given PC
def top_20_features_by_PC_abs(pc_num):
    """
    Returns the top 20 features with highest absolute contribution to a principal component
    
    Parameters:
    pc_num (int): The index of the principal component to analyze
    
    Returns:
    pandas.Series: Top 20 features and their loadings for the specified PC
    """
    # Sort features by their absolute loading values
    PC_0_abs_sorted_index = P_num_gel_cat_abs.T.sort_values(pc_num, ascending=False).index
    # Return the actual (not absolute) loadings of the top 20 features
    return P_num_gel_cat[PC_0_abs_sorted_index].T[pc_num].head(20)


# In[ ]:


# Examine the top 20 features for the first principal component (PC 0)
print("Top 20 features contributing to Principal Component 1:")
top_20_features_by_PC_abs(0)

# Interpretation:
# - These features have the strongest influence on PC1
# - Features with large positive values are positively correlated with PC1
# - Features with large negative values are negatively correlated with PC1
# - PC1 explains the largest portion of variance in our dataset


# In[ ]:


# Examine the top 20 features for the second principal component (PC 1)
print("Top 20 features contributing to Principal Component 2:")
top_20_features_by_PC_abs(1)

# Interpretation:
# - PC2 captures the second largest portion of variance
# - These features are important for PC2 but were not necessarily important for PC1
# - PC2 is orthogonal (uncorrelated) to PC1, so it captures different aspects of the data


# In[ ]:


# Examine the top 20 features for the third principal component (PC 2)
print("Top 20 features contributing to Principal Component 3:")
top_20_features_by_PC_abs(2)

# Interpretation:
# - PC3 captures even more subtle patterns in the data
# - By examining the top features across multiple PCs, we can understand
#   different aspects of what makes houses in Ames, Iowa different from each other


# In[18]:


# Transform our original data into the PCA space
# This creates new datasets with principal components as features

try:
    # Transform standard scaled numeric data
    numeric_log_std_sc_out_rem_pca_df = pd.DataFrame(
        pca_log_std_sc_out_rem.transform(numeric_log_std_sc_out_rem_df),
        columns=['PC 1', 'PC 2', 'PC 3', 'PC 4', 'PC 5', 'PC 6', 'PC 7', 'PC 8']
    )

    # Transform combined numeric and categorical data
    numeric_gelman_categorical_significant_pca = pd.DataFrame(
        pca_num_gel_cat.transform(numeric_gelman_categorical_significant),
        columns=['PC 1', 'PC 2', 'PC 3', 'PC 4', 'PC 5', 'PC 6', 'PC 7', 'PC 8']
    )
except (NameError, AttributeError):
    print("Unable to transform data - PCA models or datasets not available")
    # Create empty DataFrames as placeholders
    numeric_log_std_sc_out_rem_pca_df = pd.DataFrame()
    numeric_gelman_categorical_significant_pca = pd.DataFrame()

# These transformed datasets can now be used for modeling
# Each row corresponds to the same house as in the original data
# But now represented in terms of principal components instead of original features


# Now that we have our PCA-transformed data, we can create our complete datasets
# These will be used in subsequent analyses

try:
    # Create Dataset 1: Standard Scaled Data Set
    dataset_1 = pd.merge(categorical_encoded_df, numeric_log_std_sc_out_rem_df, 
                         left_index=True, right_index=True)

    # Create Dataset 2: Standard Scaled, PCA Augmented Data Set
    dataset_2 = pd.merge(dataset_1, numeric_log_std_sc_out_rem_pca_df, 
                         left_index=True, right_index=True)

    # Create Dataset 3: Gelman Scaled Data Set
    dataset_3 = pd.merge(numeric_log_gel_sc_out_rem_df, 
                         categorical_encoded_features_significant_variance_centered, 
                         left_index=True, right_index=True)
    dataset_3 = pd.merge(dataset_3, categorical_encoded_features_insignificant_variance, 
                         left_index=True, right_index=True)

    # Create Dataset 4: Gelman Scaled, PCA Augmented Data Set
    dataset_4 = pd.merge(dataset_3, numeric_gelman_categorical_significant_pca, 
                         left_index=True, right_index=True)
except (NameError, AttributeError):
    print("Unable to create merged datasets - component datasets not available")
    # Create empty DataFrames as placeholders
    dataset_1 = pd.DataFrame()
    dataset_2 = pd.DataFrame()
    dataset_3 = pd.DataFrame()
    dataset_4 = pd.DataFrame()

# These datasets represent different approaches to feature engineering
# In subsequent notebooks, we'll evaluate which approach works best for modeling


# In[ ]:


# Check for any null values in our datasets
# This is an important quality check before proceeding to modeling
null_counts = (
    dataset_1.isnull().sum().sum(),
    dataset_2.isnull().sum().sum(),
    dataset_3.isnull().sum().sum(),
    dataset_4.isnull().sum().sum()
)

print("Null value counts in each dataset:")
print(f"Dataset 1: {null_counts[0]} null values")
print(f"Dataset 2: {null_counts[1]} null values")
print(f"Dataset 3: {null_counts[2]} null values")
print(f"Dataset 4: {null_counts[3]} null values")


# In[ ]:


# Check the dimensions of each dataset
# This helps us understand how many features we have in each approach
shapes = (
    dataset_1.shape,
    dataset_2.shape,
    dataset_3.shape,
    dataset_4.shape
)

print("Dataset dimensions (rows, columns):")
print(f"Dataset 1: {shapes[0]}")
print(f"Dataset 2: {shapes[1]}")
print(f"Dataset 3: {shapes[2]}")
print(f"Dataset 4: {shapes[3]}")

# Note how Dataset 2 and Dataset 4 have 8 additional columns
# These are the principal components we added through PCA


# ## Summary of PCA Analysis
# 
# In this notebook, we've:
# 
# 1. **Applied PCA** to different versions of our preprocessed data
# 2. **Analyzed the variance explained** by each principal component
# 3. **Examined the loadings** to understand which features contribute most to each component
# 4. **Created transformed datasets** with principal components as features
# 5. **Prepared four different datasets** for subsequent modeling
# 
# The PCA analysis has revealed underlying patterns in our housing data and allowed us to:
# 
# - Reduce dimensionality while preserving most of the information
# - Create uncorrelated features that may improve model performance
# - Identify which original features contribute most to the variance in the data
# 
# In the next notebooks, we'll use these datasets to build and evaluate predictive models.


# In[ ]:




