# Investment Portfolio Optimizer

A Python tool to optimize investment portfolios using Modern Portfolio Theory (MPT). Features include risk-return analysis, Monte Carlo simulations, and portfolio suggestions.

## Table of Contents
- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [Contributing](#contributing)
- [License](#license)

## Features
- Fetch historical stock data using `yfinance`.
- Perform Monte Carlo simulations to visualize risk-return trade-offs.
- Optimize portfolios for maximum Sharpe Ratio or minimum volatility.
- Plot the Efficient Frontier.

## Installation
1. Clone the repository:
    ```bash
    git clone https://github.com/your-username/investment-portfolio-optimizer.git
    ```
2. Install dependencies:
    ```bash
    pip install -r requirements.txt
    ```

## Usage
1. Fetch historical stock data:
    ```bash
    python fetch_data.py --ticker AAPL --start 2020-01-01 --end 2021-01-01
    ```
2. Perform Monte Carlo simulations:
    ```bash
    python monte_carlo.py --iterations 1000
    ```
3. Optimize portfolio:
    ```bash
    python optimize.py --objective sharpe_ratio
    ```
4. Plot the Efficient Frontier:
    ```bash
    python plot_efficient_frontier.py
    ```

## Contributing
Contributions are welcome! Please follow these steps:
1. Fork the repository.
2. Create a new branch (`git checkout -b feature-branch`).
3. Commit your changes (`git commit -am 'Add new feature'`).
4. Push to the branch (`git push origin feature-branch`).
5. Create a new Pull Request.

## License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
