import pandas as pd
import yfinance as yf

def fetch_data(tickers, start_date, end_date):
    """Fetch historical stock data and calculate returns."""
    print("Fetching historical data...")
    try:
        # Download data with multi-level columns
        data = yf.download(tickers, start=start_date, end=end_date, group_by='ticker')
        
        # Extract "Adj Close" or "Close" prices for all tickers
        try:
            adj_close = data.xs('Adj Close', level=1, axis=1)
        except KeyError:
            print("Warning: 'Adj Close' not found. Using 'Close' instead.")
            adj_close = data.xs('Close', level=1, axis=1)
        
        # Handle missing data
        adj_close = adj_close.ffill().dropna()
        returns = adj_close.pct_change().dropna()
        expected_returns = returns.mean() * 252  # Annualize
        cov_matrix = returns.cov() * 252
        return expected_returns, cov_matrix, returns
    except Exception as e:
        print(f"Error fetching data: {e}")
        return None, None, None
