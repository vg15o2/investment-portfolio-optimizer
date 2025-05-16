<!--isualize risk-return trade-offs.
- Optimize portfolios for maximum Sharpe Ratio or minimum volatility.
- Plot the Efficient Fronti
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


-->

# 💰 Investment Portfolio Optimizer

> *"Risk comes from not knowing what you're doing." – Warren Buffett*

A Python-powered tool that helps you optimize investment portfolios using **Modern Portfolio Theory (MPT)** and **Monte Carlo simulations**. Analyze, simulate, and visualize risk-return trade-offs with confidence. 📊📈

---

## Table of Contents
- [Features](#-features)
- [Installation](#-installation)
- [Usage](#-usage)
- [Visuals](#-visuals)
- [Concepts](#-concepts)
- [Contributing](#-contributing)
- [License](#-license)

---

## Features

- Fetch historical stock data using `yfinance`.
- Perform **Monte Carlo simulations** to explore portfolio risk/return combinations.
-  Optimize portfolios for:
  - Maximum **Sharpe Ratio**
  - Minimum **Volatility**
-  Plot the **Efficient Frontier**.
-  Export allocation data and visuals for reporting.

---

##  Installation

1. **Clone the repository**  
    ```bash
    git clone https://github.com/your-username/investment-portfolio-optimizer.git
    cd investment-portfolio-optimizer
    ```

2. **Install dependencies**  
    ```bash
    pip install -r requirements.txt
    ```

---

##  Usage

### 1. Fetch Historical Data
```bash
python fetch_data.py --ticker AAPL --start 2020-01-01 --end 2021-01-01
````

### 2.  Run Monte Carlo Simulations

```bash
python monte_carlo.py --iterations 1000
```

### 3. Optimize Portfolio

```bash
python optimize.py --objective sharpe_ratio
```

### 4.  Plot Efficient Frontier

```bash
python plot_efficient_frontier.py
```

---

## Visuals

![Figure_1](https://github.com/user-attachments/assets/ac7558ac-838e-4e05-b297-4619ded51cf9)


>  Simulated portfolios, color-coded by Sharpe ratio.
> Red Star = Max Sharpe 📍 | Green Star = Min Volatility ✅

![Figure_2](https://github.com/user-attachments/assets/216091da-4999-4234-ac4a-fde8abe8ea50)

## Concepts

### Modern Portfolio Theory (MPT)

* A strategy to construct a portfolio that **maximizes return** for a **given level of risk**.
* Introduced by **Harry Markowitz**, focuses on **diversification** and the **Efficient Frontier**.

### Monte Carlo Simulation

* Generates thousands of portfolio combinations with random weights.
* Helps estimate **distribution of returns** and identify **optimal portfolios**.

---

## Contributing

We welcome contributions! 🛠️

1. Fork the repo
2. Create a branch:
   `git checkout -b feature-branch`
3. Commit your changes:
   `git commit -am 'Add new feature'`
4. Push the branch:
   `git push origin feature-branch`
5. Create a Pull Request!

---

## 📄 License

This project is licensed under the **MIT License**. See the [LICENSE](LICENSE) file for details.

---


