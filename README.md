# 🪙 CryptoCast: Forecasting Bitcoin with AI

CryptoCast is a machine learning-powered project that forecasts future Bitcoin prices using a range of predictive models. From traditional statistical techniques like ARIMA and SARIMA to advanced deep learning models such as LSTM and BiLSTM, and sophisticated ensemble strategies, CryptoCast aims to provide accurate, explainable, and comparative insights into cryptocurrency forecasting.

Notably, the LSTM model achieved the best performance among all models explored, showcasing the strength of deep learning for time series predictions in volatile domains like cryptocurrency.

---

[![Ask DeepWiki](https://deepwiki.com/badge.svg)](https://deepwiki.com/ranjansatvik/CryptoCast)

## 📚 Table of Contents
- [Overview](#overview)
- [Features](#features)
- [Tech Stack](#tech-stack)
- [Project Structure](#project-structure)
- [How to Run](#how-to-run)
- [Modeling Techniques](#modeling-techniques)
- [Results](#results)
- [Conclusion](#conclusion)
- [Screenshots](#screenshots)
- [License](#license)
- [Contact](#contact)

---

## 📖 Overview

With the growing volatility and interest in cryptocurrencies, accurate forecasting of crypto prices is both a technical and economic challenge. This project explores Bitcoin price prediction using statistical models (ARIMA, SARIMA), deep learning models (LSTM, BiLSTM), and hybrid/ensemble approaches that combine their strengths.

Each model is evaluated using metrics such as MAE, RMSE, and R² Score, with detailed comparisons and plots provided. The ultimate goal is to assess the forecasting capabilities of each technique and determine which method best captures Bitcoin's price behavior.

---

## ✨ Features
- ✅ Log transform & normalization of time series data
- 📊 Comparative modeling using ARIMA, SARIMA, LSTM, BiLSTM
- 🔁 Hybrid and ensemble models: stacking & averaging
- 📈 Evaluation using MAE, RMSE, MSE, and R² Score
- 📎 Visualizations for predictions vs actual trends
- 📦 Modular structure for easy experimentation

---

## 🛠️ Tech Stack

- **Programming Language**: Python 3.9.13
- **Environment**:
  - VS Code
  - Jupyter Notebook (MacOS/Linux users can use `jupyter notebook` in terminal)
- **Libraries**: `pmdarima`, `scikit-learn`, `matplotlib`, `seaborn`, `tensorflow`, `xgboost`, `pandas`, `numpy`
- **Models Used**:
  - ARIMA
  - SARIMA
  - LSTM
  - BiLSTM
  - XGBoost
  - Ensemble (Averaging & Stacking)

---

## 📂 Project Structure

```bash
CryptoCast/
│
├── data/
│   ├── raw/                # Original raw data
│   └── processed/          # Preprocessed, clean data
│
├── models/                 # Saved model files (.pkl, .keras)
│
├── notebooks/
│
├── outputs/
│   ├── figures/            # Visualizations
│   └── metrics/            # CSVs of predictions, evaluations
│
├── requirements.txt        # Python dependencies
├── README.md               # Project description and documentation
└── ...                     # Other files
```

---

## ▶️ How to Run

**Step 1: Clone the repository**
```bash
# Windows
git clone https://github.com/ranjansatvik/CryptoCast.git
cd CryptoPricePrediction
```
```bash
# MacOS/Linux
git clone https://github.com/ranjansatvik/CryptoCast.git
cd CryptoPricePrediction
```

**Step 2: Install required libraries**
```bash
# Windows
pip install -r requirements.txt
```
```bash
# MacOS/Linux
pip3 install -r requirements.txt
```

**Step 3: Run the notebooks**
- Open VS Code.
- Navigate to the `notebooks/` folder.
- Open `.ipynb` files with Jupyter Notebook extension and run cell-by-cell.
- (MacOS/Linux users can run `jupyter notebook` in terminal and open in browser.)

---

## 🧪 Modeling Techniques

| Model                 | Description                                     |
|----------------------|-------------------------------------------------|
| ARIMA                | Classical model for time series prediction      |
| SARIMA               | ARIMA with seasonality                          |
| LSTM                 | Deep learning model using memory cells          |
| BiLSTM               | Bidirectional version of LSTM                   |
| Avg_LSTM_BiLSTM      | Simple average ensemble                         |
| Avg_ARIMA_BiLSTM     | Hybrid average model                            |
| Stacked Ensemble     | Meta-model using predictions from base models   |

---

## 📊 Results

Sorted by **Top R² Score**:

| Model               | MAE         | MSE         | RMSE        | R² Score  |
|--------------------|-------------|-------------|-------------|-----------|
| LSTM               | 1440.88     | 3.85e+06    | 1960.98     | 0.9943    |
| Stacked            | 1891.38     | 6.78e+06    | 2603.46     | 0.9899    |
| Avg_LSTM_BiLSTM    | 1910.78     | 8.46e+06    | 2909.12     | 0.9875    |
| BiLSTM             | 2827.65     | 1.96e+07    | 4428.93     | 0.9711    |
| Avg_ARIMA_BiLSTM   | 12169.24    | 2.33e+08    | 15265.54    | 0.6568    |
| ARIMA              | 26156.80    | 1.10e+09    | 33122.17    | -0.6140   |
| SARIMA             | 26156.80    | 1.10e+09    | 33122.17    | -0.6140   |

📌 Full comparison available in [Model_Comparison_Metrics.csv](https://github.com/ranjansatvik/CryptoCast/blob/main/outputs/metrics/Model_Comparison_Metrics.csv)

---

## ✅ Conclusion

This project demonstrates that while traditional time series models like ARIMA and SARIMA provide a foundational understanding of Bitcoin price trends, they fall short in capturing the complex, nonlinear patterns inherent in cryptocurrency data. Deep learning models, particularly LSTM, significantly outperform traditional methods, achieving an R² score above 0.99. The LSTM model also excels in terms of MAE and RMSE, proving to be the most effective standalone model.

Moreover, stacking multiple models using ensemble techniques further improved prediction accuracy, striking a balance between overfitting and generalization. Hybrid models combining ARIMA and BiLSTM or LSTM and BiLSTM show promise but are slightly less effective than pure LSTM or stacked ensembles in this context.

While results are promising, further work could include integrating external factors (e.g., news sentiment, trading volume) or testing on other cryptocurrencies. The insights here provide a solid foundation for more robust crypto price forecasting systems.

---

## 📷 Screenshots

| Model Comparison | Metrics |
|------------------|--------------------|
| ![All Models](./outputs/figures/All_Model_Comparison.png) | ![Bar Chart](./outputs/figures/Model_Comparison_Metrics.png) |

---

## 📜 License

This project is licensed under the MIT License.

---

## 📬 Contact

Satvik Ranjan — [LinkedIn](https://www.linkedin.com/in/satvik-ranjan/)
Veni Madhav — [LinkedIn](https://www.linkedin.com/in/venimadhav/)
Shikhar Srivastava — [LinkedIn](https://www.linkedin.com/in/shikhar004/)

Project Link: [CryptoCast](https://github.com/ranjansatvik/CryptoCast)

---
