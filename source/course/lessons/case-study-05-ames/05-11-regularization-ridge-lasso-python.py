#!/usr/bin/env python
# coding: utf-8

# # Regularization: Ridge and Lasso Regression
# 
# ## Introduction
# 
# In our previous notebooks, we've explored the Ames housing dataset, performed data preprocessing, applied principal component analysis, and examined cross-validation techniques. We've also learned about the mathematics behind linear models and gradient descent. Now, we'll focus on regularization techniques that help prevent overfitting and improve model generalization.
# 
# This notebook covers:
# 1. The theory behind regularization
# 2. Ridge regression (L2 regularization)
# 3. Lasso regression (L1 regularization)
# 4. Elastic Net (combined L1 and L2 regularization)
# 5. Visualization of regularization effects
# 6. Hyperparameter tuning with grid search
# 
# Regularization is particularly important for our Ames housing dataset because:
# - We have many features (high dimensionality)
# - Some features may be correlated (multicollinearity)
# - We want to build models that generalize well to new data

# In[1]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.linear_model import Ridge, Lasso
# GridSearchCV already imported at the top
from cycler import cycler
from matplotlib.patches import Patch
import warnings

# Suppress warnings
warnings.filterwarnings('ignore')

# For notebook environment only
try:
    get_ipython().run_line_magic('matplotlib', 'inline')
    from ipywidgets import interact
    from IPython.display import display
except (NameError, AttributeError):
    # Not in IPython environment
    pass


# ## Overview of Regularization
# 
# The goal of "regularizing" regression models is to **structurally prevent overfitting by imposing a penalty on the coefficients** of the model.
# 
# Regularization methods like Ridge and Lasso add an additional "penalty" on **the size of coefficients** to the loss function. When the loss function is minimized, this additional component is added to the residual sum of squares.
# 
# In other words, the minimization becomes a balance between two objectives:
# 1. Minimizing the error between predictions and true values
# 2. Keeping the size of the coefficients small
# 
# This balance helps prevent the model from becoming too complex and overfitting the training data.

# The three most common types of regularization are:
# 
# 1. **Ridge Regression** (L2 regularization): Adds a penalty equal to the sum of squared coefficients
# 2. **Lasso Regression** (L1 regularization): Adds a penalty equal to the sum of absolute values of coefficients
# 3. **Elastic Net**: A mixture of Ridge and Lasso that combines both penalties
# 
# We will examine the mathematics of each and see how these penalties affect our model fits.

# ### Geometric Interpretation of Regularization
# 
# <img src="https://www.evernote.com/l/AAH_btO8DnBF8I9__sqWwamIflWoyht43OoB/image.png"
#      width=600px>
# 
# From "Introduction to Statistical Learning" (ISLR), Chapter 6:
# 
# - The image on the left represents regularization via the Lasso (L1)
# - The image on the right represents regularization via Ridge Regression (L2)
# - The red ellipses represent contours of the loss function (residual sum of squares)
# - The blue areas represent the constraint regions for the regularization penalties
# - The point in the center is the minimum of the loss function (OLS solution)
# 
# The key insight is that regularization forces us to find the point where the loss function contour first intersects the constraint region. This can be interpreted as having a "budget" for coefficient sizes - we want to get as close as possible to the minimum of the loss function while staying within our budget.
# 
# Notice how the Lasso's diamond shape often intersects at corners (where one coefficient is zero), while Ridge's circular shape rarely sets coefficients exactly to zero.

# ## Review: Least Squares Loss Function
# 
# Before diving into regularization, let's review the standard loss function used in ordinary least squares (OLS) regression.
# 
# OLS minimizes the residual sum of squares (RSS) to fit the data:
# 
# $$\epsilon_i = y_i - \widehat{y}_i$$
# 
# Where:
# - $\epsilon_i$ is the residual for observation $i$
# - $y_i$ is the actual value for observation $i$
# - $\widehat{y}_i$ is the predicted value for observation $i$
# 
# The loss function is:
# 
# $$\mathcal{L}(\beta) = \sum_{i=1}^n \epsilon_i^2 = (y-X\beta)^T(y-X\beta)$$
# 
# Where:
# - $y$ is the vector of target values
# - $X$ is the matrix of features
# - $\beta$ is the vector of coefficients
# 
# This loss function leads to the well-known closed-form solution:
# 
# $$\beta = (X^TX)^{-1}X^Ty$$

# ## Ridge Regression (L2 Regularization)
# 
# Ridge regression adds a penalty term proportional to the sum of the squared coefficients to the loss function:
# 
# $$\mathcal{L}_{ridge}(\beta) = \sum_{i=1}^n \epsilon_i^2 + \alpha\sum_{j=1}^p\beta_j^2 = (y-X\beta)^T(y-X\beta) + \alpha\beta^T\beta $$
# 
# Where:
# - The first term is the standard OLS loss function
# - The second term is the L2 penalty
# - $\alpha$ is the regularization parameter that controls the strength of the penalty
# - Note that typically the intercept ($\beta_0$) is not penalized
# 
# ### Finding the Minimum
# 
# To find the coefficients that minimize this loss function, we take the derivative with respect to $\beta$ and set it equal to zero:
# 
# $$ \frac{d}{d\beta}\mathcal{L}_{ridge}(\beta) = 2X^TX\beta - 2X^Ty + 2\alpha\beta = 0$$
# 
# Rearranging:
# 
# $$ X^TX\beta + \alpha\beta = X^Ty $$
# $$ (X^TX + \alpha I)\beta = X^Ty $$
# 
# Where $I$ is the identity matrix. This gives us the closed-form solution:
# 
# $$\beta_{ridge} = (X^TX + \alpha I)^{-1}X^Ty$$
# 
# In code, this would be:
# ```python
# beta = np.linalg.inv(X.T.dot(X) + alpha * np.eye(X.shape[1])).dot(X.T).dot(y)
# ```
# 
# ### Key Properties of Ridge Regression
# 
# - $\beta^T\beta$ is known as the squared L2 norm ($||\beta||_2^2$)
# - $\alpha$ controls the strength of regularization:
#   - When $\alpha = 0$, Ridge regression is equivalent to OLS
#   - As $\alpha \to \infty$, all coefficients approach zero
# - Ridge shrinks all coefficients toward zero but rarely sets them exactly to zero
# - Ridge is particularly effective when dealing with multicollinearity
# - The larger the value of $\alpha$, the smaller our "budget" for coefficient sizes

# ## Lasso Regression (L1 Regularization)
# 
# Lasso (Least Absolute Shrinkage and Selection Operator) regression takes a different approach. Instead of adding the sum of squared coefficients to the loss function, it adds the sum of the absolute values of the coefficients:
# 
# $$\mathcal{L}_{lasso}(\beta) = \sum_{i=1}^n \epsilon_i^2 + \lambda\sum_{j=1}^p|\beta_j| = (y-X\beta)^T(y-X\beta) + \lambda||\beta||_1 $$
# 
# Where:
# - The first term is the standard OLS loss function
# - The second term is the L1 penalty
# - $\lambda$ is the regularization parameter that controls the strength of the penalty
# - $||\beta||_1$ is the L1 norm (sum of absolute values of coefficients)
# 
# ### No Closed-Form Solution
# 
# Unlike Ridge regression, Lasso does not have a closed-form solution. This is because the absolute value function is not differentiable at zero - it has a "kink" at that point.
# 
# Let's visualize the absolute value function and its derivative:

# In[ ]:


x = np.linspace(-3, 3, 500)
plt.figure(figsize=(10, 6))
plt.plot(x, np.piecewise(x, [x < 0, x >= 0], [lambda x: -x, lambda x: x]), 
         label='Absolute value function', linewidth=2)
plt.plot(x, np.piecewise(x, [x < 0, x >= 0], [-1, 1]), 
         label='Derivative', linewidth=2, linestyle='--')
plt.axvline(c='black', lw=0.5)
plt.axhline(c='black', lw=0.5)
plt.title('Absolute Value Function and Its Derivative', fontsize=14)
plt.xlabel('x', fontsize=12)
plt.ylabel('y', fontsize=12)
plt.grid(True, alpha=0.3)
plt.legend(fontsize=12)
plt.annotate('Non-differentiable point', xy=(0, 0), xytext=(0.5, 0.5),
             arrowprops=dict(facecolor='black', shrink=0.05))


# ### Key Properties of Lasso Regression
# 
# - $\sum|\beta_j|$ is known as the L1 norm ($||\beta||_1$)
# - $\lambda$ controls the strength of regularization:
#   - When $\lambda = 0$, Lasso is equivalent to OLS
#   - As $\lambda$ increases, more coefficients are set exactly to zero
# - Lasso performs feature selection by setting some coefficients exactly to zero
# - Lasso is solved using iterative optimization methods like coordinate descent
# - The larger the value of $\lambda$, the more aggressive the feature selection

# ## Elastic Net Regularization
# 
# Elastic Net combines both L1 and L2 regularization, adding both penalties to the loss function:
# 
# $$\mathcal{L}_{elastic}(\beta) = \sum_{i=1}^n \epsilon_i^2 + \lambda_1\sum_{j=1}^p|\beta_j| + \lambda_2\sum_{j=1}^p\beta_j^2 $$
# 
# Where:
# - The first term is the standard OLS loss function
# - The second term is the L1 penalty (Lasso)
# - The third term is the L2 penalty (Ridge)
# - $\lambda_1$ and $\lambda_2$ control the strength of each penalty
# 
# ### Key Properties of Elastic Net
# 
# - Elastic Net combines the benefits of both Ridge and Lasso
# - It can perform feature selection like Lasso while handling multicollinearity like Ridge
# - It's particularly useful when the number of features is much larger than the number of observations
# - The balance between L1 and L2 penalties can be adjusted through the ratio of $\lambda_1$ and $\lambda_2$
# - In scikit-learn, this is controlled through the `l1_ratio` parameter

# ## Why Use Regularization?
# 
# Regularization is particularly valuable when dealing with:
# 
# ### 1. Multicollinearity
# 
# Multicollinearity occurs when predictor variables are highly correlated with each other. This can lead to several problems:
# 
# - The effect of predictor variables depends on which other variables are included in the model
# - Small changes in the data can lead to large changes in coefficient estimates
# - The inverse matrix $(X^TX)^{-1}$ becomes numerically unstable
# - Coefficient interpretation becomes difficult, as we can't truly hold other variables constant
# 
# **Ridge regression** is particularly effective at handling multicollinearity by shrinking correlated variables toward each other.
# 
# ### 2. High-Dimensional Data
# 
# When we have many features relative to the number of observations:
# 
# - The model is likely to overfit the training data
# - Many features may be redundant or irrelevant
# - We need a way to identify the most important predictors
# 
# **Lasso regression** excels at feature selection by setting some coefficients exactly to zero, effectively removing irrelevant features from the model.
# 
# ### 3. Generalization
# 
# Regularization helps models generalize better to new, unseen data by:
# 
# - Preventing the model from fitting noise in the training data
# - Reducing model complexity
# - Creating more stable coefficient estimates
# 
# For our Ames housing dataset, regularization can help us build more robust models that perform well on new housing data.

# ## Applying Regularization to the Ames Housing Dataset
# 
# Let's load our preprocessed Ames housing data and apply regularization techniques to it.

# In[ ]:


# Load our preprocessed data
try:
    # Try to use IPython magic if in notebook environment
    get_ipython().run_line_magic('run', 'src/preprocessing.py')
except (NameError, AttributeError):
    # If not in notebook environment, import directly
    import sys
    import os
    sys.path.append(os.path.join(os.path.dirname(__file__), 'src'))
    from preprocessing import (
        dataset_1, dataset_2, dataset_3, dataset_4,
        target_1, target_2, target_3, target_4
    )


# In[ ]:


# Examine a sample of our dataset
print("Sample of dataset_2:")
dataset_2.sample(4)


# In[ ]:


# Check the dimensions of our data
print(f"Target shape: {target_2.shape}, Features shape: {dataset_2.shape}")
print(f"Number of features: {dataset_2.shape[1]}")

# With this many features, regularization will be particularly helpful


# ## Visualizing Ridge Regression
# 
# Let's visualize how Ridge regression coefficients change as we vary the regularization parameter alpha.

# In[6]:


# Ridge regression function already imported at the top


# In[7]:


def ridge_coefs(X, Y, alphas):
    """
    Calculate Ridge regression coefficients for different alpha values
    
    Parameters:
    -----------
    X : array-like
        Feature matrix
    Y : array-like
        Target vector
    alphas : array-like
        List of alpha values to try
        
    Returns:
    --------
    list
        List of coefficient arrays, one for each alpha value
    """
    # Set up the list to hold the different sets of coefficients
    coefs = []
    
    # Set up a ridge regression object
    ridge_reg = Ridge()
    
    # Iterate through the alphas fed into the function
    for a in alphas:
        # On each alpha reset the ridge model's alpha to the current one
        ridge_reg.set_params(alpha=a)
        
        # Fit or refit the model on the provided X, Y
        ridge_reg.fit(X, Y)
        
        # Get the coefficient list
        coefs.append(ridge_reg.coef_)
    
    return coefs


# Alpha values for Ridge regression are best visualized on a logarithmic scale because the effect of alpha on coefficients changes by orders of magnitude.

# In[ ]:


# Example of logarithmic spacing
print("Example of logarithmic spacing with np.logspace(-2, 2, 5):")
print(np.logspace(-2, 2, 5))
print("This gives us points at 0.01, 0.1, 1, 10, and 100")


# In[8]:


# Create a range of alpha values on a logarithmic scale
# np.logspace gives us points between specified orders of magnitude on a logarithmic scale (base 10)
r_alphas = np.logspace(-3, 12, 45)  # From 10^-3 to 10^12, 45 points

# Get the coefficients for each alpha for Ridge regression
print(f"Calculating Ridge coefficients for {len(r_alphas)} different alpha values...")
r_coefs = ridge_coefs(dataset_2, target_2, r_alphas)
print("Done!")


# Now let's create a function to visualize how coefficients change with different alpha values

# In[10]:


# Warnings already handled at the top


# In[11]:


# The cycler package already imported at the top

def coef_plotter(alphas, coefs, to_alpha, regtype='ridge'):
    """
    Plot the effect of regularization parameter alpha on coefficient values
    
    Parameters:
    -----------
    alphas : array-like
        List of alpha values
    coefs : list
        List of coefficient arrays corresponding to each alpha
    to_alpha : float
        Current alpha value to highlight
    regtype : str, default='ridge'
        Type of regularization ('ridge' or 'lasso')
        
    Returns:
    --------
    None
        Displays plots
    """
    # Get the full range of alphas before subsetting
    amin = np.min(alphas)
    amax = np.max(alphas)
    
    # Subset the alphas and coefficients to just the ones below the set limit
    alphas_subset = [a for a in alphas if a <= to_alpha]
    coefs_subset = coefs[0:len(alphas_subset)]
    
    # Get colors from seaborn
    colors = sns.color_palette("husl", len(coefs[0]))
    
    # Create figure with two subplots
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(18, 6))
    
    # First subplot: Coefficient paths
    ax1.set_prop_cycle(cycler('color', colors))
    
    # Print a vertical line showing our current alpha threshold
    ax1.axvline(to_alpha, lw=2, ls='dashed', c='k', alpha=0.4)
    
    # Plot the lines of alphas on x-axis and coefficients on y-axis
    ax1.plot(alphas_subset, coefs_subset, lw=2)
    
    # Set labels and scales
    ax1.set_xlabel('Alpha (regularization strength)', fontsize=14)
    ax1.set_ylabel('Coefficient value', fontsize=14)
    ax1.set_xscale('log')
    ax1.set_yscale('log')
    
    # Enforce axis limits
    ax1.set_xlim([amin, amax])
    ax1.set_ylim(1E-2, 1E5)
    
    # Add title and grid
    ax1.set_title(f'{regtype.capitalize()} Coefficient Paths', fontsize=16)
    ax1.grid(True, alpha=0.3)
    
    # Second subplot: Bar chart of coefficients at current alpha
    ax2.set_yscale('log')
    ax2.set_ylim(1E-2, 1E5)
    
    # Position the bars according to their index
    try:
        # Get the coefficients for the current alpha
        current_coefs = coefs_subset[-1] if coefs_subset else coefs[0]
        
        # Sort coefficients by absolute value for better visualization
        coef_indices = np.argsort(np.abs(current_coefs))[::-1]
        sorted_coefs = current_coefs[coef_indices]
        
        # Plot top 20 coefficients by magnitude
        top_n = min(20, len(sorted_coefs))
        ax2.bar(range(top_n), np.abs(sorted_coefs[:top_n]), align='center', color=colors[:top_n])
        
        # Add coefficient signs
        for i in range(top_n):
            sign = '+' if sorted_coefs[i] > 0 else '-'
            ax2.text(i, np.abs(sorted_coefs[i]) * 1.1, sign, ha='center')
            
    except (ValueError, IndexError):
        pass
    
    # Set labels and title
    ax2.set_title(f'Top Coefficients at Alpha={to_alpha:.2e}', fontsize=16)
    ax2.set_xlabel('Feature index', fontsize=14)
    ax2.set_ylabel('Absolute coefficient value (log scale)', fontsize=14)
    ax2.grid(True, alpha=0.3)
    
    plt.tight_layout()
    plt.show()


# Let's use ipywidgets to create an interactive visualization

# In[12]:


# Already imported at the top


# In[ ]:


# Create an interactive function to explore different alpha values
def ridge_plot_runner(log_of_alpha=-3.0):
    """Interactive function to visualize Ridge coefficients at different alpha values"""
    alpha = 10**log_of_alpha
    print(f"Showing Ridge regression with alpha = {alpha:.2e}")
    coef_plotter(r_alphas, r_coefs, alpha, regtype='ridge')

# Create an interactive slider
try:
    interact(ridge_plot_runner, 
             log_of_alpha=(-3.0, 12.0, 0.33))
except NameError:
    print("Interactive widgets not available outside of notebook environment")

# Key observations:
# - As alpha increases, coefficients shrink toward zero
# - Different features shrink at different rates
# - Even with very high alpha values, most coefficients remain non-zero


# ## Visualizing Lasso Regression
# 
# Now let's do the same analysis for Lasso regression and see how it differs from Ridge.

# In[15]:


# Lasso already imported at the top


# In[16]:


def lasso_coefs(X, Y, alphas):
    """
    Calculate Lasso regression coefficients for different alpha values
    
    Parameters:
    -----------
    X : array-like
        Feature matrix
    Y : array-like
        Target vector
    alphas : array-like
        List of alpha values to try
        
    Returns:
    --------
    list
        List of coefficient arrays, one for each alpha value
    """
    coefs = []
    lasso_reg = Lasso(max_iter=10000)  # Increase max_iter to ensure convergence
    
    for a in alphas:
        lasso_reg.set_params(alpha=a)
        try:
            lasso_reg.fit(X, Y)
            coefs.append(lasso_reg.coef_)
        except Exception as e:
            print(f"Error fitting Lasso with alpha={a}: {e}")
            # If fitting fails, use the last successful coefficients or zeros
            if coefs:
                coefs.append(coefs[-1])
            else:
                coefs.append(np.zeros(X.shape[1]))
    
    return coefs


# For Lasso, we'll use the same logarithmic scale of alpha values

# In[17]:


# Create a range of alpha values for Lasso
l_alphas = np.logspace(-3, 12, 45)

# Get the coefficients for each alpha for Lasso regression
print(f"Calculating Lasso coefficients for {len(l_alphas)} different alpha values...")
l_coefs = lasso_coefs(dataset_2, target_2, l_alphas)
print("Done!")


# In[ ]:


# Create an interactive function to explore different alpha values for Lasso
def lasso_plot_runner(log_of_alpha=-3):
    """Interactive function to visualize Lasso coefficients at different alpha values"""
    alpha = 10**log_of_alpha
    print(f"Showing Lasso regression with alpha = {alpha:.2e}")
    coef_plotter(l_alphas, l_coefs, alpha, regtype='lasso')

# Create an interactive slider
try:
    interact(lasso_plot_runner, 
             log_of_alpha=(-3.0, 10.0, 0.33))
except NameError:
    print("Interactive widgets not available outside of notebook environment")

# Key observations:
# - As alpha increases, more coefficients become exactly zero
# - Lasso performs feature selection by eliminating less important features
# - The sparsity of the model increases with alpha
# - This is different from Ridge, which only shrinks coefficients toward zero


# ## Finding the Optimal Regularization Parameter
# 
# Now that we've visualized how coefficients change with different alpha values, let's use cross-validation to find the optimal alpha for our dataset.

# In[20]:


from sklearn.model_selection import GridSearchCV


# In[ ]:


# Example of alpha values we'll use for grid search
print("Alpha values for grid search:")
print(np.logspace(-3, 5, 9))


# In[ ]:


# Perform grid search with cross-validation to find the best alpha for Lasso
print("Performing grid search for Lasso regression...")
lasso_gs = GridSearchCV(
    Lasso(max_iter=10000), 
    param_grid={'alpha': np.logspace(-3, 5, 9)}, 
    cv=5,              # 5-fold cross-validation
    n_jobs=-1,         # Use all available cores
    scoring='r2'       # Use R² score to evaluate models
)
lasso_gs.fit(dataset_1, target_1)
print(f"Best alpha: {lasso_gs.best_params_['alpha']}")
print(f"Best score: {lasso_gs.best_score_:.4f}")


# In[ ]:


# Examine the grid search results
print("Grid search results summary:")
print(f"Best parameters: {lasso_gs.best_params_}")
print(f"Best cross-validation score: {lasso_gs.best_score_:.4f}")


# In[ ]:


# Convert grid search results to a DataFrame for easier analysis
lasso_results = pd.DataFrame(lasso_gs.cv_results_)

# Display key columns
print("Grid search results details:")
display(lasso_results[['param_alpha', 'mean_test_score', 'std_test_score', 'rank_test_score']].sort_values('rank_test_score'))


# In[27]:


def plot_for_dataset(dataset, target, dataset_name, alphas):
    """
    Compare Ridge and Lasso performance across different alpha values for a dataset
    
    Parameters:
    -----------
    dataset : DataFrame
        Feature dataset
    target : Series
        Target variable
    dataset_name : str
        Name of the dataset for the plot title
    alphas : array-like
        Alpha values to test
        
    Returns:
    --------
    None
        Displays plots
    """
    # Perform grid search for Lasso
    lasso_gs = GridSearchCV(Lasso(max_iter=10000), param_grid={'alpha': alphas}, n_jobs=-1, cv=5)
    lasso_gs.fit(dataset, target)
    lasso_results = pd.DataFrame(lasso_gs.cv_results_)
    lasso_results.set_index('param_alpha', inplace=True)

    # Perform grid search for Ridge
    ridge_gs = GridSearchCV(Ridge(), param_grid={'alpha': alphas}, n_jobs=-1, cv=5)
    ridge_gs.fit(dataset, target)
    ridge_results = pd.DataFrame(ridge_gs.cv_results_)
    ridge_results.set_index('param_alpha', inplace=True)

    # Create plots
    fig, ax = plt.subplots(1, 2, figsize=(20, 6))
    fig.suptitle(f"Comparing Ridge and Lasso Performance on {dataset_name}", fontsize=16)

    # Plot Lasso results
    lasso_results[['mean_train_score', 'mean_test_score']].plot(
        logx=True, ylim=(0.5, 1.0), ax=ax[0], 
        title='Lasso Regression', grid=True
    )
    ax[0].set_xlabel('Alpha (regularization strength)', fontsize=12)
    ax[0].set_ylabel('R² Score', fontsize=12)
    ax[0].legend(['Training Score', 'Cross-Validation Score'])
    
    # Plot Ridge results
    ridge_results[['mean_train_score', 'mean_test_score']].plot(
        logx=True, ylim=(0.5, 1.0), ax=ax[1], 
        title='Ridge Regression', grid=True
    )
    ax[1].set_xlabel('Alpha (regularization strength)', fontsize=12)
    ax[1].set_ylabel('R² Score', fontsize=12)
    ax[1].legend(['Training Score', 'Cross-Validation Score'])

    # Highlight maximum test scores
    lasso_max_test_score = round(lasso_results.mean_test_score.max(), 4)
    ridge_max_test_score = round(ridge_results.mean_test_score.max(), 4)
    
    # Get best alpha values
    lasso_best_alpha = lasso_results['mean_test_score'].idxmax()
    ridge_best_alpha = ridge_results['mean_test_score'].idxmax()

    # Add horizontal lines and annotations for max scores
    ax[0].axhline(lasso_max_test_score, color='red', linestyle='--', label='Max Score')
    ax[0].text(
        lasso_best_alpha, lasso_max_test_score + 0.01, 
        f"Best Score: {lasso_max_test_score}\nBest Alpha: {lasso_best_alpha:.2e}", 
        bbox=dict(facecolor='white', alpha=0.8)
    )
    
    ax[1].axhline(ridge_max_test_score, color='red', linestyle='--', label='Max Score')
    ax[1].text(
        ridge_best_alpha, ridge_max_test_score + 0.01, 
        f"Best Score: {ridge_max_test_score}\nBest Alpha: {ridge_best_alpha:.2e}", 
        bbox=dict(facecolor='white', alpha=0.8)
    )
    
    # Add vertical lines at best alpha values
    ax[0].axvline(lasso_best_alpha, color='green', linestyle='--', alpha=0.5)
    ax[1].axvline(ridge_best_alpha, color='green', linestyle='--', alpha=0.5)
    
    plt.tight_layout(rect=[0, 0, 1, 0.95])  # Adjust for the suptitle


# In[ ]:


# Compare Ridge and Lasso across all four datasets with a wide range of alphas
print("Comparing Ridge and Lasso across all datasets with a wide range of alphas...")
plot_for_dataset(dataset_1, target_1, 'Dataset 1', np.logspace(-3, 5, 9))
plot_for_dataset(dataset_2, target_2, 'Dataset 2', np.logspace(-3, 5, 9))
plot_for_dataset(dataset_3, target_3, 'Dataset 3', np.logspace(-3, 5, 9))
plot_for_dataset(dataset_4, target_4, 'Dataset 4', np.logspace(-3, 5, 9))


# In[ ]:


# Based on the previous results, let's focus on a narrower range of alphas
print("Alpha values for refined grid search:")
print(np.logspace(1, 3, 15))


# In[ ]:


# Compare Ridge and Lasso with a more focused range of alphas
print("Comparing Ridge and Lasso with a more focused range of alphas...")
plot_for_dataset(dataset_1, target_1, 'Dataset 1', np.logspace(1, 3, 15))
plot_for_dataset(dataset_2, target_2, 'Dataset 2', np.logspace(1, 3, 15))
plot_for_dataset(dataset_3, target_3, 'Dataset 3', np.logspace(1, 3, 15))
plot_for_dataset(dataset_4, target_4, 'Dataset 4', np.logspace(1, 3, 15))

# Observations:
# 1. Both Ridge and Lasso perform well on our datasets
# 2. The optimal alpha value varies between datasets
# 3. Dataset 2 (with PCA components) generally shows good performance
# 4. There's a clear trade-off between training and test performance as alpha changes


# ## Analyzing the Best Lasso Model
# 
# Let's examine the best Lasso model in more detail to understand which features it selects as most important.

# In[33]:


# Perform a more focused grid search for Lasso on dataset_2
print("Performing focused grid search for Lasso on dataset_2...")
lasso_gs = GridSearchCV(
    Lasso(max_iter=10000), 
    param_grid={'alpha': np.logspace(1, 3, 5)}, 
    cv=5, 
    n_jobs=-1
)
lasso_gs.fit(dataset_2, target_2)

# Convert results to DataFrame
lasso_results = pd.DataFrame(lasso_gs.cv_results_)
lasso_results.set_index('param_alpha', inplace=True)

print(f"Best alpha: {lasso_gs.best_params_['alpha']}")
print(f"Best score: {lasso_gs.best_score_:.4f}")


# In[ ]:


# Examine the best estimator
best_lasso = lasso_gs.best_estimator_
print(f"Best Lasso model: {best_lasso}")
print(f"Intercept: {best_lasso.intercept_:.4f}")
print(f"Number of features used: {np.sum(best_lasso.coef_ != 0)} out of {len(best_lasso.coef_)}")


# In[35]:


# Create a DataFrame of coefficients for easier analysis
coefficients = pd.DataFrame(
    best_lasso.coef_, 
    index=dataset_2.columns, 
    columns=['value']
)


# In[ ]:


# Display all non-zero coefficients
print("Number of non-zero coefficients:", np.sum(coefficients.value != 0))
print("Number of zero coefficients:", np.sum(coefficients.value == 0))
print("Percentage of features used:", f"{np.sum(coefficients.value != 0) / len(coefficients) * 100:.1f}%")


# In[ ]:


# Filter to only non-zero coefficients
non_zero_coefs = coefficients[coefficients.value != 0]
print(f"Shape of non-zero coefficients: {non_zero_coefs.shape}")


# In[38]:


# Set display options to show more rows
pd.options.display.max_rows = 150


# In[ ]:


# Display the intercept
print(f"Intercept: {lasso_gs.best_estimator_.intercept_:.4f}")


# In[ ]:


# Add absolute value column and sort by magnitude
coefficients['abs'] = np.abs(coefficients.value)
top_coefs = coefficients.sort_values('abs', ascending=False).head(20)

# Create a bar plot of the top coefficients
plt.figure(figsize=(12, 8))
colors = ['blue' if c > 0 else 'red' for c in top_coefs['value']]
plt.bar(top_coefs.index, top_coefs['abs'], color=colors)
plt.xticks(rotation=90)
plt.title('Top 20 Features by Coefficient Magnitude', fontsize=16)
plt.xlabel('Feature', fontsize=14)
plt.ylabel('Absolute Coefficient Value', fontsize=14)
plt.grid(axis='y', alpha=0.3)

# Add a legend
# Patch already imported at the top
legend_elements = [
    Patch(facecolor='blue', label='Positive Coefficient'),
    Patch(facecolor='red', label='Negative Coefficient')
]
plt.legend(handles=legend_elements)

plt.tight_layout()
plt.show()

# Display the top coefficients
print("\nTop 20 features by coefficient magnitude:")
display(top_coefs[['value', 'abs']])


# In[ ]:


# Look at specific feature groups
condition_features = coefficients[coefficients.index.str.contains('Cond')]
print("Features related to condition:")
display(condition_features[condition_features.value != 0].sort_values('abs', ascending=False))

# You can examine other feature groups similarly
quality_features = coefficients[coefficients.index.str.contains('Qual')]
print("\nFeatures related to quality:")
display(quality_features[quality_features.value != 0].sort_values('abs', ascending=False))


# ## Summary
# 
# In this notebook, we've explored regularization techniques for linear regression:
# 
# 1. **Ridge Regression (L2)**:
#    - Adds a penalty proportional to the sum of squared coefficients
#    - Shrinks all coefficients toward zero but rarely sets them exactly to zero
#    - Particularly effective for handling multicollinearity
# 
# 2. **Lasso Regression (L1)**:
#    - Adds a penalty proportional to the sum of absolute coefficient values
#    - Can set some coefficients exactly to zero, performing feature selection
#    - Useful when you have many features and want to identify the most important ones
# 
# 3. **Elastic Net**:
#    - Combines both L1 and L2 penalties
#    - Offers a balance between feature selection and coefficient shrinkage
# 
# We've seen how the regularization parameter (alpha) affects model performance and coefficient values. Through cross-validation, we identified optimal alpha values for our Ames housing dataset.
# 
# The Lasso model with the optimal alpha selected a subset of features that are most predictive of house prices, providing us with insights into which housing characteristics have the strongest impact on price.
# 
# In the next notebook, we'll explore ensemble methods to further improve our predictive performance.

# In[ ]:




