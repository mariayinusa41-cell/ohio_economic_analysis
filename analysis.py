"""
Econometric analysis of Ohio economic indicators.

This script downloads time series data for the unemployment rate in Ohio, manufacturing employment, and housing permits from FRED, merges them into a single DataFrame, and runs a multiple linear regression to investigate how manufacturing employment and housing permits relate to the unemployment rate.

Usage:
    python analysis.py

Before running, set the environment variable `FRED_API_KEY` with your personal FRED API key.  You can obtain a key for free by registering at https://fred.stlouisfed.org/.
"""

import os
import pandas as pd
import pandas_datareader.data as web
import statsmodels.api as sm
import matplotlib.pyplot as plt

# Retrieve FRED API key from environment
fred_api_key = os.getenv('FRED_API_KEY', None)
if fred_api_key is None:
    print("Warning: FRED_API_KEY not set. Data retrieval may fail if FRED limits unauthenticated requests.")

# Define FRED series codes
SERIES = {
    'unemployment_rate': 'OHUR',        # Unemployment Rate in Ohio
    'manufacturing_employment': 'OHMANEMP',  # All Employees: Manufacturing in Ohio
    'housing_permits': 'PERMITOH'           # Building permits for housing units in Ohio
}

# Define time range
START_DATE = '2000-01-01'
END_DATE = None  # Use most recent available

def download_series(series_codes: dict, start: str, end: str, api_key: str) -> pd.DataFrame:
    """Download FRED time series given a mapping of names to series codes."""
    df = pd.DataFrame()
    for name, code in series_codes.items():
        df[name] = web.DataReader(code, 'fred', start, end, api_key=api_key)
    return df


def run_regression(df: pd.DataFrame) -> sm.regression.linear_model.RegressionResultsWrapper:
    """Run a linear regression of unemployment rate on other indicators."""
    # Drop missing values
    data = df.dropna().copy()
    y = data['unemployment_rate']
    X = data[['manufacturing_employment', 'housing_permits']]
    X = sm.add_constant(X)
    model = sm.OLS(y, X).fit()
    return model


def plot_series(df: pd.DataFrame) -> None:
    """Plot the time series and a scatter matrix and save the figures."""
    os.makedirs('results', exist_ok=True)
    # Line plots
    plt.figure()
    df.plot(subplots=True, title='Economic Indicators in Ohio')
    plt.tight_layout()
    plt.savefig('results/ohio_indicators.png')
    plt.close()
    # Scatter matrix
    pd.plotting.scatter_matrix(df.dropna(), figsize=(8, 8))
    plt.savefig('results/scatter_matrix.png')
    plt.close()


def main() -> None:
    df = download_series(SERIES, START_DATE, END_DATE, fred_api_key)
    model = run_regression(df)
    print(model.summary())
    plot_series(df)


if __name__ == '__main__':
    main()
