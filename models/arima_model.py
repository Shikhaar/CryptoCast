from statsmodels.tsa.arima.model import ARIMA
import numpy as np
from sklearn.metrics import mean_squared_error

def build_and_train_arima(data, test_data, order=(5,1,0)):
    model = ARIMA(data, order=order)
    model_fit = model.fit()
    
    # Make predictions on the test data
    y_pred = model_fit.predict(start=len(data)-len(test_data), end=len(data)-1, typ='levels')
    
    # Calculate RMSE
    rmse = np.sqrt(mean_squared_error(test_data, y_pred))
    
    return model_fit, y_pred, rmse
