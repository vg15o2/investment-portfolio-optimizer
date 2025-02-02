# portfolio_optimizer.py
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import yfinance as yf
from scipy.optimize import minimize

# Step 1: Fetch Historical Data
def fetch_data(tickers, start_date, end_date):
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

# Step 2: Monte Carlo Simulation
def monte_carlo_simulation(expected_returns, cov_matrix, num_portfolios=10000):
    print("Running Monte Carlo simulation...")
    results = np.zeros((3, num_portfolios))
    for i in range(num_portfolios):
        weights = np.random.random(len(expected_returns))
        weights /= np.sum(weights)
        port_return = np.dot(weights, expected_returns)
        port_volatility = np.sqrt(weights.T @ cov_matrix @ weights)
        sharpe_ratio = port_return / port_volatility
        results[0, i] = port_return
        results[1, i] = port_volatility
        results[2, i] = sharpe_ratio
    return results.T

# Step 3: Portfolio Optimization
def optimize_portfolio(expected_returns, cov_matrix, risk_free_rate=0.02):
    print("Optimizing portfolio...")
    def negative_sharpe(weights):
        port_return = np.dot(weights, expected_returns)
        port_volatility = np.sqrt(weights.T @ cov_matrix @ weights)
        return -(port_return - risk_free_rate) / port_volatility

    constraints = ({'type': 'eq', 'fun': lambda x: np.sum(x) - 1})
    bounds = tuple((0, 1) for _ in range(len(expected_returns)))
    initial_weights = np.array([1/len(expected_returns)] * len(expected_returns))
    optimal = minimize(negative_sharpe, initial_weights, method='SLSQP', bounds=bounds, constraints=constraints)
    return optimal.x

# Step 4: Efficient Frontier Calculation
def efficient_frontier(expected_returns, cov_matrix, return_range):
    print("Calculating efficient frontier...")
    efficient_portfolios = []
    initial_weights = np.array([1/len(expected_returns)] * len(expected_returns))
    bounds = tuple((0, 1) for _ in range(len(expected_returns)))
    for target_return in return_range:
        constraints = (
            {'type': 'eq', 'fun': lambda x: np.sum(x) - 1},
            {'type': 'eq', 'fun': lambda x: np.dot(x, expected_returns) - target_return}
        )
        result = minimize(lambda x: np.sqrt(x.T @ cov_matrix @ x), initial_weights, method='SLSQP', bounds=bounds, constraints=constraints)
        efficient_portfolios.append(result.x)
    return efficient_portfolios

# Step 5: Visualization
def plot_results(results_df, efficient_volatilities, efficient_returns, optimal_weights, min_vol_weights, expected_returns, cov_matrix):
    print("Plotting results...")
    plt.figure(figsize=(12, 8))
    plt.scatter(results_df['Volatility'], results_df['Return'], c=results_df['Sharpe'], cmap='viridis', alpha=0.5)
    plt.colorbar(label='Sharpe Ratio')
    plt.xlabel('Volatility')
    plt.ylabel('Return')

    plt.plot(efficient_volatilities, efficient_returns, 'r--', linewidth=2, label='Efficient Frontier')
    
    optimal_return = np.dot(optimal_weights, expected_returns)
    optimal_volatility = np.sqrt(optimal_weights.T @ cov_matrix @ optimal_weights)
    plt.scatter(optimal_volatility, optimal_return, marker='*', color='r', s=200, label='Max Sharpe')

    min_vol_return = np.dot(min_vol_weights, expected_returns)
    min_vol_volatility = np.sqrt(min_vol_weights.T @ cov_matrix @ min_vol_weights)
    plt.scatter(min_vol_volatility, min_vol_return, marker='*', color='g', s=200, label='Min Volatility')

    plt.title('Efficient Frontier with Optimal Portfolios')
    plt.legend()
    plt.show()

# Step 6: Main Function
def main():
    # User inputs
    tickers = input("Enter tickers (comma-separated, e.g., AAPL,MSFT,GOOGL): ").split(',')
    start_date = input("Enter start date (YYYY-MM-DD, e.g., 2020-01-01): ")
    end_date = input("Enter end date (YYYY-MM-DD, e.g., 2023-01-01): ")

    # Fetch data
    expected_returns, cov_matrix, returns = fetch_data([ticker.strip() for ticker in tickers], start_date, end_date)
    if expected_returns is None:
        return

    # Monte Carlo simulation
    results = monte_carlo_simulation(expected_returns, cov_matrix)
    results_df = pd.DataFrame(results, columns=['Return', 'Volatility', 'Sharpe'])

    # Optimize portfolio
    optimal_weights = optimize_portfolio(expected_returns, cov_matrix)
    initial_weights = np.array([1/len(expected_returns)] * len(expected_returns))
    bounds = tuple((0, 1) for _ in range(len(expected_returns)))
    min_vol_result = minimize(lambda x: np.sqrt(x.T @ cov_matrix @ x), initial_weights, method='SLSQP', bounds=bounds, constraints={'type': 'eq', 'fun': lambda x: np.sum(x) - 1})
    min_vol_weights = min_vol_result.x

    # Efficient frontier
    return_range = np.linspace(expected_returns.min(), expected_returns.max(), 50)
    efficient_weights = efficient_frontier(expected_returns, cov_matrix, return_range)
    efficient_returns = [np.dot(weights, expected_returns) for weights in efficient_weights]
    efficient_volatilities = [np.sqrt(weights.T @ cov_matrix @ weights) for weights in efficient_weights]

    # Plot results
    plot_results(results_df, efficient_volatilities, efficient_returns, optimal_weights, min_vol_weights, expected_returns, cov_matrix)

    # Display portfolio metrics
    print("\nOptimal Portfolio Weights:")
    for ticker, weight in zip(tickers, optimal_weights):
        print(f"{ticker.strip()}: {weight:.2%}")

    optimal_return = np.dot(optimal_weights, expected_returns)
    optimal_volatility = np.sqrt(optimal_weights.T @ cov_matrix @ optimal_weights)
    print(f"\nExpected Return: {optimal_return:.2%}")
    print(f"Volatility: {optimal_volatility:.2%}")
    print(f"Sharpe Ratio: {optimal_return / optimal_volatility:.2f}")

if __name__ == "__main__":
    main()