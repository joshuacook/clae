#!/usr/bin/env python
# coding: utf-8

# # Benchmark Model for Ames Housing Dataset
# 
# ## Introduction
# 
# Before developing complex models, it's important to establish a simple benchmark. This gives us a baseline performance to compare against and helps us understand if our more sophisticated models are actually providing value.
# 
# In this notebook, we'll create a very simple benchmark model for predicting house prices in Ames, Iowa. The simplest possible model is to predict that every house costs the same amount - specifically, the mean sale price of all houses in our dataset.

# In[1]:


# Load our preprocessed data
run src/preprocessing.py


# In[2]:


# Check the shape of our dataset to confirm it loaded correctly
print(f"Dataset 4 shape: {dataset_4.shape}")


# In[3]:


# Install tqdm for progress bars if needed
try:
    get_ipython().system('pip install tqdm --quiet')
except (NameError, AttributeError):
    # Not in notebook environment
    pass


# In[4]:


# Import necessary libraries
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns
from sklearn.metrics import r2_score, mean_squared_error, mean_absolute_error


# In[5]:


# Visualize the distribution of our target variable (house prices)
plt.figure(figsize=(20,6))
sns.histplot(target_1, kde=True)
plt.title('Distribution of House Prices in Ames, Iowa', fontsize=16)
plt.xlabel('Sale Price ($)', fontsize=14)
plt.ylabel('Frequency', fontsize=14)
plt.axvline(target_1.mean(), color='red', linestyle='--', 
            label=f'Mean: ${target_1.mean():.2f}')
plt.axvline(target_1.median(), color='green', linestyle='--', 
            label=f'Median: ${target_1.median():.2f}')
plt.legend(fontsize=12)
plt.show()


# ## Naive Benchmark Model
# 
# Our benchmark model will simply predict the mean sale price for every house. This is the simplest possible model and requires no features.
# 
# ### Fundamental Question: How much does a home in Ames, Iowa sell for?

# In[6]:


# Calculate the mean sale price
mean_sale_price = target_1.mean()
print(f"Mean sale price: ${mean_sale_price:.2f}")

# Create predictions using the mean for every house
naive_guess = np.ones(len(target_1)) * mean_sale_price
print(f"Example predictions: ${naive_guess[:5]}")


# ## Evaluating the Benchmark Model
# 
# We'll evaluate our naive benchmark using three common metrics:
# 
# 1. **R² Score**: Measures the proportion of variance in the target that is predictable from the features
# 2. **Root Mean Squared Error (RMSE)**: Measures the average magnitude of errors in predictions
# 3. **Mean Absolute Error (MAE)**: Measures the average absolute difference between predictions and actual values

# In[7]:


# Calculate R² score
r2 = r2_score(target_1, naive_guess)
print(f"R² Score: {r2:.4f}")

# Calculate RMSE
rmse = np.sqrt(mean_squared_error(target_1, naive_guess))
print(f"Root Mean Squared Error: ${rmse:.2f}")

# Calculate MAE
mae = mean_absolute_error(target_1, naive_guess)
print(f"Mean Absolute Error: ${mae:.2f}")


# ## Interpretation of Results
# 
# - **R² Score**: The R² score of 0 indicates that our model doesn't explain any of the variance in house prices. This is expected for a naive model that always predicts the mean.
# 
# - **RMSE**: The RMSE tells us that, on average, our predictions are off by about ${rmse:.2f}. This is a substantial error considering the mean house price.
# 
# - **MAE**: The MAE indicates that, on average, our predictions differ from the actual prices by ${mae:.2f}.
# 
# These metrics provide a baseline against which we can compare our more sophisticated models. Any model we develop should perform significantly better than this naive benchmark to be considered useful.
# 
# In the next notebooks, we'll develop more complex models using the features we've engineered and compare their performance to this benchmark.

# In[ ]:



