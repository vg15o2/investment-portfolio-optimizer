import unittest
import numpy as np
from src.portfolio_optimizer import optimize_portfolio, monte_carlo_simulation
from src.utils import fetch_data

class TestPortfolioOptimizer(unittest.TestCase):
    def test_optimize_portfolio(self):
        """Test portfolio optimization."""
        # Mock data
        expected_returns = np.array([0.1, 0.2])
        cov_matrix = np.array([[0.1, 0.02], [0.02, 0.2]])
        
        # Optimize portfolio
        weights = optimize_portfolio(expected_returns, cov_matrix)
        
        # Check if weights sum to 1
        self.assertTrue(np.allclose(np.sum(weights), 1.0))

    def test_monte_carlo_simulation(self):
        """Test Monte Carlo simulation."""
        # Mock data
        expected_returns = np.array([0.1, 0.2])
        cov_matrix = np.array([[0.1, 0.02], [0.02, 0.2]])
        
        # Run simulation
        results = monte_carlo_simulation(expected_returns, cov_matrix, num_portfolios=100)
        
        # Check if results have the correct shape
        self.assertEqual(results.shape, (100, 3))

    def test_fetch_data(self):
        """Test data fetching."""
        tickers = ["AAPL", "MSFT"]
        start_date = "2020-01-01"
        end_date = "2023-01-01"
        
        # Fetch data
        expected_returns, cov_matrix, returns = fetch_data(tickers, start_date, end_date)
        
        # Check if data is returned
        self.assertIsNotNone(expected_returns)
        self.assertIsNotNone(cov_matrix)
        self.assertIsNotNone(returns)

if __name__ == "__main__":
    unittest.main()
