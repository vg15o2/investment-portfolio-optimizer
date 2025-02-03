from setuptools import setup, find_packages

setup(
    name="portfolio_optimizer",
    version="0.1",
    packages=find_packages(),
    install_requires=[
        "pandas",
        "numpy",
        "matplotlib",
        "yfinance",
        "scipy",
    ],
    entry_points={
        "console_scripts": [
            "portfolio-optimizer=src.portfolio_optimizer:main",
        ],
    },
)
