import pip
import pandas as pd
import numpy as np

from sklearn.metrics import mean_squared_error, mean_absolute_error, r2_score

def import_or_install(package):
    try:
        __import__(package)
    except ImportError:
        pip.main(['install', package])
        __import__(package)

def metrics(model_name, actual, predictions):
    df = pd.DataFrame(columns=['model', 'MAE', 'MSE', 'RMSE', 'RMSLE', 'R2'])
    mae = mean_absolute_error(actual, predictions)
    mse = mean_squared_error(actual, predictions, squared=False)
    rmse = np.sqrt(mse)
    rmsle = np.log(rmse)
    r2 = r2_score(actual, predictions)
    
    metrics_data = pd.Series([model_name, mae, mse, rmse, rmsle, r2], index = df.columns)
    df = df.append(metrics_data, ignore_index=True)
    df.set_index('model', inplace=True)
    return df