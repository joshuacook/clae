import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns

def multiplot(plots, cols=1, figsize=(20, 4)):
    """
    Display multiple matplotlib plots in a grid layout.
    
    Parameters:
    -----------
    plots : list
        List of matplotlib figure objects to display
    cols : int
        Number of columns in the grid
    figsize : tuple
        Figure size (width, height) in inches
    """
    n = len(plots)
    rows = (n + cols - 1) // cols  # Ceiling division
    
    fig = plt.figure(figsize=(figsize[0], figsize[1] * rows))
    
    for i, plot in enumerate(plots):
        plt.subplot(rows, cols, i + 1)
        if hasattr(plot, 'figure'):
            # If it's a figure, get the axes
            ax = plot.figure.axes[0]
            # Copy the plot to the current axes
            for item in ax.get_children():
                if hasattr(item, 'get_data'):
                    x, y = item.get_data()
                    plt.plot(x, y)
            plt.title(ax.get_title())
            plt.xlabel(ax.get_xlabel())
            plt.ylabel(ax.get_ylabel())
        else:
            # If it's already an axes or other object, just show it
            plt.sca(plot)
    
    plt.tight_layout()
    return fig

def hist_with_kde(feature, bins=50):
    """
    Create a histogram with KDE, mean, and median lines.
    
    Parameters:
    -----------
    feature : array-like
        Data to plot
    bins : int
        Number of bins for histogram
    
    Returns:
    --------
    matplotlib.axes.Axes
        The plot axes
    """
    plt.figure(figsize=(10, 6))
    
    # Create histogram with density
    sns.histplot(feature, bins=bins, kde=True, alpha=0.4)
    
    # Add mean and median lines
    mean_val = np.mean(feature)
    median_val = np.median(feature)
    
    plt.axvline(mean_val, color='blue', linestyle='dashed', linewidth=1, label=f'Mean: {mean_val:.2f}')
    plt.axvline(median_val, color='red', linestyle='dashed', linewidth=1, label=f'Median: {median_val:.2f}')
    
    plt.legend()
    return plt.gca()

def hist_with_kde_numerical_by_category(numerical_feature, categorical_feature):
    """
    Create a histogram with KDE for a numerical feature grouped by a categorical feature.
    
    Parameters:
    -----------
    numerical_feature : array-like
        Numerical data to plot
    categorical_feature : array-like
        Categorical data for grouping
    
    Returns:
    --------
    matplotlib.axes.Axes
        The plot axes
    """
    plt.figure(figsize=(12, 8))
    
    # Create a DataFrame for easier handling
    df = pd.DataFrame({
        'numerical': numerical_feature,
        'categorical': categorical_feature
    })
    
    # Plot histogram with KDE for each category
    sns.histplot(
        data=df, 
        x='numerical', 
        hue='categorical',
        kde=True, 
        alpha=0.4,
        common_norm=False
    )
    
    plt.title(f'{numerical_feature.name} by {categorical_feature.name}')
    return plt.gca()
