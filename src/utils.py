import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def plot_price(df, price_column='Price', date_column='Date', title='Bitcoin Closing Price Over Time'):
    """
    Plots the price over time.
    """
    plt.figure(figsize=(14, 7))
    plt.plot(df[date_column], df[price_column], label=price_column, color='blue')
    plt.title(title)
    plt.xlabel('Date')
    plt.ylabel('Price (USD)')
    plt.legend()
    plt.grid(True)
    plt.show()

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
