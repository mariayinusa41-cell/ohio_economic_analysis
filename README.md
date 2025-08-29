# Econometric Analysis of Ohio Economic Indicators

This project analyzes how economic indicators such as manufacturing employment and housing permits relate to Ohio's unemployment rate.  Using state level time series data from the Federal Reserve Bank of St. Louis (FRED) and the U.S. Bureau of Labor Statistics (BLS), a multiple regression model is fitted to examine which factors have the strongest association with unemployment.

## Data Sources

The data for this analysis can be obtained using the FRED API or downloaded directly from FRED/BLS websites.  Suggested series include:

- **Unemployment Rate in Ohio (`OHUR`)** – state level unemployment rate (monthly, seasonally adjusted).
- **All Employees: Manufacturing in Ohio (`OHMANEMP`)** – manufacturing employment levels measured in thousands.
- **Building Permits for Housing Units Authorized in Ohio (`PERMITOH`)** – number of housing units authorized by building permits.

You can explore additional variables to improve the model.

## Requirements

Install the required Python packages:

```bash
pip install pandas pandas_datareader matplotlib seaborn statsmodels
```

You will also need a FRED API key.  Create a free account at [FRED](https://fred.stlouisfed.org/) and obtain an API key.  Set it as an environment variable named `FRED_API_KEY` before running the script.

## Usage

Run the analysis script:

```bash
python analysis.py
```

The script performs the following steps:

1. Downloads time series data for the selected indicators from FRED.
2. Merges the series on their dates and drops missing values.
3. Performs multiple linear regression with the unemployment rate as the dependent variable and the other indicators as independent variables.
4. Prints the regression summary to the console.
5. Creates line plots of each series and a scatter matrix to explore relationships.

You can modify the script to include additional variables or change the time period of interest.

## Interpretation

The regression coefficients indicate the direction and magnitude of the relationship between each economic indicator and Ohio's unemployment rate.  Statistical significance (p values) helps determine whether an indicator is a meaningful predictor.  Be cautious in interpreting causality; regression results show association rather than causation.

## Acknowledgements

Data used in this project are courtesy of the Federal Reserve Bank of St. Louis and the U.S. Bureau of Labor Statistics.
