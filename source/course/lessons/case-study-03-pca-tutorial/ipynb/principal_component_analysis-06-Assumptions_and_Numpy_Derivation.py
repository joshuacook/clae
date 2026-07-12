#!/usr/bin/env python
# coding: utf-8

# Estimated time: 45 minutes
#
# In[1]:


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


# <img src="https://www.evernote.com/l/AAFyWbRBljJIqqUfNcOo8SvvvPa3gCnvCsAB/image.png" width="400px">

# In[2]:


data_df = pd.read_pickle('../data/ball_on_spring.p')


# In[ ]:


data_df.sample(4)


# In[ ]:


fig, ax = plt.subplots(1,3,figsize=(15,4))
for i, cam in enumerate(['a', 'b', 'c']):
    x_axis = 'x_{}'.format(cam)
    y_axis = 'y_{}'.format(cam)
    
    data_df.plot(x_axis, y_axis, kind='scatter', 
                 ax=ax[i], xlim=(-4,4), ylim=(-4,4))
    
    ax[i].axvline(c='black')
    ax[i].axhline(c='black')
    ax[i].arrow(0,-4,0,1,color='green',lw=12)


# We can think of the green arrow as the camera.

# ### Variance and the Goal

# At a high-level, our goal is to find a transformation for our data so that it is a "best expression" of the data.

# Mathematically, this looks like this 
# 
# $$X' = PX$$
# 
# where $X$ is the original data and $X'$ is the transformed, "best expression" of the data. 
# 
# $P$ is a permutation or transformation matrix. 

# # Assumptions and Limits
# 
# 1. Linearity
# 2. Scaled, Skew-Normal Data
# 3. Larger variances are more important
# 4. The principal components are orthogonal

# ### Numpy Derivation

# Let $X$ be our data.

# In[8]:


X = data_df


# First look at $X^TX$.
# 
# **NOTE:** $X^TX$ is a symmetric matrix.

# In[ ]:


X.shape


# ### Gramian Matrix

# In[ ]:


X.T.dot(X)


# Let's look at the covariance matrix of $X$.

# In[ ]:


X.cov()


# And the correlation matrix of $X$.

# In[ ]:


X.corr()


# There's no discernable pattern in there because the data is not conditioned.

# ### Conditioning The Data

# Here we manually scale the data instead of importing `StandardScaler` from `sklearn.preprocessing`.

# In[ ]:


X.shape


# #### Center the Data

# In[ ]:


X.mean(), np.array(X).mean()


# In[15]:


X_c = X - X.mean()


# ### $X_{c}^TX_{c}$

# In[ ]:


X_c.T.dot(X_c)


# ### $X_{c}$ covariance
# 
# Note that `.cov()` calculates the **sample covariance** and is thus multiplied by a factor of $\frac{1}{n-1}$.
# 
# Here, we achieve identical results using `X_c.T.dot(X_c)/149` and `X.cov()`.

# In[ ]:


X_c.T.dot(X_c)/149


# In[ ]:


X.cov()


# ##### Remember: assertions go silent when they pass

# In[19]:


assert True


# In[ ]:


assert False


# In[21]:


np.testing.assert_array_almost_equal(X_c.T.dot(X_c)/149, X.cov())


# ### $X_{sc}$ correlation

# The correlation matrix is scaled data. 
# 
# Note that `.corr` calculates the **population correlation** and is the scaled data multiplied by a factor of $\frac1n$.

# #### Scale the Data

# In[22]:


X_sc = X_c/X.std(ddof=0)


# In[ ]:


X_sc.T.dot(X_sc)/150


# In[ ]:


X.corr()


# In[25]:


np.testing.assert_array_almost_equal(X_sc.T.dot(X_sc)/150, X.corr())


# ### This is Interesting

# In[26]:


np.testing.assert_array_almost_equal(X_sc.corr(), X.corr())


# Correlation is scale independent (think distributions).

# ## Datasets
# 
# ### Conditioned Data
# | dataset    | `numpy`                        | definition                                            |
# |:-----------|--------------------------------|-------------------------------------------------------|
# | $X$        | `X`                            | original                                              |
# | $X_{c}$    | `X - X.mean()`                 | centered (subtract the mean)                          |
# | $X_{sc}$   | `(X - X.mean())/X.std(ddof=0)` | scaled (subtract the mean, divide by std)             |
# 
# ### Gramian Data
# | dataset    | `numpy`                        | definition                                            |
# |:-----------|--------------------------------|-------------------------------------------------------|
# | $X^TX$     | `X.T.dot(X)` | the Gramian matrix for $X$ |
# | $X_{cov}$  | `X.cov()` | pairwise covariance of columns, divided by $n-1$<br>$X_c^TX_c$, divided by $n-1$ |
# | $X_{corr}$ | `X.corr()`| scaled, pairwise covariance, divided by $n$<br>$X_{sc}^TX_{sc}$, divided by $n$  |

# ##  EigenDecomposition of the Covariance
# 
# One tricky thing:
# 
# - `sklearn` uses the population covariance i.e. multiplied by $\frac{1}{n}$
# - `pandas` uses the sample covariance i.e. multiplied by $\frac{1}{n-1}$
# 

# In[ ]:


from sklearn.decomposition import PCA
pca = PCA()
pca.fit(X)


# In[28]:


eig_vals_cov, eig_vecs_cov = np.linalg.eig(X.cov()*149/150)


# In[29]:


eig_vals_man, eig_vecs_man = np.linalg.eig(X_c.T.dot(X_c)/150)


# In[ ]:


eig_vecs_cov = pd.DataFrame(eig_vecs_cov)
eig_vecs_cov


# In[ ]:


pd.DataFrame(pca.components_.T)


# In[ ]:


eig_vecs_man = pd.DataFrame(eig_vecs_man)
eig_vecs_man


# In[ ]:


try:
    np.testing.assert_array_almost_equal(eig_vecs_cov, eig_vecs_man)
except:
    print("Manual and Covariance are not equal.")
try:
    np.testing.assert_array_almost_equal(pca.components_.T, eig_vecs_man)
except:
    print("Manual and PCA Components are not equal.")


# In[ ]:


eig_vals_man, eig_vals_cov


# In[ ]:


pca.explained_variance_


# # A Principal Component Analysis is the EigenDecomposition of the Population Covariance Matrix

# ### We can state the sklearn PCA algorithm as such

# 1. for data $A$
# 2. center the data $A_c = A - A_\mu$
# 2. calculate $A_c^TA_c$
# 3. divide $A_c^TA_c$ by $n$
# 4. find the eigendecomposition of this matrix, $S\Lambda S^T$
# 5. the explained variances are the eigenvalues, the principal components are S.

# ### Explained Variance Ratio
# 
# Explained variance ratio scales all of the explained variance values so that the sum of the explained variances is 1.

# In[ ]:


pca.explained_variance_ratio_


# Basically almost all of our data is captured by the first principal component. 

# In[37]:


pca_1 = PCA(n_components=3)


# In[38]:


pca_1_vec = pca_1.fit_transform(X)


# In[39]:


tt = np.array(range(150))


# In[ ]:


plt.scatter(pca_1_vec[:,0], tt)


# In[ ]:


plt.scatter(pca_1_vec[:,1], tt)


# In[ ]:


plt.scatter(pca_1_vec[:,2], tt)

