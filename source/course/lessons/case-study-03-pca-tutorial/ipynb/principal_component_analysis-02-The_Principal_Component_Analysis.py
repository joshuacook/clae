#!/usr/bin/env python
# coding: utf-8

# Here, we formally introduce the Principal Component Analysis.

# # The Principal Component Analysis

# PCA is fundamentally a dimensionality reduction algorithm, but it can also be useful as a tool:
# 
# - for visualization
# - for noise filtering
# - for (latent) feature extraction and engineering
# 
# PCA provides a low-dimensional representaion of a data set that contains as much of the variation in the data as possible. 
# 
# The original data is $n$ observations in $p$-dimensional space. PCA is useful where not all $p$ dimensions are equally interesting. 
# 
# PCA seeks a small number of dimensions that are as interesting as possible. 
# 
# Each dimension found by the PCA is a linear combination of the $p$ features so that each Principal Component is given by 
# 
# $$Z_i = \phi_{1i}X_1 + \phi_{2i}X_2 + \dots + \phi_{pi}X_p$$
# 
# $$Z_1 = \phi_{11}X_1 + \phi_{21}X_2 + \dots + \phi_{p1}X_p$$

# In[1]:


import numpy as np
from pandas import DataFrame as DF
import matplotlib.pyplot as plt


# The behavior of the PCA is easiest to visualize by looking at a two-dimensional dataset. By eye, it is clear that there is a nearly linear relationship between the x and y variables.

# In[3]:


rng = np.random.RandomState(1)
X = np.dot(rng.rand(2, 2), rng.randn(2, 200)).T
plt.scatter(X[:, 0], X[:, 1])
plt.axis('equal');


# PCA attempts to learn about the **relationship** between the x and y values.

# #### `sklearn.decomposition.PCA`

# In principal component analysis, this relationship is quantified by finding a list of the principal axes in the data, and using those axes to describe the dataset. Using Scikit-Learn's `PCA` estimator, we can compute this as follows:

# In python, classes are camel case, `MyPythonClass`.
# 
# Objects are snake case, `my_python_object`.
# 
# On the names of cases, there is also kebab case, which is used for file names, `my-python-file.py`.
# 

# In[4]:


from sklearn.decomposition import PCA
pca = PCA(n_components=2) # instantiate the PCA object
pca.fit(X) # fit the PCA object to the data


# The fit learns some quantities from the data, most importantly the "components" and "explained variance":

# In[5]:


DF(pca.components_) # column-oriented because pandas


# In[6]:


DF(pca.explained_variance_)


# To see what these numbers mean, let's visualize them as vectors over the input data, using the "components" to define the direction of the vector, and the "explained variance" to define the squared-length of the vector:

# In[7]:


def draw_vector(v0, v1, ax=None):
    ax = ax or plt.gca()
    arrowprops=dict(arrowstyle='->',
                    linewidth=2,
                    shrinkA=0, shrinkB=0)
    ax.annotate('', v1, v0, arrowprops=arrowprops)

# plot data
plt.scatter(X[:, 0], X[:, 1], alpha=0.2)
for length, vector in zip(pca.explained_variance_, pca.components_):
    v = vector * 3 * np.sqrt(length)
    draw_vector(pca.mean_, pca.mean_ + v)
plt.axis('equal');


# ### PCA as dimensionality reduction
# 
# Using PCA for dimensionality reduction involves zeroing out one or more of the smallest principal components, resulting in a lower-dimensional projection of the data that preserves the maximal data variance.

# In[8]:


pca = PCA(n_components=1)
pca.fit(X)
X_pca = pca.transform(X)
print("original shape:   ", X.shape)
print("transformed shape:", X_pca.shape)


# The transformed data has been reduced to a single dimension. To understand the effect of this dimensionality reduction, we can perform the inverse transform of this reduced data and plot it along with the original data:
# 

# In[9]:


X_new = pca.inverse_transform(X_pca)
plt.scatter(X[:, 0], X[:, 1], alpha=0.2)
plt.scatter(X_new[:, 0], X_new[:, 1], alpha=0.8)
plt.axis('equal');


# The light points are the original data, while the dark points are the projected version. This makes clear what a PCA dimensionality reduction means: the information along the least important principal axis or axes is removed, leaving only the component(s) of the data with the highest variance. The fraction of variance that is cut out (proportional to the spread of points about the line formed in this figure) is roughly a measure of how much "information" is discarded in this reduction of dimensionality.

# ### PCA for visualization: Hand-written digits
# The usefulness of the dimensionality reduction may not be entirely apparent in only two dimensions, but becomes much more clear when looking at high-dimensional data.

# In[10]:


from sklearn.datasets import load_digits # mnist dataset
digits = load_digits()
digits.data.shape


# In[11]:


print(digits.DESCR)


# In[12]:


# set up the figure
fig = plt.figure(figsize=(6, 6))  # figure size in inches
fig.subplots_adjust(left=0, right=1, bottom=0, top=1, hspace=0.05, wspace=0.05)

# plot the digits: each image is 8x8 pixels
for i in range(64):
    ax = fig.add_subplot(8, 8, i + 1, xticks=[], yticks=[])
    ax.imshow(digits.images[i], cmap=plt.cm.binary, interpolation='nearest')
    
    # label the image with the target value
    ax.text(0, 7, str(digits.target[i]))


# Reduce the dimensionality.

# In[13]:


pca = PCA(2)  # project from 64 to 2 dimensions
projected = pca.fit_transform(digits.data)
print(digits.data.shape)
print(projected.shape)


# We can now plot the first two principal components of each point to learn about the data:

# In[17]:


plt.scatter(projected[:, 0], projected[:, 1],
            c=digits.target, edgecolor='none', alpha=0.5,
            cmap=plt.cm.get_cmap('jet', 10))
plt.xlabel('component 1')
plt.ylabel('component 2')
plt.colorbar();


# In[18]:


pca.explained_variance_


# In[32]:


pca_10 = PCA(10)  # project from 64 to 2 dimensions
projected_10 = pca_10.fit_transform(digits.data)


# In[25]:


pca_10.explained_variance_


# In[26]:


pca_20 = PCA(20)  # project from 64 to 2 dimensions
pca_20.fit(digits.data)

pca_20.explained_variance_


# In[34]:


pca_20.explained_variance_ratio_


# In[35]:


plt.bar(height=np.cumsum(pca_20.explained_variance_ratio_), x=range(20))


# In[33]:


fig, ax = plt.subplots(1, 3, figsize=(12, 4))

# plot 1 shows pc 1 vs pc 2
ax[0].scatter(projected_10[:, 0], projected_10[:, 1],
            c=digits.target, edgecolor='none', alpha=0.5,
            cmap=plt.cm.get_cmap('jet', 10))
ax[0].set_xlabel('component 1')
ax[0].set_ylabel('component 2')
ax[0].set_title('2 components')

# plot 2 shows pc 1 vs pc 3
ax[1].scatter(projected_10[:, 0], projected_10[:, 2],
            c=digits.target, edgecolor='none', alpha=0.5,
            cmap=plt.cm.get_cmap('jet', 10))
ax[1].set_xlabel('component 1')
ax[1].set_ylabel('component 3')
ax[1].set_title('3 components')

# plot 3 shows pc 2 vs pc 3
ax[2].scatter(projected_10[:, 1], projected_10[:, 2],
            c=digits.target, edgecolor='none', alpha=0.5,
            cmap=plt.cm.get_cmap('jet', 10))
ax[2].set_xlabel('component 2')
ax[2].set_ylabel('component 3')
ax[2].set_title('3 components')



# In[ ]:




