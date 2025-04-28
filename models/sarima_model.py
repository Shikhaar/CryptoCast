# sarima_model.py

from statsmodels.tsa.statespace.sarimax import SARIMAX
import numpy as np
from sklearn.metrics import mean_squared_error

def build_and_train_sarima(data, test_data, order=(5,1,0), seasonal_order=(1,1,1,12)):
    model = SARIMAX(data, order=order, seasonal_order=seasonal_order)
    model_fit = model.fit()
    
    # Make predictions on the test data
    y_pred = model_fit.predict(start=len(data)-len(test_data), end=len(data)-1, typ='levels')
    
    # Calculate RMSE
    rmse = np.sqrt(mean_squared_error(test_data, y_pred))
    
    return model_fit, y_pred, rmse
