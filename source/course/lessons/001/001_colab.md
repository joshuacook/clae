---
title: "Vector Spaces: Mathematical Foundations"
subtitle: "Lesson 1: Colab"
author: "Linear Algebra and Estimation Theory"
date: "Week 1, Session 1"
---

# Vector Operations Support for Lab 1

This notebook provides helper functions and examples to support completion of Lab 1, focusing on vector operations and their visualization.

## Setup

```python
import numpy as np
import matplotlib.pyplot as plt

def setup_plot():
    plt.figure(figsize=(10, 6))
    plt.grid(True)
    plt.axhline(y=0, color='k', linestyle=':')
    plt.axvline(x=0, color='k', linestyle=':')
```

## Vector Operations

```python
def plot_vector(v, color='blue', label=None):
    """Plot a 2D vector from origin"""
    plt.quiver(0, 0, v[0], v[1], 
              angles='xy', scale_units='xy', scale=1,
              color=color, label=label)

def vector_addition(v1, v2):
    """Demonstrate vector addition"""
    setup_plot()
    plot_vector(v1, 'blue', 'v1')
    plot_vector(v2, 'red', 'v2')
    plot_vector(v1 + v2, 'green', 'v1 + v2')
    plt.title('Vector Addition')
    plt.legend()
    plt.show()
```

## Examples

```python
# Example vectors
v1 = np.array([1, 2])
v2 = np.array([3, 1])

# Basic operations
print(f"v1 + v2 = {v1 + v2}")
print(f"2v1 = {2 * v1}")

# Visualize
vector_addition(v1, v2)
```

## Practice Problems

```python
def practice():
    """Vector operation practice problems"""
    # Your code here
    pass
```
