import pandas as pd
import numpy as np
from sklearn.preprocessing import MinMaxScaler
from typing import Tuple, Dict
from sklearn.model_selection import train_test_split

def load_and_clean_data(filepath: str) -> pd.DataFrame:
    """Load and clean the raw data"""
    df = pd.read_csv(filepath)
    
    # Clean numeric columns
    numeric_cols = ['Price', 'Open', 'High', 'Low']
    for col in numeric_cols:
        df[col] = df[col].str.replace(',', '', regex=True).astype(float)
    
    # Clean volume column
    df['Vol.'] = df['Vol.'].apply(lambda x: float(x.replace('K', 'e3').replace('M', 'e6').replace('B', 'e9').replace(',', '')) if isinstance(x, str) else x)
    
    # Clean Change % column
    df['Change %'] = df['Change %'].str.replace('%', '', regex=True).astype(float)
    
    # Convert and sort by date
    df['Date'] = pd.to_datetime(df['Date'])
    df = df.sort_values('Date')
    
    return df

def prepare_sequences(data: np.ndarray, seq_length: int = 10) -> Tuple[np.ndarray, np.ndarray]:
    """Create sequences for time series prediction"""
    X, y = [], []
    for i in range(len(data) - seq_length):
        X.append(data[i:(i + seq_length)])
        y.append(data[i + seq_length])
    return np.array(X), np.array(y)

def prepare_model_data(data: pd.DataFrame, seq_length: int = 10, test_size: float = 0.2) -> Dict:
    """Prepare data for model training"""
    # Scale the data
    scaler = MinMaxScaler()
    scaled_data = scaler.fit_transform(data['Price'].values.reshape(-1, 1))
    
    # Create sequences
    X, y = prepare_sequences(scaled_data, seq_length)
    
    # Split data
    X_temp, X_test, y_temp, y_test = train_test_split(X, y, test_size=test_size, shuffle=False)
    X_train, X_val, y_train, y_val = train_test_split(X_temp, y_temp, test_size=test_size, shuffle=False)
    
    # Reshape for LSTM input
    X_train = X_train.reshape((X_train.shape[0], X_train.shape[1], 1))
    X_val = X_val.reshape((X_val.shape[0], X_val.shape[1], 1))
    X_test = X_test.reshape((X_test.shape[0], X_test.shape[1], 1))
    
    return {
        'X_train': X_train, 'y_train': y_train,
        'X_val': X_val, 'y_val': y_val,
        'X_test': X_test, 'y_test': y_test,
        'scaler': scaler
    }