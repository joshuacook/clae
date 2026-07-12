"""
Impute Missing Values

This script handles imputing missing values in the Ames Housing dataset.
It addresses two types of missing values:
1. NaN values in numerical features
2. Empty strings in categorical features that should be 'None' or NA
"""

import numpy as np

def count_empty_values(df, feature):
    """Count empty string values in a column"""
    empty_string_mask = df[feature] == ""
    return empty_string_mask.sum()

def count_empty_total(df):
    """Count empty string values in all columns"""
    empty_counts = {}
    for feature in df.columns:
        if df[feature].dtype == 'object' or df[feature].dtype.name == 'category':
            empty_count = count_empty_values(df, feature)
            if empty_count > 0:
                empty_counts[feature] = empty_count
                print(f"{feature}: {empty_count}")
    return empty_counts

def replace_empty_with_none(df, feature):
    """Replace empty strings with 'None' in categorical columns"""
    # Convert to category if not already
    if df[feature].dtype.name != 'category':
        df[feature] = df[feature].astype('category')
    
    # Get current categories
    current_categories = df[feature].cat.categories.tolist()
    
    # Add 'None' to categories if not present
    if 'None' not in current_categories:
        new_categories = current_categories + ['None']
        df[feature] = df[feature].cat.set_categories(new_categories)
    
    # Create a mask for empty strings
    empty_string_mask = df[feature] == ''
    
    # Replace empty strings with 'None'
    df.loc[empty_string_mask, feature] = 'None'
    return df[feature]

def replace_empty_with_NA(df, feature):
    """Replace empty strings with NaN in categorical columns"""
    # Convert to category if not already
    if df[feature].dtype.name != 'category':
        df[feature] = df[feature].astype('category')
    
    # Create a mask for empty strings
    empty_string_mask = df[feature] == ''
    
    # Replace empty strings with NaN
    df.loc[empty_string_mask, feature] = np.nan
    return df[feature]

def impute_missing_values(housing_df):
    """
    Impute missing values in the housing dataset.
    
    Args:
        housing_df: pandas DataFrame with the housing data
        
    Returns:
        pandas DataFrame with imputed values
    """
    # Make a copy to avoid modifying the original
    df = housing_df.copy()
    
    # Print columns with NaN values
    nan_sums = df.isna().sum()
    nan_columns = nan_sums[nan_sums > 0]
    print(f"Columns with NaN values:\n{nan_columns}")
    
    # Calculate mean values for numerical columns with missing data
    mean_LotFrontage = df['LotFrontage'].mean()
    mean_MasVnrArea = df['MasVnrArea'].mean()
    mean_GarageYrBlt = df['GarageYrBlt'].mean()
    
    # Impute missing values with means
    df['LotFrontage'] = df['LotFrontage'].fillna(mean_LotFrontage)
    df['MasVnrArea'] = df['MasVnrArea'].fillna(mean_MasVnrArea)
    df['GarageYrBlt'] = df['GarageYrBlt'].fillna(mean_GarageYrBlt)
    
    # Define features where empty strings mean 'None' vs NA
    empty_means_without = [
        "Alley", "BsmtQual", "BsmtCond", "BsmtExposure", "BsmtFinType1",
        "BsmtFinType2", "FireplaceQu", "GarageType", "GarageFinish",
        "GarageQual", "GarageCond", "PoolQC", "Fence", "MiscFeature", "MasVnrType"
    ]
    
    empty_means_NA = ["Electrical"]
    
    # Replace empty strings with 'None' or NA as appropriate
    for feature in empty_means_without:
        if feature in df.columns:
            df[feature] = replace_empty_with_none(df, feature)
    
    for feature in empty_means_NA:
        if feature in df.columns:
            df[feature] = replace_empty_with_NA(df, feature)
    
    # Check for any remaining NaN values
    remaining_nans = df.isna().sum()
    remaining_nan_columns = remaining_nans[remaining_nans > 0]
    
    if len(remaining_nan_columns) > 0:
        print(f"Remaining columns with NaN values:\n{remaining_nan_columns}")
        print("Dropping rows with remaining NaN values")
        df = df.dropna()
        print(f"Shape after dropping NaN rows: {df.shape}")
    
    return df

def main():
    """Main function to load data and impute missing values"""
    import os
    import pandas as pd
    
    # Import the data loading function from previous script
    try:
        from load_data_01 import load_data
        
        # Load the housing data
        print("Loading housing data...")
        housing_df = load_data()
    except FileNotFoundError:
        # Fallback to direct loading if the load_data function fails
        print("Could not load data using load_data_01.py, trying direct loading...")
        
        # Get the current directory and parent directory for data
        current_dir = os.path.dirname(os.path.abspath(__file__))
        parent_dir = os.path.dirname(current_dir)
        data_dir = os.path.join(parent_dir, 'data')
        
        # Try to load the train.csv file
        train_path = os.path.join(data_dir, 'train.csv')
        if os.path.exists(train_path):
            housing_df = pd.read_csv(train_path, index_col='Id')
        else:
            # Try alternative paths
            possible_paths = [
                'data/train.csv',
                '../data/train.csv',
                '../../data/train.csv',
            ]
            
            for path in possible_paths:
                try:
                    housing_df = pd.read_csv(path, index_col='Id')
                    print(f"Successfully loaded data from {path}")
                    break
                except FileNotFoundError:
                    continue
            else:
                raise FileNotFoundError("Could not find the train.csv file in any expected location")
    
    print(f"Original data shape: {housing_df.shape}")
    
    # Impute missing values
    print("\nImputing missing values...")
    cleaned_df = impute_missing_values(housing_df)
    
    print("\nData cleaning complete!")
    return cleaned_df

if __name__ == "__main__":
    main()
