import os
import textwrap

# --- Project Configuration ---
REPO_NAME = "Quantitative-Portfolio-Strategy"

# Define the directory structure
DIRECTORIES = [
    f"{REPO_NAME}/.github/workflows",
    f"{REPO_NAME}/data/raw",
    f"{REPO_NAME}/data/processed",
    f"{REPO_NAME}/notebooks",
    f"{REPO_NAME}/reports/figures",
    f"{REPO_NAME}/src",
    f"{REPO_NAME}/tests",
]

# --- File Content Definitions ---

# .gitignore content
GITIGNORE_CONTENT = textwrap.dedent("""
    # Byte-compiled / optimized / DLL files
    __pycache__/
    *.pyc
    *.pyo
    *.pyd

    # Distribution / packaging
    .Python
    build/
    develop-eggs/
    dist/
    downloads/
    eggs/
    .eggs/
    lib/
    lib64/
    parts/
    sdist/
    var/
    wheels/
    *.egg-info/
    .installed.cfg
    *.egg
    MANIFEST

    # Jupyter Notebook
    .ipynb_checkpoints
    
    # Virtual Environments
    .env
    .venv
    env/
    venv/
    ENV/

    # Data files - Crucial for not uploading large datasets
    data/
    
    # Model files
    models/
    *.h5
    *.pkl
    *.joblib

    # IDE / Editor specific
    .idea/
    .vscode/
    *.suo
    *.ntvs*
    *.njsproj
    *.sln
    *.sw?
""")

# requirements.txt content
REQUIREMENTS_CONTENT = textwrap.dedent("""
    # Core Libraries
    pandas
    numpy
    scikit-learn
    
    # Data Source
    yfinance
    
    # Time Series Modeling
    statsmodels
    pmdarima
    tensorflow
    
    # Portfolio Optimization
    PyPortfolioOpt
    
    # Visualization
    matplotlib
    seaborn
    
    # Utilities & Quality
    jupyterlab
    black
    flake8
    pytest
""")

# README.md template
README_CONTENT = textwrap.dedent(f"""
    # {REPO_NAME.replace('-', ' ')}

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
    {os.linesep.join(DIRECTORIES)}
    ```

    ## How to Run
    1. Clone the repository:
       ```bash
       git clone https://github.com/your-username/{REPO_NAME}.git
       cd {REPO_NAME}
       ```
    2. Create a virtual environment and activate it:
       ```bash
       python -m venv venv
       source venv/bin/activate  # On Windows, use `venv\\Scripts\\activate`
       ```
    3. Install the required dependencies:
       ```bash
       pip install -r requirements.txt
       ```
    4. Run the Jupyter notebooks in the `/notebooks` directory to see the workflow.
""")

# GitHub Actions CI/CD workflow
CI_YAML_CONTENT = textwrap.dedent("""
    name: Python CI/CD

    on:
      push:
        branches: [ main ]
      pull_request:
        branches: [ main ]

    jobs:
      build:
        runs-on: ubuntu-latest
        strategy:
          matrix:
            python-version: ["3.9", "3.10"]

        steps:
        - uses: actions/checkout@v3
        - name: Set up Python ${{ matrix.python-version }}
          uses: actions/setup-python@v4
          with:
            python-version: ${{ matrix.python-version }}
        
        - name: Install dependencies
          run: |
            python -m pip install --upgrade pip
            pip install flake8 pytest
            if [ -f requirements.txt ]; then pip install -r requirements.txt; fi
            
        - name: Lint with flake8
          run: |
            # stop the build if there are Python syntax errors or undefined names
            flake8 . --count --select=E9,F63,F7,F82 --show-source --statistics
            # exit-zero treats all errors as warnings. The GitHub editor is 127 chars wide
            flake8 . --count --exit-zero --max-complexity=10 --max-line-length=127 --statistics
            
        - name: Test with pytest
          run: |
            pytest
""")

# --- Script Logic ---

def create_project_structure():
    """Generates the project folders and files."""
    print(f"Creating project structure for '{REPO_NAME}'...")

    # Create root directory
    os.makedirs(REPO_NAME, exist_ok=True)

    # Create subdirectories
    for path in DIRECTORIES:
        os.makedirs(path, exist_ok=True)

    # Dictionary of files to create with their content
    files_to_create = {
        f"{REPO_NAME}/.gitignore": GITIGNORE_CONTENT,
        f"{REPO_NAME}/requirements.txt": REQUIREMENTS_CONTENT,
        f"{REPO_NAME}/README.md": README_CONTENT,
        f"{REPO_NAME}/LICENSE": "Add your chosen license text here (e.g., MIT License).",
        f"{REPO_NAME}/.github/workflows/python-ci.yml": CI_YAML_CONTENT,
        f"{REPO_NAME}/src/__init__.py": "",
        f"{REPO_NAME}/tests/__init__.py": "",
        # Add empty notebooks and script files
        f"{REPO_NAME}/notebooks/01_data_extraction_and_eda.ipynb": "{\n \"cells\": [],\n \"metadata\": {},\n \"nbformat\": 4,\n \"nbformat_minor\": 2\n}",
        f"{REPO_NAME}/notebooks/02_arima_modeling.ipynb": "{\n \"cells\": [],\n \"metadata\": {},\n \"nbformat\": 4,\n \"nbformat_minor\": 2\n}",
        f"{REPO_NAME}/notebooks/03_lstm_modeling.ipynb": "{\n \"cells\": [],\n \"metadata\": {},\n \"nbformat\": 4,\n \"nbformat_minor\": 2\n}",
        f"{REPO_NAME}/notebooks/04_portfolio_optimization.ipynb": "{\n \"cells\": [],\n \"metadata\": {},\n \"nbformat\": 4,\n \"nbformat_minor\": 2\n}",
        f"{REPO_NAME}/notebooks/05_strategy_backtesting.ipynb": "{\n \"cells\": [],\n \"metadata\": {},\n \"nbformat\": 4,\n \"nbformat_minor\": 2\n}",
        f"{REPO_NAME}/src/data_ingestion.py": "# Functions for fetching data from yfinance",
        f"{REPO_NAME}/src/feature_engineering.py": "# Functions for data cleaning and feature creation",
        f"{REPO_NAME}/src/modeling.py": "# Functions/classes for ARIMA and LSTM models",
        f"{REPO_NAME}/src/optimization.py": "# Functions for portfolio optimization using PyPortfolioOpt",
        f"{REPO_NAME}/src/backtesting.py": "# Logic for running the backtest simulation",
        f"{REPO_NAME}/src/visualization.py": "# Reusable plotting functions",
        f"{REPO_NAME}/tests/test_feature_engineering.py": "# Unit tests for feature engineering functions",
    }

    # Create files with content
    for path, content in files_to_create.items():
        with open(path, 'w') as f:
            f.write(content)

    print("Project structure created successfully!")
    print(f"Next steps:")
    print(f"1. cd {REPO_NAME}")
    print("2. git init")
    print("3. git add .")
    print("4. git commit -m 'Initial project structure'")
    print("5. Create the repository on GitHub and push.")

if __name__ == "__main__":
    create_project_structure()