🚀 CryptoCast: Forecasting Bitcoin with AI
CryptoCast is a comprehensive time series forecasting project aimed at predicting Bitcoin prices using both traditional statistical models and advanced deep learning techniques. This project showcases model implementation, comparison, and ensemble approaches to identify the best-performing predictors.

📌 Project Overview
This project involves:

Collecting historical Bitcoin price data.

Preprocessing and transforming the time series.

Applying and comparing various forecasting models:

Traditional Models: ARIMA, SARIMA

Deep Learning Models: LSTM, BiLSTM

Hybrid Approaches: Averaging (ARIMA+BiLSTM, LSTM+BiLSTM), Stacked Ensemble

Evaluating model performance using metrics like MAE, MSE, RMSE, and R².

Visualizing predictions vs actuals and model comparisons.

🧠 Models Used

Model	MAE	RMSE	R² Score
LSTM	1440.88	1960.98	0.9943
Stacked Ensemble	1891.38	2603.46	0.9899
LSTM + BiLSTM Avg	1910.78	2909.12	0.9875
BiLSTM	2827.65	4428.93	0.9711
ARIMA + BiLSTM Avg	12169.24	15265.54	0.6568
ARIMA	26156.80	33122.17	-0.6140
SARIMA	26156.80	33122.17	-0.6140

📈 Conclusion: The LSTM model performed the best, achieving an R² of 0.994, indicating excellent forecasting ability on unseen data.

📂 Project Structure
CryptoCast/
├── data/                  # Raw and processed data
├── models/                # Saved model files (e.g., .pkl, .keras)
├── outputs/
│   ├── figures/           # Prediction and comparison plots
│   └── metrics/           # Evaluation and result CSVs
├── src/                   # Scripts and utility functions
├── notebooks/             # Jupyter notebooks (modeling, evaluation, visualization)
└── README.md              # Project summary and instructions

🛠️ Requirements
Install dependencies using:
pip install -r requirements.txt

Main libraries:

pmdarima

statsmodels

scikit-learn

tensorflow / keras

matplotlib, seaborn, pandas, numpy

📊 Visual Insights
The project includes:

Line plots of predicted vs actual prices.

Metric comparison bar plots across all models.

Time series visualizations and error analysis.

📌 Key Takeaways
Deep learning models, particularly LSTM, are highly effective for non-linear and noisy data like cryptocurrency prices.

Ensemble methods, such as stacked models and average combinations, help balance model weaknesses and often yield robust results.

Traditional models like ARIMA and SARIMA perform poorly in volatile crypto markets.

🧾 License
This project is intended for academic and educational use.