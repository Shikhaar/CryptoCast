# src/data_preprocessing.py

import pandas as pd

def load_data(filepath):
    """
    Loads the BTC data from CSV file.

    Args:
        filepath (str): Path to the CSV file.

    Returns:
        pd.DataFrame: Loaded DataFrame.
    """
    df = pd.read_csv(filepath)
    return df

def clean_numeric_columns(df, columns):
    """
    Removes commas and converts specified columns to float.

    Args:
        df (pd.DataFrame): Input DataFrame.
        columns (list): List of columns to clean.

    Returns:
        pd.DataFrame: DataFrame with cleaned numeric columns.
    """
    for col in columns:
        df[col] = df[col].str.replace(',', '', regex=True)
        df[col] = df[col].astype(float)
    return df

def convert_volume_column(df, col_name='Vol.'):
    """
    Converts the Volume column from K/M/B to actual numbers.

    Args:
        df (pd.DataFrame): Input DataFrame.
        col_name (str): Name of the volume column.

    Returns:
        pd.DataFrame: DataFrame with Volume converted.
    """
    def volume_to_number(val):
        if isinstance(val, str):
            val = val.replace(',', '')
            if 'K' in val:
                return float(val.replace('K', '')) * 1e3
            elif 'M' in val:
                return float(val.replace('M', '')) * 1e6
            elif 'B' in val:
                return float(val.replace('B', '')) * 1e9
            else:
                return float(val)
        return val

    df[col_name] = df[col_name].apply(volume_to_number)
    return df

def clean_change_column(df, col_name='Change %'):
    """
    Cleans the Change % column by removing '%' and converting to float.

    Args:
        df (pd.DataFrame): Input DataFrame.
        col_name (str): Name of the change column.

    Returns:
        pd.DataFrame: DataFrame with Change % cleaned.
    """
    df[col_name] = df[col_name].str.replace('%', '', regex=True)
    df[col_name] = df[col_name].astype(float)
    return df

def preprocess_data(filepath):
    """
    Full preprocessing pipeline: loads, cleans, and returns DataFrame.

    Args:
        filepath (str): Path to raw data CSV.

    Returns:
        pd.DataFrame: Cleaned DataFrame.
    """
    df = load_data(filepath)

    # Clean specific columns
    numeric_cols = ['Price', 'Open', 'High', 'Low']
    df = clean_numeric_columns(df, numeric_cols)

    df = convert_volume_column(df, col_name='Vol.')
    df = clean_change_column(df, col_name='Change %')

    # Convert Date
    df['Date'] = pd.to_datetime(df['Date'])

    # Sort by Date
    df = df.sort_values('Date')

    return df

def save_data(df, save_path):
    """
    Saves the DataFrame to a CSV file.

    Args:
        df (pd.DataFrame): DataFrame to save.
        save_path (str): Destination path for the CSV.
    """
    df.to_csv(save_path, index=False)
    print(f"✅ Data saved to {save_path}")
