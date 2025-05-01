# 📈 CryptoCast: Forecasting Bitcoin with AI

**CryptoCast** is a machine learning-powered project that forecasts future Bitcoin prices using traditional statistical models (ARIMA, SARIMA), deep learning (LSTM, BiLSTM), and ensemble strategies like stacking and averaging. Through comprehensive experimentation, we discovered that the LSTM model delivers the most accurate predictions, outperforming classical approaches by a significant margin.

---

## 📌 Table of Contents
- [Overview](#-overview)
- [Tech Stack](#-tech-stack)
- [Project Structure](#-project-structure)
- [How to Run](#-how-to-run)
- [Modeling Techniques](#-modeling-techniques)
- [Results](#-results)
- [Conclusion](#-conclusion)
- [Screenshots](#-screenshots)
- [Contact](#-contact)

---

## 🧠 Overview

Bitcoin is one of the most volatile and highly traded digital assets in the financial market. Accurately forecasting its price is crucial for traders, investors, and researchers. This project investigates various models ranging from simple statistical methods to advanced neural networks, using historical price data to predict future movements.

We implemented and compared ARIMA, SARIMA, LSTM, BiLSTM, hybrid average models, and a stacked ensemble to find the most accurate forecasting approach. The LSTM model emerged as the best performer.

---

## 🛠️ Tech Stack

- **Programming Language**: Python 3.9.13
- **Environment**: VS Code, Jupyter Notebooks
- **Libraries**: `pmdarima`, `scikit-learn`, `matplotlib`, `seaborn`, `tensorflow`, `xgboost`, `pandas`, `numpy`
- **Models Used**:
  - ARIMA
  - SARIMA
  - LSTM
  - BiLSTM
  - Ensemble (Averaging & Stacking)

---

## 📁 Project Structure

```
CryptoCast/
├── data/                      # Raw data files
├── models/                    # Saved model files (.pkl, .keras)
├── outputs/
│   ├── figures/               # All visualizations
│   └── metrics/               # Model predictions and metrics
├── src/                       # Preprocessing and utility scripts
├── notebooks/                 # Jupyter modeling notebooks
├── README.md                  # Project overview
```

---

## 🚀 How to Run

1. **Clone the repository**
   ```bash
   git clone https://github.com/your-username/CryptoCast.git
   cd CryptoCast
   ```

2. **Create a virtual environment**
   ```bash
   python -m venv venv
   source venv/bin/activate  # or venv\Scripts\activate on Windows
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Run the notebooks**
   Launch Jupyter Notebook or JupyterLab and execute the notebooks inside the `notebooks/` folder.

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

## 📊 Results (Top 3 Models by RMSE)

| Model               | MAE       | RMSE      | R² Score |
|--------------------|-----------|-----------|----------|
| **LSTM**           | 1,440.88  | 1,960.98  | 0.9943   |
| **Stacked**        | 1,891.38  | 2,603.45  | 0.9899   |
| **Avg_LSTM_BiLSTM**| 1,910.78  | 2,909.12  | 0.9875   |

📌 Full comparison available in `/outputs/metrics/Model_Comparison_Metrics.csv`

---

## ✅ Conclusion

Deep learning models, particularly **LSTM**, significantly outperformed traditional methods like ARIMA and SARIMA. Among all tested models, LSTM achieved the **lowest RMSE** and **highest R²**, making it the most suitable for crypto price prediction.

Traditional models are valuable for their interpretability, but ensembles and deep learning strategies demonstrate far superior forecasting capabilities for highly volatile assets like Bitcoin.

---

## 📷 Screenshots

| Model Comparison | Normalized Metrics |
|------------------|--------------------|
| ![All Models](./outputs/figures/All_Model_Comparison.png) | ![Bar Chart](./outputs/figures/Model_Comparison_Metrics.png) |

---

## 📬 Contact

For suggestions or collaborations, connect on [LinkedIn](https://https://www.linkedin.com/in/satvik-ranjan/)

---