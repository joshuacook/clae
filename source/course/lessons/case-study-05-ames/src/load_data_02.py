import pandas as pd
import numpy as np
import os

def load_data():
    """
    Load and prepare the Ames housing dataset with imputed missing values.
    
    Returns:
        pandas.DataFrame: The prepared housing dataset with missing values handled
    """
    # Determine the correct path to the data files
    current_dir = os.path.dirname(os.path.abspath(__file__))
    parent_dir = os.path.dirname(current_dir)
    data_dir = os.path.join(parent_dir, 'data')
    
    # Try to load the train.csv file directly if it exists
    train_path = os.path.join(data_dir, 'train.csv')
    if os.path.exists(train_path):
        housing_df = pd.read_csv(train_path, index_col='Id')
    else:
        # Try alternative paths for housing.csv
        housing_path = os.path.join(data_dir, 'housing.csv')
        if os.path.exists(housing_path):
            housing_df = pd.read_csv(housing_path)
            print(housing_df.columns)
            # Set Id as index
            housing_df = housing_df.set_index('Id')
        else:
            # If neither file exists, try loading from load_data_01
            try:
                from load_data_01 import load_data as load_data_01
                housing_df = load_data_01()
                print("Loaded data using load_data_01")
            except Exception as e:
                print(f"Error loading data: {e}")
                raise FileNotFoundError("Could not find housing data files")
    
    # Drop X column if it exists
    if 'X' in housing_df.columns:
        housing_df = housing_df.drop('X', axis=1)
    
    # Convert categorical features
    categorical_columns = [
        'MSSubClass', 'OverallQual', 'OverallCond', 'BsmtFullBath',
        'BsmtHalfBath', 'FullBath', 'HalfBath', 'BedroomAbvGr',
        'KitchenAbvGr', 'TotRmsAbvGrd', 'Fireplaces', 'GarageCars', 'MoSold'
    ]
    for col in categorical_columns:
        housing_df[col] = housing_df[col].astype('category')
        current_categories = housing_df[col].cat.categories.tolist()
        housing_df[col] = housing_df[col].cat.set_categories(current_categories)
    
    # Handle missing values in numeric columns
    mean_LotFrontage = housing_df['LotFrontage'].mean()
    mean_MasVnrArea = housing_df['MasVnrArea'].mean()
    mean_GarageYrBlt = housing_df['GarageYrBlt'].mean()
    
    housing_df['LotFrontage'] = housing_df['LotFrontage'].fillna(mean_LotFrontage)
    housing_df['MasVnrArea'] = housing_df['MasVnrArea'].fillna(mean_MasVnrArea)
    housing_df['GarageYrBlt'] = housing_df['GarageYrBlt'].fillna(mean_GarageYrBlt)
    
    # Handle empty strings in categorical columns
    empty_means_without = [
        "Alley", "BsmtQual", "BsmtCond", "BsmtExposure", "BsmtFinType1",
        "BsmtFinType2", "FireplaceQu", "GarageType", "GarageFinish",
        "GarageQual", "GarageCond", "PoolQC", "Fence", "MiscFeature"
    ]
    
    empty_means_NA = ["MasVnrType", "Electrical"]
    
    # Helper functions for handling empty strings
    def replace_empty_with_none(df, feature):
        """Replace empty strings with 'None' in categorical columns"""
        if df[feature].dtype.name != 'category':
            df[feature] = df[feature].astype('category')
        
        # Get current categories and add 'None' if not present
        current_categories = df[feature].cat.categories.tolist()
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
        if df[feature].dtype.name != 'category':
            df[feature] = df[feature].astype('category')
        
        # Create a mask for empty strings
        empty_string_mask = df[feature] == ''
        
        # Replace empty strings with NaN
        df.loc[empty_string_mask, feature] = np.nan
        return df[feature]
    
    # Apply the replacements
    for feature in empty_means_without:
        if feature in housing_df.columns:
            housing_df[feature] = replace_empty_with_none(housing_df, feature)
    
    for feature in empty_means_NA:
        if feature in housing_df.columns:
            housing_df[feature] = replace_empty_with_NA(housing_df, feature)
    
    # Comment out dropna as we want to keep rows with NaN values for further processing
    # housing_df = housing_df.dropna()
    
    # Check if there are any remaining nulls and print them for debugging
    remaining_nulls = housing_df.isnull().sum()
    if remaining_nulls.sum() > 0:
        print("Remaining null values by column:")
        print(remaining_nulls[remaining_nulls > 0])
    
    return housing_df

def count_empty_values(df, feature):
    """Count empty string values in a column"""
    empty_string_mask = df[feature] == ""
    return empty_string_mask.sum()

def count_empty_total(df=None):
    """Count empty string values in all columns"""
    if df is None:
        df = load_data()
    
    empty_counts = {}
    for feature in df.columns:
        if df[feature].dtype == 'object' or df[feature].dtype.name == 'category':
            empty_count = count_empty_values(df, feature)
            if empty_count > 0:
                empty_counts[feature] = empty_count
                print(f"{feature}: {empty_count}")
    
    return empty_counts

if __name__ == "__main__":
    # Test the function
    df = load_data()
    print(f"Dataset shape: {df.shape}")
    print("\nFirst few rows:")
    print(df.head())
