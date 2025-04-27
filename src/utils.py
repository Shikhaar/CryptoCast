import os
import re
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def train_test_split_time_series(df, test_size=0.2):
    """
    Splits a DataFrame into train and test sets for time series forecasting.
    """
    split_index = int(len(df) * (1 - test_size))
    train = df.iloc[:split_index]
    test = df.iloc[split_index:]
    return train, test

def display_missing_values(df):
    """
    Displays missing values in the DataFrame.
    """
    missing = df.isnull().sum()
    missing = missing[missing > 0]
    if missing.empty:
        print("✅ No missing values!")
    else:
        print("⚠️ Missing values found:")
        print(missing)

def format_large_numbers(num):
    """
    Formats large numbers for better readability (e.g., 1000000 -> 1M)
    """
    if abs(num) >= 1e9:
        return f'{num/1e9:.2f}B'
    elif abs(num) >= 1e6:
        return f'{num/1e6:.2f}M'
    elif abs(num) >= 1e3:
        return f'{num/1e3:.2f}K'
    else:
        return str(num)

def save_fig(title, tight=True, dpi=300, folder="../outputs/figures"):
    """
    Saves the current Matplotlib figure with a cleaned-up filename.
    
    Args:
        title (str): Title to use for the filename.
        tight (bool): Whether to use tight layout.
        dpi (int): Resolution of the image.
        folder (str): Folder where to save the figure.
    """
    if not os.path.exists(folder):
        os.makedirs(folder)  # Create folder if it doesn't exist
    
    # Clean filename: remove special characters, spaces to underscores
    filename = re.sub(r'[^a-zA-Z0-9]', '_', title) + ".png"
    filepath = os.path.join(folder, filename)
    
    if tight:
        plt.savefig(filepath, bbox_inches='tight', dpi=dpi)
    else:
        plt.savefig(filepath, dpi=dpi)
    
    print(f"✅ Figure saved: {filepath}")