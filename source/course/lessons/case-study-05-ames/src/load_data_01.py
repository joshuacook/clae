import pandas as pd
import os

def load_data():
    """
    Load and prepare the Ames housing dataset.
    
    Returns:
        pandas.DataFrame: The prepared housing dataset
    """
    # Determine the correct path to the data files
    current_dir = os.path.dirname(os.path.abspath(__file__))
    parent_dir = os.path.dirname(current_dir)
    data_dir = os.path.join(parent_dir, 'data')
    
    # Try to load the train.csv file directly if it exists
    train_path = os.path.join(data_dir, 'train.csv')
    if os.path.exists(train_path):
        housing_df = pd.read_csv(train_path, index_col='Id')
        return housing_df
    
    # If train.csv doesn't exist, try the separate files
    # Load the three separate datasets
    zoning_df = pd.read_csv(os.path.join(data_dir, 'zoning.csv'))
    listing_df = pd.read_csv(os.path.join(data_dir, 'listing.csv'))
    sale_df = pd.read_csv(os.path.join(data_dir, 'sale.csv'))
    
    # Merge the datasets
    housing_df = pd.merge(zoning_df, listing_df, on="Id")
    housing_df = pd.merge(housing_df, sale_df, on="Id")
    
    # Set Id as index
    housing_df = housing_df.set_index('Id')
    
    # Convert categorical features
    categorical_columns = [
        'MSSubClass', 'OverallQual', 'OverallCond', 'BsmtFullBath',
        'BsmtHalfBath', 'FullBath', 'HalfBath', 'BedroomAbvGr',
        'KitchenAbvGr', 'TotRmsAbvGrd', 'Fireplaces', 'GarageCars', 'MoSold'
    ]
    
    for col in categorical_columns:
        housing_df[col] = housing_df[col].astype('category')
    
    return housing_df

if __name__ == "__main__":
    # Test the function
    df = load_data()
    print(f"Dataset shape: {df.shape}")
    print("\nFirst few rows:")
    print(df.head())
