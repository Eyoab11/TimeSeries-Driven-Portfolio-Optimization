
    # Quantitative Portfolio Strategy

    ## Business Objective
    This project, developed for GMF Investments, leverages time series forecasting and Modern Portfolio Theory (MPT) to build an optimized investment portfolio. The primary goal is to enhance portfolio performance by forecasting trends for a high-growth asset (TSLA) and balancing it with stable assets (BND, SPY) to maximize risk-adjusted returns.

    ---

    ## Table of Contents
    1. [Data Ingestion & EDA](#data-ingestion--eda)
    2. [Time Series Modeling](#time-series-modeling)
    3. [Portfolio Optimization](#portfolio-optimization)
    4. [Strategy Backtesting](#strategy-backtesting)
    5. [Results & Recommendation](#results--recommendation)
    6. [Project Structure](#project-structure)
    7. [How to Run](#how-to-run)

    ---

    ## Data Ingestion & EDA
    - **Data Source:** `yfinance` API.
    - **Assets:** Tesla (TSLA), Vanguard Total Bond Market ETF (BND), S&P 500 ETF (SPY).
    - **Period:** July 1, 2015 - July 31, 2025.
    - **Key Findings:** Documented key trends, volatility analysis, and stationarity tests (ADF).

    ## Time Series Modeling
    Two models were developed to forecast TSLA's adjusted closing price:
    - **Classical Model:** ARIMA/SARIMA (using `statsmodels` and `pmdarima`).
    - **Deep Learning Model:** LSTM (using `tensorflow.keras`).
    - **Evaluation Metrics:** MAE, RMSE, MAPE.

    ## Portfolio Optimization
    - **Methodology:** Modern Portfolio Theory (MPT).
    - **Inputs:**
        - Expected returns for TSLA from the best-performing forecast model.
        - Historical average returns for BND and SPY.
        - Covariance matrix from historical data of all three assets.
    - **Output:** The Efficient Frontier, identifying the Maximum Sharpe Ratio and Minimum Volatility portfolios.

    ## Strategy Backtesting
    - **Period:** August 1, 2024 - July 31, 2025.
    - **Strategy:** Rebalancing based on the optimized weights derived from the MPT analysis.
    - **Benchmark:** A static 60/40 SPY/BND portfolio.
    - **Analysis:** Comparison of cumulative returns and Sharpe Ratios.

    ## Results & Recommendation
    A summary of the findings, including the final recommended portfolio weights for GMF's investment committee.

    ---

    ## Project Structure
    ```
    Quantitative-Portfolio-Strategy/.github/workflows
Quantitative-Portfolio-Strategy/data/raw
Quantitative-Portfolio-Strategy/data/processed
Quantitative-Portfolio-Strategy/notebooks
Quantitative-Portfolio-Strategy/reports/figures
Quantitative-Portfolio-Strategy/src
Quantitative-Portfolio-Strategy/tests
    ```

    ## How to Run
    1. Clone the repository:
       ```bash
       git clone https://github.com/your-username/Quantitative-Portfolio-Strategy.git
       cd Quantitative-Portfolio-Strategy
       ```
    2. Create a virtual environment and activate it:
       ```bash
       python -m venv venv
       source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
       ```
    3. Install the required dependencies:
       ```bash
       pip install -r requirements.txt
       ```
    4. Run the Jupyter notebooks in the `/notebooks` directory to see the workflow.
