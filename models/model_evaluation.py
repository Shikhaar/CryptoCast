import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

def evaluate_model(true_values, predicted_values, model_name):
    # Calculate RMSE
    rmse = np.sqrt(np.mean((true_values - predicted_values) ** 2))
    
    # Plot Actual vs Predicted
    plt.figure(figsize=(10, 6))
    plt.plot(true_values, label="Actual", color='blue')
    plt.plot(predicted_values, label=f"Predicted ({model_name})", color='red')
    plt.title(f"Model Evaluation: {model_name}")
    plt.xlabel("Time")
    plt.ylabel("Price")
    plt.legend()
    plt.show()
    
    print(f"{model_name} RMSE: {rmse}")
    return rmse
